import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split

from numpy import *

from keras.layers import Activation, Convolution2D, MaxPooling2D, Flatten, ZeroPadding2D, Conv2D, AveragePooling2D, \
    GaussianDropout
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Flatten
from keras.optimizers import SGD
from tensorflow.keras import layers, models





num = str(380)
num_2 = str(500)
filedir = 'E:/training_' + num_2 + '/sectionA' + num + '/'
os.listdir(filedir)  # 返回指定路径下的文件和文件夹列表

file_list1 = []
fn_1 = []
for root, dirs, files in os.walk(filedir):
    for file in files:
        if os.path.splitext(file)[1] == ".png":  # 分割路径，返回路径名和文件扩展名的元组
            file_list1.append(os.path.join(root, file))
            fn_1.append(os.path.splitext(file)[0])

for filename in file_list1:
    try:
        im = Image.open(filename)
        new_im = im.resize((128, 128))  # 用于调整图像的大小
        new_im.save('E:/training_' + num_2 + '/sectionA' + num + '/j_128/' + fn_1[file_list1.index(filename)] + '.png')
        # print('图片'+fn_1[file_list1.index(filename)]+'.png'+'像素转换完成')
    except OSError as e:
        print(e.args)

filedir = 'E:/training_' + num_2 + '/sectionA' + num + '/j_128/'
os.listdir(filedir)

file_list_1 = []
for root, dirs, files in os.walk(filedir):
    for file in files:
        if os.path.splitext(file)[1] == ".png":
            file_list_1.append(os.path.join(root, file))

filedir = 'E:/training_' + num_2 + '/sectionB' + num + '/'
file_list2 = []
fn_2 = []
for root, dirs, files in os.walk(filedir):
    for file in files:
        if os.path.splitext(file)[1] == ".png":
            file_list2.append(os.path.join(root, file))
            fn_2.append(os.path.splitext(file)[0])

for filename in file_list2:
    try:
        im = Image.open(filename)
        new_im = im.resize((128, 128))
        new_im.save('E:/training_' + num_2 + '/sectionB' + num + '/f_128/' + fn_2[file_list2.index(filename)] + '.png')
        # print('图片'+fn_2[file_list2.index(filename)]+'.png'+'像素转换完成')
    except OSError as e:
        print(e.args)

filedir = 'E:/training_' + num_2 + '/sectionB' + num + '/f_128/'
os.listdir(filedir)

file_list_2 = []
for root, dirs, files in os.walk(filedir):
    for file in files:
        if os.path.splitext(file)[1] == ".png":
            file_list_2.append(os.path.join(root, file))

len(file_list_1)
len(file_list_2)
file_list_all = file_list_1 + file_list_2
len(file_list_all)

M = []
for filename in file_list_all:
    im = Image.open(filename)
    width, height = im.size
    im_L = im.convert("L")
    Core = im_L.getdata()
    arr1 = np.array(Core, dtype='float32') / 255.0
    arr1.shape
    list_img = arr1.tolist()
    M.extend(list_img)

X = np.array(M).reshape(len(file_list_all), width, height)
X.shape

class_names = ['crystal', 'Amorphous']

dict_label = {0: 'crystal', 1: 'Amorphous'}

label = [0] * len(file_list_1) + [1] * len(file_list_2)
y = np.array(label)

train_images, test_images, train_labels, test_labels = train_test_split(X, y, test_size=0.2, random_state=0, stratify=y)
train_images = train_images[..., tf.newaxis]
test_images = test_images[..., tf.newaxis]

model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), padding = "SAME", activation='relu', input_shape=(128, 128, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), padding = "SAME", activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), padding = "SAME", activation='relu'))
model.add(layers.Dropout(0.25))  # 2
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(2, activation='softmax'))
model.summary()
model.compile(optimizer=tf.optimizers.Adam(),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
history = model.fit(train_images, train_labels, epochs=10, validation_data=(test_images, test_labels))  # 相当于reshape特殊操作
test_loss, test_acc = model.evaluate(test_images, test_labels)

print(num + ':Test accuracy:', test_acc)

# 大批量
f = "final_consequence_" + num_2 + ".txt"
doc = open(f, 'a')
print(num_2 + ',' + num + ':', test_acc, ',', file=doc)
# print(history.epoch, file=doc)
# print("训练准确率", sep=':', file=doc)
# print(history.history['accuracy'], file=doc)
# print("验证准确率", sep=':', file=doc)
# print(history.history['val_accuracy'], file=doc)
doc.close()

# print(history.history.keys())
# %config InlineBackend.figure_format = 'retina'


#图片暂时隐去！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
# plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
# plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
# plt.title("Debye=" + num_2 + "，位置" + num + "处(400)", fontsize=20)
# plt.plot(history.epoch, history.history['accuracy'], label="训练准确率")
#
#
# plt.plot(history.epoch, history.history['val_accuracy'], label="验证准确率")
#
# plt.xlabel("迭代次数", fontsize=16)
# plt.ylabel("预测准确率", fontsize=16)
# plt.legend(fontsize=16)
# plt.show()
#


# 某一特定位置
# f = "consequence_" + num_2 + "_change" + num + ".txt"
# doc = open(f, 'a')
# print(num + ':', test_acc, ", ", file=doc)
# doc.close()



