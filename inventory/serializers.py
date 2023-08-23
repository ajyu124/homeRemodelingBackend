from rest_framework import serializers
from .models import InventoryDetail, InventoryCategory

class InventoryDetailSerializer(serializers.ModelSerializer):
	category_description = serializers.SerializerMethodField()

	def get_category_description(self, obj):
	  if obj.category:
		  return obj.category.description
	  return None

	class Meta:
		model = InventoryDetail
		fields = '__all__'

class InventoryCategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = InventoryCategory
		fields = '__all__'