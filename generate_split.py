import os
from random import Random
from shutil import copy2
from tqdm import tqdm

img_list = []
FROM_DIR = 'kaggle_train/'
TO_DIR_TRAIN = 'train/'
TO_DIR_TEST = 'test/'

for img in os.listdir(FROM_DIR):
    img_list.append(img)

Random(1).shuffle(img_list)

train_images = os.listdir(TO_DIR_TRAIN)
test_images = os.listdir(TO_DIR_TEST)

for img in tqdm(img_list[:20000]):
    if img not in train_images:
        copy2(FROM_DIR+img, TO_DIR_TRAIN)

for img in tqdm(img_list[20000:]):
    if img not in test_images:
        copy2(FROM_DIR+img, TO_DIR_TEST)