from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from keras.preprocessing.image import img_to_array
from keras.utils import to_categorical
from imutils import paths
import matplotlib.pyplot as plt
import numpy as np
import argparse
import random
import cv2
import os
import pandas as pd
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as K
from keras.optimizers import Adam



data_labels = pd.read_csv("train.csv")

print(data_labels.head())

epochs = 100
batch_size = 500

data = []
labels = []
num_classes = 102
imagePaths = os.listdir('train')

print(len(imagePaths))
# loop over the input images
for imagePath in imagePaths:
    # load the image, pre-process it, and store it in the data list
    print('image = ', imagePath)
    image = cv2.imread('train/'+ imagePath)
    image = cv2.resize(image, (28, 28))
    image = img_to_array(image)
    data.append(image)

    # extract the class label from the image path and update the
    # labels list
    image_label = int(imagePath.split('.jpg')[0])
    label = data_labels['category'][image_label]
    print('image- label', label)
    labels.append(label-1)

# scale the raw pixel intensities to the range [0, 1]
data = np.array(data, dtype="float") / 255.0
labels = np.array(labels)

# partition the data into training and testing splits using 75% of
# the data for training and the remaining 25% for testing
(trainX, testX, trainY, testY) = train_test_split(data,
                                                  labels, test_size=0.25, random_state=42)

# convert the labels from integers to vectors
trainY = to_categorical(trainY, num_classes=num_classes)
testY = to_categorical(testY, num_classes=num_classes)




model = Sequential()
model.add(Conv2D(48, (5, 5), input_shape=(28, 28,3), activation='tanh'))
# model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

# model.add(Conv2D(32, (5, 5), activation='tanh'))
# # model.add(Activation('relu'))
# model.add(MaxPooling2D(pool_size=(5, 5), strides=(5, 5)))

model.add(Conv2D(64, (5, 5), activation='tanh'))
# model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(5, 5), strides=(5, 5)))

model.add(Flatten())
# model.add(Dense(64, activation='tanh'))
# model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(102,activation='softmax'))
# model.add(Activation('softmax'))

print('model', model.output)

opt = Adam(lr=0.00001)

model.compile(optimizer=opt,
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# this is the augmentation configuration we will use for training
train_datagen = ImageDataGenerator(rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

# this is the augmentation configuration we will use for testing:
# only rescaling
test_datagen = ImageDataGenerator(rescale=1. / 255)

# train_generator = train_datagen.flow_from_directory(
#     train_data_dir,
#     target_size=(img_width, img_height),
#     batch_size=batch_size,
#     color_mode='grayscale',
#     class_mode='categorical')
#
# validation_generator = test_datagen.flow_from_directory(
#     validation_data_dir,
#     target_size=(img_width, img_height),
#     batch_size=batch_size,
#     color_mode='grayscale',
#     class_mode='categorical')

# print('validation', validation_generator.batch_size)

model.fit_generator(
    train_datagen.flow(trainX,trainY, batch_size = batch_size),
    steps_per_epoch=len(trainX) // batch_size,
    epochs=epochs,
    validation_data=(testX,testY),
    validation_steps=len(testX) // batch_size)

model.save('flower.h5')