import json
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from django.http import JsonResponse, Http404
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView, CreateView,\
    UpdateView, DeleteView
from django.views.decorators.csrf import csrf_exempt

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView,\
    UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from ads.models import Ad, Category, Selection
from ads.serializers import AdSerializer, AdCreateSerializer, AdDeleteSerializer, SelectionListSerializer, SelectionDetailSerializer,\
    SelectionSerializer, SelectionDeleteSerializer
from authentication.models import User
from ads.permissions import AdChangePermission, SelectionChangePermission


def index(request):
    return JsonResponse({"status": "ok"})


class AdsListView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        category_id = request.GET.getlist("cat", None)

        if category_id:
            self.queryset = self.queryset.filter(category_id__in=category_id)

        if request.GET.getlist("text", None):
            self.queryset = self.queryset.filter(name__icontains=request.GET.get("text"))

        if request.GET.getlist("location", None):
            self.queryset = self.queryset.filter(author__location__name__icontains=request.GET.get("location"))

        if request.GET.getlist("price_from", None):
            self.queryset = self.queryset.filter(price__gte=request.GET.get("price_from"))

        if request.GET.getlist("price_to", None):
            self.queryset = self.queryset.filter(price__lte=request.GET.get("price_to"))

        return super().get(request, *args, **kwargs)


class AdsDetailView(RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated]


@method_decorator(csrf_exempt, name='dispatch')
class AdCreateView(CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdCreateSerializer


@api_view(["PUT", "PATCH"])
@permission_classes([IsAuthenticated, AdChangePermission])
def ad_update_view(request, pk):
    ad_data = json.loads(request.body)
    try:
        ad = Ad.objects.get(pk=pk)
    except Ad.DoesNotExist:
        raise Http404("Объявления не существует")

    ad.name = ad_data["name"]
    ad.price = ad_data["price"]
    ad.description = ad_data["description"]
    ad.category_id = ad_data["category"]

    ad.save()
    return JsonResponse({
        "id": ad.id,
        "name": ad.name,
        "author_id": ad.author_id,
        "author": ad.author.first_name,
        "price": ad.price,
        "description": ad.description,
        "is_published": ad.is_published,
        "category_id": ad.category_id,
    })


@method_decorator(csrf_exempt, name="dispatch")
class AdDelete(DestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDeleteSerializer
    permission_classes = [IsAuthenticated, AdChangePermission]

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class CategoriesView(ListView):
    model = Category
    fields = ["id", "name"]

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        result = []
        for category in self.object_list:
            result.append(
                {"id": category.id,
                "name": category.name})

        return JsonResponse(result, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        try:
            category = self.get_object()
        except Ad.DoesNotExist:
            return JsonResponse({"error": "Not found"}, status=404)
        return JsonResponse({
              "id": category.id,
              "name": category.name})


@method_decorator(csrf_exempt, name='dispatch')
class CategoryCreateView(CreateView):
    model = Category
    fields = ["id", "name"]

    def post(self, request, *args, **kwargs):
        cat_data = json.loads(request.body)

        cat = Category.objects.create(name=cat_data["name"])
        return JsonResponse({"id": cat.id,
                             "name": cat.name})


@method_decorator(csrf_exempt, name='dispatch')
class CategoryUpdate(UpdateView):
    model = Category
    fields = ["id", "name"]

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        cat_data = json.loads(request.body)
        self.object.name = cat_data["name"]

        try:
            self.object.full_clean()
        except ValidationError as e:
            return JsonResponse(e.message_dict, status=422)

        self.object.save()
        return JsonResponse({"id": self.object.id,
                             "name": self.object.name})


@method_decorator(csrf_exempt, name="dispatch")
class CategoryDelete(DeleteView):
    model = Category
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=200)


class SelectionsViewList(ListAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionListSerializer


class SelectionDetailView(RetrieveAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionDetailSerializer


class SelectionCreateView(CreateAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer
    permission_classes = [IsAuthenticated]


class SelectionUpdateView(UpdateAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer
    permission_classes = [IsAuthenticated, SelectionChangePermission]


class SelectionDeleteView(DestroyAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionDeleteSerializer
    success_url = "/"
    permission_classes = [IsAuthenticated, SelectionChangePermission]

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=200)

