from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APITestCase
from django.urls import reverse

class SignViewTestCase(APITestCase):
    def test_sign_view(self):
        with open('F:/shams/grad-project/django/main/sign/yolov5/1014_32_F_thaa_6.jpg', 'rb') as f:
            image_file = SimpleUploadedFile('image.jpg', f.read(), content_type='image/jpeg')
        url = reverse('sign')
        response = self.client.post(url, {'image': image_file}, format='multipart')
        self.assertEqual(response.status_code, 200)
        self.assertIn('output', response.data)