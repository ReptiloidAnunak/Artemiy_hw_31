from django.core.validators import ValidationError
from rest_framework import serializers
from authentication.models import User, Location
from Avito30.settings import EMAIL_DOMAINS_NOT_ALLOWED


class EmailValidator:
    def __call__(self, email):
        not_allowed = EMAIL_DOMAINS_NOT_ALLOWED
        if email.split("@")[1] in not_allowed:
            raise ValidationError(f"Addresses of domains {','.join(not_allowed)} are not allowed")
        return True


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(many=True, read_only=True, slug_field="name")

    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "birth_date", "email", "role", "location"]


class UserCreateSerializer(serializers.ModelSerializer):

    id = max(user.id for user in User.objects.all()) + 1
    email = serializers.EmailField(validators=[EmailValidator()])
    location = serializers.SlugRelatedField(
        required=False,
        queryset=Location.objects.all(),
        many=True,
        read_only=False,
        slug_field="name"
    )

    def is_valid(self, raise_exception=False):
        self._location = self.initial_data.pop("location")
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)

        user.set_password(validated_data["password"])
        user.save()
        for loc in self._location:
            obj, _ = Location.objects.get_or_create(name=loc)
            user.location.add(obj)

        return user

    class Meta:
        model = User
        exclude = ["role", "last_login", "is_superuser", "is_staff", "date_joined", "is_active",
                   "user_permissions", "groups"]


class UserUpdateSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        queryset=Location.objects.all(),
        many=True,
        slug_field="name"
    )

    def is_valid(self, raise_exception=False):
        self._location = self.initial_data.pop("location")
        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        user = super().save()

        for loc in self._location:
            obj, _ = Location.objects.get_or_create(name=loc)
            user.location.add(obj)

        return user

    class Meta:
        model = User
        exclude = ["id", "role", "last_login", "is_superuser", "is_staff", "date_joined", "is_active", "user_permissions", "groups"]


class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id"]
