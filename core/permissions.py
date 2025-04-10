from rest_framework.permissions import BasePermission, SAFE_METHODS

class isAuthenticatedPost(BasePermission):
    def has_permission(self, request, view):
        print(request.user)
        if request.method in SAFE_METHODS:
            return True
        print(request.user and request.user.is_authenticated)
        return request.user and request.user.is_authenticated