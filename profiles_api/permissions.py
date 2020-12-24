from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""
    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        """This function gets called whenever a request is made"""
        #print(view)
        if request.method in permissions.SAFE_METHODS: return True
        return request.user.id == obj.id

class UpdateOwnStatus(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS: return True
        return obj.user_profile.id == request.user.id
