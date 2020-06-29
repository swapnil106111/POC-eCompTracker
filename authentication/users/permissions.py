from rest_framework import permissions
from .models import Role

class IsTeamMemberForTask(permissions.BasePermission):
    """
    Allow if user is a team member and is assigned to this task.
    """

    def has_permission(self, request, view):
        if request.user and request.user.role.name == Role.TEAM_MEMBER:
            return True
        else:
            return False