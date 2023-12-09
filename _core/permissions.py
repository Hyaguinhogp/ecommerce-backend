from rest_framework.permissions import BasePermission
from rest_framework.views import Request
from rest_framework.exceptions import AuthenticationFailed
from users.models import User

import jwt

class IsAuthenticated(BasePermission):
    def has_permission(self, request: Request, view):
        try:
            token = request.headers['Authorization'].split(' ')[1]
            decoded_token = jwt.decode(token, 'secret', algorithms='HS256')
            request.is_superuser = User.objects.get(id=decoded_token['user_id']).is_superuser
            return True

        except KeyError:
            raise AuthenticationFailed('Token não disponibilizado')

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token expirado')

        except jwt.InvalidTokenError:
            raise AuthenticationFailed('Token inválido')
        
class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.is_superuser:
            return True
        
        raise AuthenticationFailed('Sem autorização')