# CV-Road
Pytorch Dataset code：torch/utils/data/dataset.py#L17 
Pytorch Dataset tutorial: tutorials/beginner/basics/data_tutorial.html 
理论：
PyTorch中的Dataset是一个抽象类，用来表示数据集的接口，所有其他数据集都需要继承这个类，并且覆写以下三个方法：
1. __init__：初始化数据集的一些配置，例如加载所有的数据标签。
2. __len__：以便len(dataset)可以返回数据集的大小，例如n。如果n小于数据集长度，则只会取前n个的数据。
3. __getitem__：输入是数据的索引，以便可以使用dataset[i]来获取第i个样本，数据增强一般会在这里做。