from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ShippingDetail
from .serializers import ShippingDetailSerializer

@api_view(['GET'])
def get_shipping_list(request):
    search_query = request.GET.get('search', '')
    query_set = ShippingDetail.objects.filter(
        Q(street_address__icontains=search_query) |
        Q(city__icontains=search_query) |
        Q(state__icontains=search_query) |
        Q(zipcode__icontains=search_query) |
        Q(customer_name__icontains=search_query) |
        Q(customer_email__icontains=search_query)
    ).order_by('-id')
    # query_set = ShippingDetail.objects.all().order_by('-id') # order by id in descending order
    
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

    existingItem.product_detail_id = request.data.get('product_detail')
    existingItem.street_address = request.data.get('street_address')
    existingItem.city = request.data.get('city')
    existingItem.state = request.data.get('state')
    existingItem.zipcode = request.data.get('zipcode')
    existingItem.customer_name = request.data.get('customer_name')
    existingItem.customer_email = request.data.get('customer_email')

    existingItem.save()
    serializer = ShippingDetailSerializer(instance=existingItem)
    return Response(serializer.data) 

