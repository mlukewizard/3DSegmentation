from __future__ import print_function
from keras.callbacks import ModelCheckpoint
from keras.models import Model, load_model
from keras.layers import Input, Conv2D, MaxPooling2D, UpSampling2D, concatenate, ConvLSTM2D, TimeDistributed, Bidirectional
from keras.optimizers import Adam
from keras import losses
import numpy as np
import h5py
import matplotlib
import matplotlib.pyplot as plt


model_file = '/media/sf_sharedFolder/Models/23rdNov/weights.03-0.03.h5'

x = np.load('/media/sf_sharedFolder/npArrays/39894NS/3DAugment001-002PatientNS_Original.npy')

fig = plt.figure()
#model = load_model(model_file)
npImageArray = np.ndarray((1, 3, 256, 256, 1), dtype='float32')

for i in range(200, 400, 50):
    x1 = x[i, 1, :, :, 0]
    x2 = x[i, 1, :, :, 0]
    x3 = x[i, 2, :, :, 0]
    npImageArray[0, :, :, :, 0] = x[i, :, :, :, 0]

    #y = model.predict(npImageArray)
    #y1 = y[0, 1, :, :, 0]

    #plt.subplot(121)
    #plt.imshow(x1, cmap='gray')
    #plt.subplot(122)
    #plt.imshow(y1, cmap='gray')
    #plt.show()
    plt.subplot(131)
    plt.imshow(x1, cmap='gray')
    plt.subplot(132)
    plt.imshow(x2, cmap='gray')
    plt.subplot(133)
    plt.imshow(x3, cmap='gray')
    plt.show()
