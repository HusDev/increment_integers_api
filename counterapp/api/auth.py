
from counterapp.schemas.message import MessageOut
from counterapp.schemas.auth import UserAuthDataIn, AuthSchemaOut,UserSchemaout, UserCreateIn
from counterapp.permissions import get_token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from ninja import Router

auth = Router(tags=['auth'])

#-------------------------------------------------------------------------  

@auth.post("/register", auth=None, response={201: MessageOut})
def create_user(request, payload: UserCreateIn):
    # check if username or email is taken
    # to be implemented
   
    if User.objects.filter(email=payload.email).exists() or User.objects.filter(username=payload.username).exists():
        return 201, {'message': 'User exist'}
    else: 
        user = User.objects.create(username=payload.username, email=payload.email)
        password =payload.password
        user.password = make_password(password)
        user.save()
        return 201, {'message': 'User created successfully'}

#-------------------------------------------------------------------------  

@auth.post('/login', auth=None, response={404: MessageOut, 400: MessageOut, 200: AuthSchemaOut})
def login(request, data: UserAuthDataIn):
    
    user = authenticate(username=data.username, password=data.password)
    try:
        User.objects.get(pk=user.pk)
    except User.DoesNotExist:
        return 404, {'message': 'User does not exist.'}

    if user is not None:
        user.last_login = timezone.now()
        user.save(update_fields=['last_login'])
        token = get_token(user)
        return {
            'access': token['access'],
            'user': user
        }
    else:
        return 400, {'message': 'User does not exist or has no permissions'}

#-------------------------------------------------------------------------   

@auth.get('/me', response={200:UserSchemaout, 401: MessageOut})
def show(request):   
    user = request.auth.get('user') 
    if user is not None:
        return {'user': request.auth['user'],}
    else:
        return 401, {'message': 'Unauthorized'}
