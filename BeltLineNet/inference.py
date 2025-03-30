from ultralytics import YOLO
import torch



if __name__ == '__main__':
    weight = 'weights/val_weight.pt'
    model = YOLO(weight)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    validation_results = model.val(data='validation.yaml', device=device)
    result = model('test_vedio/Task_1_test1.mp4',show=True,save=True)


