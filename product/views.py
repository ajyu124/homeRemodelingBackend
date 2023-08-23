from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ProductDetail
from .serializers import ProductDetailSerializer

@api_view(['GET'])
def get_product_list(request):
    search_query = request.GET.get('search', '')
    query_set = ProductDetail.objects.filter(
        Q(name__icontains=search_query)  # Case-insensitive search for 'name'
    ).order_by('-id')
    # query_set = ProductDetail.objects.all().order_by('-id') # order by id in descending order

    serializer = ProductDetailSerializer(query_set, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_product_detail(request, product_id):
    single_product = ProductDetail.objects.get(id=product_id)
    serializer = ProductDetailSerializer(single_product)
    return Response(serializer.data)

@api_view(['POST'])
def create_product(request):
    newItem = ProductDetail.objects.create(
        name = request.data.get('name'),
        image_name = request.data.get('image_name'),
    )
    serializer = ProductDetailSerializer(instance=newItem)
    return Response(serializer.data, status=201) 

@api_view(['DELETE'])
def delete_product(request, product_id):
    item = ProductDetail.objects.get(id=product_id)
    item.delete()
    return Response(status=204)

@api_view(['PUT'])
def update_product(request, product_id):
    existingItem = ProductDetail.objects.get(id=product_id)
    existingItem.name = request.data.get("name")
    # existingItem.image_name = request.data.get("image_name")
    existingItem.save()
    serializer = ProductDetailSerializer(instance=existingItem)
    return Response(serializer.data) 
