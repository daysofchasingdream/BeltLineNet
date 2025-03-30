import torch
import torch.nn as nn
from einops import rearrange
__all__ = ['Aggregate_CGA', 'Enhancement_Glob_loc', 'BeltLineEnhance']

class Aggregate_CGA(nn.Module):
    def __init__(self, dim):
        super(Aggregate_CGA, self).__init__()
        self.group_conv = nn.Conv2d(2 * dim, dim, 7, padding=3, padding_mode='reflect', groups=dim, bias=True)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x, temp):
        x, temp = x.unsqueeze(dim=2), temp.unsqueeze(dim=2)
        x_concat = torch.cat([x, temp], dim=2)
        x_concat = rearrange(x_concat, 'b c t h w -> b (c t) h w')
        ratio_raw = self.sigmoid(self.group_conv(x_concat))
        return ratio_raw

class Enhancement_Glob_loc(nn.Module):
    def __init__(self, dim, num_heads=8, bias=False):
        super(Enhancement_Glob_loc, self).__init__()
        self.num_heads = num_heads
        self.temperature = nn.Parameter(torch.ones(num_heads, 1, 1))

        self.conv1 = nn.Conv3d(dim, dim * 3, kernel_size=(1, 1, 1), bias=bias)
        self.DepthWiseConv = nn.Conv3d(dim * 3, dim * 3, kernel_size=(3, 3, 3), stride=1, padding=1, groups=dim * 3, bias=bias)
        self.conv3 = nn.Conv3d(dim, dim, kernel_size=(1, 1, 1), bias=bias)
        self.conv2 = nn.Conv3d(3 * self.num_heads, 9, kernel_size=(1, 1, 1), bias=True)

        self.dep_group_conv = nn.Conv3d(9 * dim // self.num_heads, dim, kernel_size=(3, 3, 3), bias=True,
                                  groups=dim // self.num_heads, padding=1)


    def forward(self, x):
        b, c, h, w = x.shape
        qkv = self.DepthWiseConv(self.conv1(x.unsqueeze(2)))
        qkv = qkv.squeeze(2)

        # local conv
        temp1 = qkv.permute(0, 2, 3, 1)
        temp2 = qkv.reshape(temp1.shape[0], h * w, 3 * self.num_heads, -1).permute(0, 2, 1, 3)
        temp2 = self.conv2(temp2.unsqueeze(2))
        temp2 = temp2.squeeze(2)
        temp1 = temp2.permute(0, 3, 1, 2).reshape(x.shape[0], 9 * x.shape[1] // self.num_heads, h, w)
        temp1 = temp1.unsqueeze(2)
        local_out = self.dep_group_conv(temp1)  # B, C, H, W
        local_out = local_out.squeeze(2)

        # global branch
        Q, K, V = qkv.chunk(3, dim=1)
        Q = rearrange(Q, 'b (head c) h w -> b head c (h w)', head=self.num_heads)
        K = rearrange(K, 'b (head c) h w -> b head c (h w)', head=self.num_heads)
        V = rearrange(V, 'b (head c) h w -> b head c (h w)', head=self.num_heads)
        Q = torch.nn.functional.normalize(Q, dim=-1)
        K = torch.nn.functional.normalize(K, dim=-1)
        attention_map = (Q @ K.transpose(-2, -1)) * self.temperature
        attention_map = attention_map.softmax(dim=-1)
        glob_out = (attention_map @ V)

        glob_out = rearrange(glob_out, 'b head c (h w) -> b (head c) h w', head=self.num_heads, h=h, w=w)
        glob_out = glob_out.unsqueeze(2)
        glob_out = self.conv3(glob_out)
        glob_out = glob_out.squeeze(2)

        # merge the global and local features
        output = glob_out + local_out

        return output

class BeltLineEnhance(nn.Module):
    def __init__(self, dim, heads):
        super(BeltLineEnhance, self).__init__()
        self.g_l_enhance = Enhancement_Glob_loc(dim, num_heads=heads)
        self.agg = Aggregate_CGA(dim)
        self.conv = nn.Conv2d(dim, dim, 1, bias=True)
        self.sigmoid = nn.Sigmoid()

    def forward(self, primary_feature_extraction):
        low_level, high_level = primary_feature_extraction
        feature_before_enhance = low_level + high_level
        temp = self.g_l_enhance(feature_before_enhance)
        ratio = self.sigmoid(self.agg(feature_before_enhance, temp))
        result = feature_before_enhance + ratio * low_level + (1 - ratio) * high_level
        result = self.conv(result)
        return result

