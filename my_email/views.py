from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail
from .models import MyEmailDetail
from .serializers import MyEmailDetailSerializer

@api_view(['GET'])
def get_my_email_list(request):
    query_set = MyEmailDetail.objects.all()
    serializer = MyEmailDetailSerializer(query_set, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_my_email_detail(request, my_email_id):
    single_my_email = MyEmailDetail.objects.get(id=my_email_id)
    serializer = MyEmailDetailSerializer(single_my_email)
    return Response(serializer.data)

@api_view(['POST'])
def create_my_email(request):
    newItem = MyEmailDetail.objects.create(
        recipient = request.data.get('recipient'),
        subject = request.data.get('subject'),
        body = request.data.get('body'),
    )
    serializer = MyEmailDetailSerializer(instance=newItem)

    # send email via SMTP server
    subject = newItem.subject
    message = newItem.body
    from_email = 'burlingame_home_remodelling@gmail.com'
    recipient_list = [newItem.recipient]
    send_mail(subject, message, from_email, recipient_list)

    return Response(serializer.data, status=201) 

@api_view(['DELETE'])
def delete_my_email(request, my_email_id):
    item = MyEmailDetail.objects.get(id=my_email_id)
    item.delete()
    return Response(status=204)

@api_view(['PUT'])
def update_my_email(request, my_email_id):
    existingItem = MyEmailDetail.objects.get(id=my_email_id)
    existingItem.name = request.data.get("name")
    existingItem.image_name = request.data.get("image_name")
    existingItem.save()
    serializer = MyEmailDetailSerializer(instance=existingItem)
    return Response(serializer.data) 
