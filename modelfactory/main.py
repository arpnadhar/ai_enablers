from transfer_model import trf_modnet, mainSoc
import os
from export_modnet_onnx import export_model

if __name__ == '__main__':
    #path = 'MattingDataset/train'
    # soc_path="MattingDataset/trainSoc"
    directory = os.getcwd()
    print("current directory = ", directory)

    # Code for training the dataset
    #E:\SriGanesh\PrePress\Burda\repository\traindataset
    #path = 'E:\\SriGanesh\\PrePress\\Burda\\repository\\traindataset'
    #trf_modnet(path, std=10)

    # Code for generalizing by training on unlabelled dataset to avoid over fitting of model
    # on train data set
    export_model()
    soc_path = 'E:\\SriGanesh\\PrePress\\Burda\\repository\\trainsoc'
    mainSoc(soc_path)

