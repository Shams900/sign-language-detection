from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
import torchvision.transforms as transforms
from rest_framework.views import APIView
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from base64 import b64encode
from PIL import Image
from . import models
import numpy as np
import subprocess
import torch
import os
import io


cwd = os.getcwd()
# print("E7naa ahena" , cwd)
model = torch.hub.load( "sign/yolov5", 'custom', source='local', path=cwd + "/sign/yolov5/best.pt", force_reload=True)

@parser_classes((MultiPartParser, ))

class SignView(APIView):
    def post(self, request):
        img = request.FILES.get('image')
        print('img:', img)
        print('request.FILES:', request.FILES)
        if img is None:
            return Response({'error': 'Image field is missing'}, status=status.HTTP_400_BAD_REQUEST)
        else:
        
            image = Image.open(io.BytesIO(img.read()))

            #print("THE IMAGE" , img)
            output = model(image)
            r_img = output.render() # returns a list with the images as np.array
            img_with_boxes = r_img[0]
            theImage = Image.fromarray(img_with_boxes)
            
            buffered = io.BytesIO()
            theImage.save(buffered, format="JPEG")
            #bezo = b64encode(buffered.getvalue()).decode("utf-8")
            #data_url = 'data:image/jpeg;base64,'+bezo
            image_data = buffered.getvalue()
            response = HttpResponse(image_data, content_type='image/jpeg')
            #my_model_image = models.SignImages.objects.create(image=data_url)
            """data = {
                #'output': request.build_absolute_uri(data_url),
                'output' : data_url
            }"""
            response['Content-Disposition'] = 'attachment; filename=output.jpg'
            return response


def project(request):
    image = None
    context = {
        'image': "",
    }
    if request.method == 'POST':
        img = request.FILES.get('image')
        if img is not None:
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

    

