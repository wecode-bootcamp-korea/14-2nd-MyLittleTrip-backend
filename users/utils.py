import jwt, json
from django.http import JsonResponse

from .models     import User
from my_settings import SECRET_KEY,JWT_ALGORITHM

def Login_decorator(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            token        = request.headers.get('Authorization', None)
            payload      = jwt.decode(token, SECRET_KEY, algorithm = JWT_ALGORITHM)
            user         = User.objects.get(id=payload['id'])
            request.user = user

        except jwt.exceptions.DecodeError:
            return JsonResponse ({'message':'INVALID_TOKEN'}, status=400)

        except User.DoesNotExist:
            return JsonResponse ({'message':'INVALID_USER'}, status=400)

        return func(self, request, *args, **kwargs)
    return wrapper
