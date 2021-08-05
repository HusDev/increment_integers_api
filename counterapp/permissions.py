import datetime
import jwt
from django.conf import settings
from ninja.security import HttpBearer
from django.contrib.auth.models import User

TIME_DELTA = datetime.timedelta(days=30)

class IsAuthenticated(HttpBearer):
    def authenticate(self, request, token):
        try:
            user_pk = jwt.decode(token, key=settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.exceptions.InvalidTokenError as e:
            return {'token': 'unauthorized'}
        user = User.objects.get(pk=user_pk['user'])
        if user:
            return {'user': user,  'token': token}


def get_token(user):
    token = jwt.encode({'user': user.pk, 'exp': datetime.datetime.utcnow() + TIME_DELTA},
                       key=settings.SECRET_KEY,
                       algorithm='HS256')
    return {
        'access': str(token),
    }