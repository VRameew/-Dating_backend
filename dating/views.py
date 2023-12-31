from dating.validator import CustomUserValidator
from rest_framework.response import Response
from rest_framework.decorators import api_view
from dating.watermarker import watermark_text
from django.shortcuts import get_object_or_404
from dating.models import CustomUser, Match
from dating.emailsender import email_sender
from dating.DistanceBetweenPoints import getDistanceBetweenPointsNew


# Create your views here.
@api_view(['POST'])
def create_client(request):
    validator = CustomUserValidator(data=request.data)
    if validator.is_valid():
        user = validator.save()
        watermark_text(user.avatar, f'avatars/{user.id}',
                       text='DATING_API', pos=(0, 0))
        return Response(validator.data)
    return Response(validator.errors, status=400)


@api_view(['POST'])
def match_client(request, id):
    client = get_object_or_404(CustomUser, id=id)
    liked_client_id = request.data.get('liked_client_id')
    liked_client = get_object_or_404(CustomUser, id=liked_client_id)
    match = Match.objects.create(client=client, liked_client=liked_client)
    if Match.objects.filter(client=liked_client, liked_client=client).exists():
        email_sender(liked_client.email, f'Вы понравились {client.first_name}! Почта участника: {client.email}')
        match.email_sent = True
        match.save()
        return Response({'message': f'Вы понравились {liked_client.first_name}! Почта участника: {liked_client.email}'})
    return Response(status=204)


@api_view(['GET'])
def client_list(request):
    queryset = CustomUser.objects.all()
    gender = request.query_params.get('gender')
    name = request.query_params.get('name')
    surname = request.query_params.get('surname')
    if gender:
        queryset = queryset.filter(gender=gender)
    if name:
        queryset = queryset.filter(first_name__icontains=name)
    if surname:
        queryset = queryset.filter(last_name__icontains=surname)
    serializer = CustomUserValidator(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def nearby_clients(request, id, distance):
    client = get_object_or_404(CustomUser, id=id)
    longitude_client = client.longitude
    latitude_client = client.latitude
    nearby_users = []
    for user in CustomUser.objects.all():
        distance_to_user = getDistanceBetweenPointsNew(
            latitude_client, longitude_client, user.latitude, user.longitude)
        if distance <= distance_to_user:
            nearby_users.append(user)
    return Response(nearby_users)
