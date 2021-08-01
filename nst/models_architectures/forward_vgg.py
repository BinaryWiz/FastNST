import torch
import torch.nn as nn
import torchvision
from torchvision.models import vgg19

class ForwardVGG19(torch.nn.Module):
    def __init__(self):
        super(ForwardVGG19, self).__init__()
        vgg = vgg19(pretrained=True)
        vgg.eval()
        self.features = vgg.features
        
    def forward(self, x, layers):
        results = []
        for i, model in enumerate(self.features):
            x = model(x)

            if i in layers:
                results.append(x)
                        
        return results
