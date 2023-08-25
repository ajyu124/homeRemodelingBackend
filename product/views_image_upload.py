from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.http import HttpResponse
from django.conf import settings
import os

from .serializers import UploadedImageSerializer

class ImageUploadView(APIView):
    def post(self, request, format=None):
        serializer = UploadedImageSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def serve_uploaded_image(request, filename):
    image_path = os.path.join(settings.MEDIA_ROOT, 'uploads/product/', filename)
    with open(image_path, 'rb') as img_file:
        response = HttpResponse(img_file.read(), content_type='image/jpeg')  # Adjust content type based on image type
        return response
