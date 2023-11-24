# -*- coding: utf-8 -*-
"""ANN - Part 6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VRblxiFjAmakbF58-m8kZ7pNWqZbtj4v
"""

import os
import numpy as np
import tensorflow as tf
import skimage.io
from skimage.io import imread
from skimage.util import random_noise
from sklearn.model_selection import train_test_split

# Specify the directory for the non-noisy images
non_noisy_directory = "/content/drive/MyDrive/ANN/images/train"

# Specify the directory for saving the noisy images
noisy_directory = "/content/drive/MyDrive/ANN/images/noisy"

# Specify the type and parameters of the noise
noise_type = 'gaussian'
variance = 0.01

# Iterate over the files in the non-noisy directory
for filename in os.listdir(non_noisy_directory):
    # Check if the file name matches the desired pattern
    if filename.endswith('.jpg'):
        file_path_non_noisy = os.path.join(non_noisy_directory, filename)
        # Read the non-noisy image
        non_noisy_image = imread(file_path_non_noisy)
        # Generate the noisy image
        noisy_image = random_noise(non_noisy_image, mode=noise_type, var=variance)
        # Save the noisy image
        noisy_filename = 'noisy_' + filename
        noisy_file_path = os.path.join(noisy_directory, noisy_filename)
        skimage.io.imsave(noisy_file_path, (noisy_image * 255).astype(np.uint8))

# Initialize empty lists for noisy images and non-noisy images
noisy_images = []
non_noisy_images = []

# Iterate over the files in the noisy directory
for noisy_filename in os.listdir(noisy_directory):
    # Check if the file name matches the desired pattern
    if noisy_filename.startswith('noisy_'):
        # Extract the common identifier from the noisy file name
        common_identifier = noisy_filename.split('noisy_')[1]
        # Construct the corresponding non-noisy file name
        non_noisy_filename = common_identifier
        # Construct the file paths for the noisy and non-noisy images
        file_path_noisy = os.path.join(noisy_directory, noisy_filename)
        file_path_non_noisy = os.path.join(non_noisy_directory, non_noisy_filename)
        # Read the noisy image
        noisy_image = imread(file_path_noisy)
        # Read the corresponding non-noisy image
        non_noisy_image = imread(file_path_non_noisy)
        # Append the images to the respective lists
        noisy_images.append(noisy_image)
        non_noisy_images.append(non_noisy_image)

# Convert the lists to numpy arrays
noisy_images = np.array(noisy_images)
non_noisy_images = np.array(non_noisy_images)

# Normalize the pixel values to the range [0, 1]
noisy_images = noisy_images / 255.0
non_noisy_images = non_noisy_images / 255.0

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(noisy_images, non_noisy_images, test_size=0.2)

# Define the architecture of the denoising ANN
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=(32, 32, 3)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(3, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='mse')

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

# Generate denoised images
denoised_images = model.predict(noisy_images)