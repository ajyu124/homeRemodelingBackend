from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail
from .models import InventoryDetail
from .serializers import InventoryDetailSerializer

@api_view(['GET'])
def get_inventory_list(request):
    query_set = InventoryDetail.objects.all()
    serializer = InventoryDetailSerializer(query_set, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_inventory_detail(request, inventory_id):
    single_inventory = InventoryDetail.objects.get(id=inventory_id)
    serializer = InventoryDetailSerializer(single_inventory)
    return Response(serializer.data)

@api_view(['POST'])
def create_inventory(request):
    newItem = InventoryDetail.objects.create(
        item = request.data.get('item'),
        quantity = request.data.get('quantity'),
    )
    serializer = InventoryDetailSerializer(instance=newItem)
    return Response(serializer.data, status=201) 

@api_view(['DELETE'])
def delete_inventory(request, inventory_id):
    item = InventoryDetail.objects.get(id=inventory_id)
    item.delete()
    return Response(status=204)

@api_view(['PUT'])
def update_inventory(request, inventory_id):
    existingItem = InventoryDetail.objects.get(id=inventory_id)
    existingItem.name = request.data.get("name")
    existingItem.image_name = request.data.get("image_name")
    existingItem.save()
    serializer = InventoryDetailSerializer(instance=existingItem)
    return Response(serializer.data) 
