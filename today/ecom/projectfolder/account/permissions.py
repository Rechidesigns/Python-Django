from rest_framework import permissions
# from rest_framework.exceptions import PermissionDenied

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Allow access all users but gives special permissions to admin users.
    """

    def has_permission(self, request, view):
        if request.mothod in permissions.SAFE_METHODS:

            return True

        else:
            if request.user.is_authentication and request.user.is_staff == True:
                return True

            return False

            
 