from rest_framework.decorators import action
from rest_framework.response import Response
from rating_app.models import Rating
from rating_app.serializers import RatingSerializer


@action(methods=['POST'], detail=True)
def rating(self, request, pk, *args, **kwargs):
    serializers = RatingSerializer(data=request.data)
    serializers.is_valid(raise_exception=True)
    obj, _ = Rating.objects.get_or_create(product_id=pk,
                                          owner=request.user)
    obj.rating = request.data['rating']
    obj.save()
    return Response(request.data, status=201)