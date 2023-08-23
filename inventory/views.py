from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail
from .models import InventoryDetail, InventoryCategory
from .serializers import InventoryDetailSerializer, InventoryCategorySerializer

@api_view(['GET'])
def get_inventory_list(request):
    search_query = request.GET.get('search', '')
    query_set = InventoryDetail.objects.filter(
        Q(item__icontains=search_query) |  # Case-insensitive search for 'item'
        Q(quantity__icontains=search_query) |  # Case-insensitive search for 'quantity'
        Q(price_per_unit__icontains=search_query)  # Case-insensitive search for 'price_per_unit'
    ).order_by('-id')
    # query_set = InventoryDetail.objects.all().order_by('-id') # order by id in descending order

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
        price_per_unit = request.data.get('price_per_unit'),
        category_id = request.data.get('category'),
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
    existingItem.item = request.data.get("item")
    existingItem.quantity = request.data.get("quantity")
    existingItem.price_per_unit = request.data.get("price_per_unit")
    existingItem.category_id = request.data.get("category")
    existingItem.save()
    serializer = InventoryDetailSerializer(instance=existingItem)
    return Response(serializer.data) 


@api_view(['GET'])
def get_inventory_category_list(request):
    query_set = InventoryCategory.objects.all()
    serializer = InventoryCategorySerializer(query_set, many=True)
    return Response(serializer.data)