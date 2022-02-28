"""
Export onnx model

Arguments:
    --ckpt-path --> Path of last checkpoint to load
    --output-path --> path of onnx model to be saved

example:
    --ckpt-path=modnet_photographic_portrait_matting.ckpt \
    --output-path=modnet.onnx

output:
ONNX model with dynamic input shape: (batch_size, 3, height, width) &
                        output shape: (batch_size, 1, height, width)                  
"""
import os
import argparse
import torch
import torch.nn as nn
from torch.autograd import Variable
# from src.models.onnx_modnet import MODNet
from models.modnet.src.models.modnet import MODNet
import config


def export_model():
    # check input arguments
    if not os.path.exists(config.ckpt_path):
        print('Cannot find checkpoint path: {0}'.format(config.ckpt_path))
        exit()

    # define model & load checkpoint
    modnet = MODNet(backbone_pretrained=False)
    #AD modnet = nn.DataParallel(modnet).cuda()
    modnet = nn.DataParallel(modnet)
    state_dict = torch.load(config.ckpt_path)
    modnet.load_state_dict(state_dict)
    modnet.eval()
    #AD
    modnet.train(False)
    # prepare dummy_input
    batch_size = 1
    height = 512
    width = 512
    #AD dummy_input = Variable(torch.randn(batch_size, 3, height, width)).cuda()
    dummy_input = Variable(torch.randn(batch_size, 3, height, width))
    # AD Let's create a dummy input tensor
    # dummy_input = torch.randn(batch_size, (3*height* width)) #, requires_grad=True, inference=True)

    # export to onnx model
    torch.onnx.export(modnet.module, dummy_input, config.model_path, export_params = True, opset_version=11,
                    input_names = ['input'], output_names = ['output'], 
                    dynamic_axes = {'input': {0:'batch_size', 2:'height', 3:'width'},
                                    'output': {0: 'batch_size', 2: 'height', 3: 'width'}})
