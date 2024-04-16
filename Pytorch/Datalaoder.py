from torch.utils.data import Dataset, DataLoader
 
class CustomDataset(Dataset):
    def __init__(self, data_len):
        self.data_len = data_len
 
    def __getitem__(self, idx):
        return f"Data at index {idx}"
 
    def __len__(self):
        return self.data_len
 
if __name__ == "__main__":
    data_len = 10
 
    dataset = CustomDataset(data_len)
    print("Dataset:")
    for i in range(data_len):
        data_item = dataset[i]
        print(data_item)
 
    print("0. DataLoader(batch_size=1, shuffle=False, drop_last=False):")
    dataloader = DataLoader(dataset)
    for batch in dataloader:
        print(batch)
 
    print("\n1. DataLoader(batch_size=4):")
    dataloader = DataLoader(dataset, batch_size=4)
    for batch in dataloader:
        print(batch)
 
    print("\n2. DataLoader(batch_size=4, shuffle=True):")
    dataloader = DataLoader(dataset, batch_size=4, shuffle=True)
    for batch in dataloader:
        print(batch)
 
    print("\n3. DataLoader(batch_size=4, shuffle=True, drop_last=True):")
    dataloader = DataLoader(dataset, batch_size=4, shuffle=True, drop_last=True)
    for batch in dataloader:
        print(batch)
        
# ----------------------------------------------------------------------------------------------------------
# Dataset:    # Dataset每次只能读取一个样本
# Data at index 0
# Data at index 1
# Data at index 2
# Data at index 3
# Data at index 4
# Data at index 5
# Data at index 6
# Data at index 7
# Data at index 8
# Data at index 9
 
# # Dataloader默认的参数
# 0. DataLoader(batch_size=1, shuffle=False, drop_last=False):
# ['Data at index 0']
# ['Data at index 1']
# ['Data at index 2']
# ['Data at index 3']
# ['Data at index 4']
# ['Data at index 5']
# ['Data at index 6']
# ['Data at index 7']
# ['Data at index 8']
# ['Data at index 9']
 
# # Dataloader跟返回值相关的参数
# 1. DataLoader(batch_size=4):
# ['Data at index 0', 'Data at index 1', 'Data at index 2', 'Data at index 3']
# ['Data at index 4', 'Data at index 5', 'Data at index 6', 'Data at index 7']
# ['Data at index 8', 'Data at index 9']
 
# 2. DataLoader(batch_size=4, shuffle=True):
# ['Data at index 8', 'Data at index 3', 'Data at index 2', 'Data at index 1']
# ['Data at index 4', 'Data at index 0', 'Data at index 6', 'Data at index 9']
# ['Data at index 7', 'Data at index 5']
 
# 3. DataLoader(batch_size=4, shuffle=True, drop_last=True):
# ['Data at index 6', 'Data at index 5', 'Data at index 7', 'Data at index 2']
# ['Data at index 1', 'Data at index 3', 'Data at index 8', 'Data at index 0']