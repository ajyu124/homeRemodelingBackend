from rest_framework import serializers
from .models import MyEmailDetail

class MyEmailDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = MyEmailDetail
		fields = '__all__'