import torchvision
from torch.utils.tensorboard import SummaryWriter

dataset_transform = torchvision.transforms.Compose([torchvision.transforms.ToTensor()])
train_set = torchvision.datasets.CIFAR10(root="/mnt/dataset", train= True, transform = dataset_transform, download = True)
test_set = torchvision.datasets.CIFAR10(root="/mnt/dataset", train= False, transform = dataset_transform, download = True)

writer = SummaryWriter("p10")
for i in range(10) :
    img, target = test_set[i]
    writer.add_image("test_set", img, i)
writer.close