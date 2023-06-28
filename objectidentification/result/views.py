from django.shortcuts import render, redirect
from django.urls import reverse
import os
import random, string
from objectidentification.forms import ImageUploadForm

import tensorflow as tf
import numpy as np



def handle_uploaded_file(f, file_name):
    with open(file_name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

# Create your views here.
def result(request):
    file_name = None
    print("result: Processing request")
    form = ImageUploadForm(request.POST, request.FILES)

    if form.is_valid():
        print("Form is valid")
        image_path = "images/"
        os.makedirs(image_path) if not os.path.exists(image_path) else print("Images directory exists")
        random_name = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(20))
        file_name = random_name+'.png'
        image_path = f'{image_path}{file_name}'

        handle_uploaded_file(request.FILES['image'], image_path)

        model = tf.keras.applications.ResNet50V2(weights="imagenet")

        img = tf.keras.preprocessing.image.load_img(image_path, target_size=(224, 224))
        x = tf.keras.preprocessing.image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = tf.keras.applications.resnet_v2.preprocess_input(x)

        preds = model.predict(x)
        result = tf.keras.applications.resnet_v2.decode_predictions(preds, top=3)[0]
        print(result)
        res = []
        for x, label, percentage in result:
            res.append((label,round(int(percentage*10000)/10000, 4)))
        return render(request, "result.html", {"res":res})
    else:
        return redirect(reverse('index_redirect'))
    

def redirect_to_index_page(request):
    return render(request, "index.html")