from rest_framework import status

from rating_app.serializers import RatingSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def rating(request, pk):
    serializer = RatingSerializer(data=request.data, context={'request': request})
    serializer.is_valid(raise_exception=True)
    serializer.get_or_create_product_rating(pk)
    return Response(request.data, status=status.HTTP_201_CREATED)