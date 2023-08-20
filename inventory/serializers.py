from rest_framework import serializers
from .models import InventoryDetail

class InventoryDetailSerializer(serializers.ModelSerializer):

	class Meta:
		model = InventoryDetail
		fields = '__all__'