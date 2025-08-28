from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission class for Fundraiser ownership
    Allows read access to all users but restricts edit rights to owners
    
    Extends: rest_framework.permissions.BasePermission
    Used by: FundraiserDetail view
    """
    def has_object_permission(self, request, view, obj):
        """
        Determines if user has permission to perform action on fundraiser
        
        Args:
            request: HTTP request object
            view: View being accessed
            obj: Fundraiser instance being accessed
            
        Returns:
            bool: True if user can access, False if denied
            - TRUE for all GET, HEAD, OPTIONS requests (safe methods)
            - TRUE if user is fundraiser owner for unsafe methods
            - FALSE otherwise
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.owner == request.user


class IsSupporterOrReadOnly(permissions.BasePermission):
    """
    Custom permission class for Pledge support
    Allows read access to all users but restricts edit rights to supporters
    
    Extends: rest_framework.permissions.BasePermission
    Used by: PledgeDetail view
    """
    def has_object_permission(self, request, view, obj):
        """
        Determines if user has permission to perform action on pledge
        
        Args:
            request: HTTP request object
            view: View being accessed
            obj: Pledge instance being accessed
            
        Returns:
            bool: True if user can access, False if denied
            - TRUE for all GET, HEAD, OPTIONS requests (safe methods)
            - TRUE if user is pledge supporter for unsafe methods
            - FALSE otherwise
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.supporter == request.user