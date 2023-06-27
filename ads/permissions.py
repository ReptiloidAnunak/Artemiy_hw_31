from rest_framework import permissions
from django.http import Http404

from authentication.models import User
from ads.models import Ad, Selection


class AdChangePermission(permissions.BasePermission):
    message = 'Updating or deleting other users ads not allowed'

    def has_permission(self, request, view):

        ad = Ad.objects.get(pk=view.kwargs["pk"])
        if request.user.role in ["admin", "moderator"]:
            return True
        elif ad.author_id == request.user.id:
            return True
        return False


class SelectionChangePermission(permissions.BasePermission):
    message = 'Updating or deleting other users selections not allowed'

    def has_permission(self, request, view):
        selection = Selection.objects.get(pk=view.kwargs["pk"])
        if request.user.id != selection.owner.id:
            return False
        return True
