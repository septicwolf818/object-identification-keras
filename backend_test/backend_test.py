import tensorflow as tf
import numpy as np
import math

model = tf.keras.applications.ResNet50V2(weights="imagenet")

image_path = './toy_poodle.png'
img  = tf.keras.preprocessing.image.load_img(image_path, target_size=(224, 224))
x = tf.keras.preprocessing.image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = tf.keras.applications.resnet_v2.preprocess_input(x)

preds = model.predict(x)
result = tf.keras.applications.resnet_v2.decode_predictions(preds, top=3)[0]
for x, label, percentage in result:
    print(f"[{x}] \"{label}\": {round(int(percentage*10000)/10000, 4)}%")