from rest_framework import serializers
from ads.models import Ad, Category, Selection


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class AdSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field="first_name")
    category = serializers.SlugRelatedField(read_only=True,
                                            slug_field="name")

    class Meta:
        model = Ad
        fields = "__all__"


class AdCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ["name", "author", "price", "description", "category", "is_published", "image"]


class AdDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ["id"]


class SelectionListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Selection
        fields = ["id", "name"]


class SelectionDetailSerializer(serializers.ModelSerializer):
    items = AdSerializer(many=True)
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field="first_name")

    class Meta:
        model = Selection
        fields = "__all__"


class SelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = "__all__"


class SelectionDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = ["id"]