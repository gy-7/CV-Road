import cv2
import json
import torch.utils.Dataset as Dataset


class CustomDataset(Dataset):
    def __init__(self, imgs_path, labels_path, img_transform=None, label_transform=None):
        self.imgs_path = imgs_path  # 输入图像的路径，list
        self.labels_path = labels_path  # 输入图像对应的标签路径，list
        self.img_transform = img_transform  # 图像的数据增强
        self.label_transform = label_transform  # 标签的数据增强

    def __len__(self):
        return len(self.imgs_path)  # 返回数据集的长度

    def __getitem__(self, idx):
        img_path = self.imgs_path[idx]
        label_path = self.labels_path[idx]
        img = cv2.imread(img_path)  # 读取图像
        label = json.load(open(label_path))  # 读取标签
        if self.img_transform:  # 图像的数据增强
            img = self.img_transform(img)
        if self.label_transform:  # 标签的数据增强
            label = self.label_transform(label)
        return img, label  # 返回图像和标签，用于训练
