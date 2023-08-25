from rest_framework import serializers
from .models import ProductDetail, UploadedImage

class ProductDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = ProductDetail
		fields = '__all__'

class UploadedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedImage
        fields = '__all__'
