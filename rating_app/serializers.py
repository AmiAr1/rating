from rest_framework import serializers
from rating_app.models import Rating, Product


class RatingSerializer(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    rating = serializers.IntegerField(required=True, min_value=1, max_value=5)

    def get_or_create_product_rating(self, product_id: int):
        # для работоспособности
        obj, _ = Rating.objects.get_or_create(product=Product.objects.get(pk=product_id),
                                              user=self.get('user'))
        # для тестов
        # obj, _ = Rating.objects.get_or_create(product=Product.objects.first(),
        #                                       user=User.objects.first())
        obj.rating = self.data.get('rating', 1)
        obj.save()