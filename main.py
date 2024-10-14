import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Set font for displaying Chinese characters and handling minus signs in plots
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
from keras.layers import Conv2D, MaxPooling2D, Dense, Dropout, Flatten
from keras.models import Sequential
from tensorflow.keras import layers, models

# Variables for the directory paths
num = str(380)
num_2 = str(500)
filedir = 'E:/training_' + num_2 + '/sectionA' + num + '/'

# List all files in the directory
os.listdir(filedir)

# Initialize lists for file paths and filenames
file_list1 = []
fn_1 = []

# Traverse the directory and find all PNG files
for root, dirs, files in os.walk(filedir):
    for file in files:
        if os.path.splitext(file)[1] == ".png":  # Check if the file is a PNG image
            file_list1.append(os.path.join(root, file))
            fn_1.append(os.path.splitext(file)[0])

# Resize images and save them to a new directory
for filename in file_list1:
    try:
        im = Image.open(filename)
        new_im = im.resize((128, 128))  # Resize the image to 128x128 pixels
        new_im.save('E:/training_' + num_2 + '/sectionA' + num + '/j_128/' + fn_1[file_list1.index(filename)] + '.png')
    except OSError as e:
        print(e.args)

# Load images after resizing
filedir = 'E:/training_' + num_2 + '/sectionA' + num + '/j_128/'
os.listdir(filedir)

# Initialize list for resized images
file_list_1 = []
for root, dirs, files in os.walk(filedir):
    for file in files:
        if os.path.splitext(file)[1] == ".png":
            file_list_1.append(os.path.join(root, file))

# Repeat the process for section B
filedir = 'E:/training_' + num_2 + '/sectionB' + num + '/'
file_list2 = []
fn_2 = []
for root, dirs, files in os.walk(filedir):
    for file in files:
        if os.path.splitext(file)[1] == ".png":
            file_list2.append(os.path.join(root, file))
            fn_2.append(os.path.splitext(file)[0])

# Resize images and save to section B directory
for filename in file_list2:
    try:
        im = Image.open(filename)
        new_im = im.resize((128, 128))
        new_im.save('E:/training_' + num_2 + '/sectionB' + num + '/f_128/' + fn_2[file_list2.index(filename)] + '.png')
    except OSError as e:
        print(e.args)

# Load images from section B after resizing
filedir = 'E:/training_' + num_2 + '/sectionB' + num + '/f_128/'
os.listdir(filedir)

file_list_2 = []
for root, dirs, files in os.walk(filedir):
    for file in files:
        if os.path.splitext(file)[1] == ".png":
            file_list_2.append(os.path.join(root, file))

# Combine file lists from section A and section B
file_list_all = file_list_1 + file_list_2
len(file_list_all)

# Prepare image data for model input
M = []
for filename in file_list_all:
    im = Image.open(filename)
    width, height = im.size
    im_L = im.convert("L")  # Convert the image to grayscale
    Core = im_L.getdata()
    arr1 = np.array(Core, dtype='float32') / 255.0  # Normalize pixel values
    M.extend(arr1.tolist())

# Reshape the image data
X = np.array(M).reshape(len(file_list_all), width, height)
X.shape

# Class names and label mapping
class_names = ['crystal', 'Amorphous']
dict_label = {0: 'crystal', 1: 'Amorphous'}

# Label assignment for section A and B
label = [0] * len(file_list_1) + [1] * len(file_list_2)
y = np.array(label)

# Split the data into training and testing sets
train_images, test_images, train_labels, test_labels = train_test_split(X, y, test_size=0.2, random_state=0, stratify=y)
train_images = train_images[..., tf.newaxis]  # Add channel dimension for TensorFlow input
test_images = test_images[..., tf.newaxis]

# Build a CNN model
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), padding="SAME", activation='relu', input_shape=(128, 128, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), padding="SAME", activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), padding="SAME", activation='relu'))
model.add(layers.Dropout(0.25))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(2, activation='softmax'))

# Display model summary
model.summary()

# Compile the model
model.compile(optimizer=tf.optimizers.Adam(),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
history = model.fit(train_images, train_labels, epochs=10, validation_data=(test_images, test_labels))

# Evaluate the model
test_loss, test_acc = model.evaluate(test_images, test_labels)
print(num + ': Test accuracy:', test_acc)

# Log test accuracy to a file
f = "final_consequence_" + num_2 + ".txt"
with open(f, 'a') as doc:
    print(num_2 + ',' + num + ':', test_acc, ',', file=doc)

# Plotting code (commented out for now)
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False
# plt.title("Debye=" + num_2 + "，位置" + num + "处(400)", fontsize=20)
# plt.plot(history.epoch, history.history['accuracy'], label="Training Accuracy")
# plt.plot(history.epoch, history.history['val_accuracy'], label="Validation Accuracy")
# plt.xlabel("Epochs", fontsize=16)
# plt.ylabel("Accuracy", fontsize=16)
# plt.legend(fontsize=16)
# plt.show()

# Log test accuracy for specific locations (commented out)
# f = "consequence_" + num_2 + "_change" + num + ".txt"
# with open(f, 'a') as doc:
#     print(num + ':', test_acc, ", ", file=doc)
