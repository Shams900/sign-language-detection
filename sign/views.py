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



@parser_classes((MultiPartParser, ))
class SignView(APIView):
    def post(self, request):
        image = request.FILES.get('image')
        
        # load model
        
        # enter image to model
        
        # get predict image from the model
        my_image = ''
        
        my_model_image = models.SignImages.objects.create(image=image)
        
        
        data = {
            'output': request.build_absolute_uri(my_model_image.image.url),
        }
        return Response(data)


def project(request):
    image = None
    if request.method == 'POST':
        image = request.FILES.get('image')
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
        image = models.SignImages.objects.create(image=image)

    context = {
        'image': image,
        #'predicted_image_path': None
    }
    return render(request, 'sign/index.html', context)

    

