from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ShippingDetail
from .serializers import ShippingDetailSerializer

@api_view(['GET'])
def get_shipping_list(request):
    query_set = ShippingDetail.objects.all()
    serializer = ShippingDetailSerializer(query_set, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_shipping_detail(request, shipping_id):
    single_shipping = ShippingDetail.objects.get(id=shipping_id)
    serializer = ShippingDetailSerializer(single_shipping)
    return Response(serializer.data)

@api_view(['POST'])
def create_shipping(request):
    newItem = ShippingDetail.objects.create(
        street_address = request.data.get('street_address'),
        city = request.data.get('city'),
        state = request.data.get('state'),
        zipcode = request.data.get('zipcode'),
        customer_name = request.data.get('customer_name'),
        customer_email = request.data.get('customer_email'),
        product_detail_id = request.data.get('product_detail'),
    )
    serializer = ShippingDetailSerializer(instance=newItem)
    return Response(serializer.data, status=201) 

@api_view(['DELETE'])
def delete_shipping(request, shipping_id):
    item = ShippingDetail.objects.get(id=shipping_id)
    item.delete()
    return Response(status=204)

@api_view(['PUT'])
def update_shipping(request, shipping_id):
    existingItem = ShippingDetail.objects.get(id=shipping_id)
    existingItem.name = request.data.get("name")
    # existingItem.description = request.data.get("description")
    existingItem.image_name = request.data.get("image_name")
    existingItem.save()
    serializer = ShippingDetailSerializer(instance=existingItem)
    return Response(serializer.data) 

