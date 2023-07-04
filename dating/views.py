from dating.validator import CustomUserValidator
from rest_framework.response import Response
from rest_framework.decorators import api_view
from dating.watermarker import watermark_text


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
