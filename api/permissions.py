from rest_framework.permissions import BasePermission


class IsCartUser(BasePermission):
	message = "It's not Ur Cart !"

	def has_object_permission(self, request, view, obj):
		if (obj.user == request.user):
			return True
		else:
			return False

