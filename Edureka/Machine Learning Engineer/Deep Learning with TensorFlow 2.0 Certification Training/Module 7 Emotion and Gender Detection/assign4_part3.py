# -*- coding: utf-8 -*-
"""Assign4_Part3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1s6UAfUyylir_sg2o4GhkyJljNbouYhkL
"""

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Activation, MaxPool2D, Dropout, Flatten
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import matplotlib.image as mimg
import pandas as pd
from tensorflow.keras.preprocessing.image import ImageDataGenerator

!tar -xvf /content/UTKFace.tar.gz
!tar -xvf /content/crop_part1.tar.gz

!mv /content/UTKFace/* /content/data
!mv /content/crop_part1/* /content/data

contentdata = []

import os
for i in os.listdir("data"):
  content = i.split("_")
  if ((content[0].isnumeric()) and (content[1].isnumeric()) and (content[2].isnumeric())):
      contentdata.append([content[0],content[1],content[2],os.path.join("data",i)])
  #print(content[2])
  #imgarray = plt.imread(os.path.join("data",i))

data = pd.DataFrame(contentdata,columns=["Age","Gender","Racevalues","Filepath"])

data.head(10)

data.dtypes

data = []

data.dtypes

data["Gender"] = data['Gender'].map({'0':'Male','1':'Female'})
data["Racevalues"] = data['Racevalues'].map({'0':"White",'1':"Black",'2':"Asian",'3':"Indian",'4':"Others"})

data.head(10)

data.Age = data.Age.astype('float')
data.Gender = data.Gender.astype('float')
data['Racevalues'] = data['Racevalues'].astype('float')
data.Filepath = data.Filepath.astype('string')

data.dtypes

train, test = train_test_split(data, test_size=0.1)

testdatagenerator = ImageDataGenerator(rescale=1. /255)
testdata = testdatagenerator.flow_from_dataframe(dataframe=test,directory=None,x_col="Filepath",y_col=["Age","Gender","Racevalues"],class_mode="raw")

traindatagenerator = ImageDataGenerator(rescale=1. /255,shear_range =0.2,zoom_range=0.2,horizontal_flip =True)
traindata = traindatagenerator.flow_from_dataframe(dataframe=train,directory=None,x_col="Filepath",y_col=["Age","Gender","Racevalues"],class_mode="raw")

#model = []

model = Sequential()

model.add(Conv2D(32, (3, 3), padding='same',
                 input_shape=(100,100,3)))
model.add(Activation('relu'))
model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPool2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Conv2D(64, (3, 3), padding='same'))
model.add(Activation('relu'))
model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPool2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(5, activation='sigmoid'))

model.compile(optimizer="Adam",loss="binary_crossentropy",metrics=["accuracy"])

model.fit(traindata,
                   steps_per_epoch=100,epochs=100,
                   validation_data=testdata,
                       validation_steps=100,batch_size=20)