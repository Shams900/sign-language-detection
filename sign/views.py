from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
import torchvision.transforms as transforms
from rest_framework.views import APIView
from django.shortcuts import render
from PIL import Image
from . import models
import numpy as np
import subprocess
import torch
import time
import cv2
import os
from base64 import b64encode
import io
from django.db import models as modelz
from django.utils.translation import gettext_lazy as _
from PIL import Image

cwd = os.getcwd()

print("E7naa ahena" , cwd)
model = torch.hub.load( "sign/yolov5",'custom' , source='local' , path="F:/shams/grad-project/django/main/sign/yolov5/best.pt", force_reload=True)
@parser_classes((MultiPartParser, ))
class SignView(APIView):
    def post(self, request):
        image = request.FILES.get('image')
        
        # load model
        
        # enter image to model
        
        # get predict image from the model
        my_image = ''
        
        my_model_image = models.SignImages.objects.create(image=image)
        
        image = Image.open(io.BytesIO(img.read()))

        print("THE IMAGE" , img)
        output = model(image)
        r_img = output.render() # returns a list with the images as np.array
        img_with_boxes = r_img[0]
        theImage = Image.fromarray(img_with_boxes)
        # output = Image.open(io.BytesIO(theImage.read()))
        buffered = io.BytesIO()
        theImage.save(buffered, format="JPEG")
        bezo = b64encode(buffered.getvalue()).decode("utf-8")
        data_url = 'data:image/jpeg;base64,'+bezo
        data = {
            # 'output': request.build_absolute_uri(my_model_image.image.url),
            output : data_url
        }
        return Response(data)


def project(request):
    image = None
    context = {
        'image': "",
    }
    if request.method == 'POST':
        img = request.FILES.get('image')
        if img is not None:
            """# Save the uploaded image to the database
            image_obj = models.SignImages.objects.create(image=image)
            # Get the path to the saved image
            image_path = str(image_obj.image.path)
            # Build the command to run the detect.py script
            command = f'cd yolov5 python detect.py --weights best.pt --img 640 --conf 0.25 --source "{image_path}"'
            # Run the command as a subprocess and capture its output
            output = subprocess.check_output(command, shell=True, universal_newlines=True)
            # Extract the path to the predicted image from the output
            print(output)
            predicted_image_path = os.path.join(os.getcwd(), output.split()[-1])
            print(predicted_image_path)
            # Set the predicted image path in the context
            context = {
                'image': image_obj,
                'predicted_image_path': predicted_image_path
            }
            return render(request, 'sign/index.html', context)"""
            # image = models.SignImages.objects.create(image=image)
            # img_np = np.fromstring(image.read(), np.uint8)
            # img = cv2.imdecode(img_np, cv2.IMREAD_COLOR)
            # img = cv2.resize(img, (640, 640))
            # img = torch.from_numpy(img).permute(2, 0, 1).float().div(255.0).unsqueeze(0)
            # output = model(img)
            # output = output.squeeze(0)
            # output = output.unsqueeze(0)  # Add two new dimensions
            # output = output.unsqueeze(-1)
            # output = output.permute(0, 2, 3, 1).detach().cpu().numpy() * 255.0
            # output = output.astype(np.uint8)
            # output = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
            # output = Image.fromarray(output)

            # Convert the PIL image to a data URL image
            # buffer = io.BytesIO()
            # output.save(buffer, format='JPEG')
            # img_instance =  models.SignImages.objects.create(image=img)

            # uploaded_img_qs = ImageModel.objects.filter().last()
            # img_bytes = img_instance.image.read()
            # img = img.open(io.BytesIO(img_bytes))
            image = Image.open(io.BytesIO(img.read()))

            print("THE IMAGE" , img)
            output = model(image)
            r_img = output.render() # returns a list with the images as np.array
            img_with_boxes = r_img[0]
            theImage = Image.fromarray(img_with_boxes)
            # output = Image.open(io.BytesIO(theImage.read()))
            buffered = io.BytesIO()
            theImage.save(buffered, format="JPEG")
            bezo = b64encode(buffered.getvalue()).decode("utf-8")
            data_url = 'data:image/jpeg;base64,'+bezo
            context = {
                'image': data_url,
                #'predicted_image_path': None
            }
    return render(request, 'sign/index.html', context)

    

