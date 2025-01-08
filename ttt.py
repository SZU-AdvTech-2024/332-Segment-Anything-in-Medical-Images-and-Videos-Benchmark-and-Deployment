import torch
from torchsummary import summary

path = "/home/ybc/MedSAM/work_dir/FLARE22Train/medsam_model_best.pth"
device = "cuda:0" if torch.cuda.is_available() else "cpu"
model = torch.load(path, map_location = device)
# map_location 参数可选，用于在多卡GPU中训练和推理使用的 CUDA 序号不一样的情况
print(model)