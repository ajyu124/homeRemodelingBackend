from rest_framework import serializers
from .models import ShippingDetail

class ShippingDetailSerializer(serializers.ModelSerializer):
	product_detail_name = serializers.SerializerMethodField()

	def get_product_detail_name(self, obj):
			if obj.product_detail:
					return obj.product_detail.name
			return None

	class Meta:
		model = ShippingDetail
		fields = '__all__'