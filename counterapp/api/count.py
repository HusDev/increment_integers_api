
from counterapp.schemas.message import MessageOut

from counterapp.permissions import get_token
from counterapp.models import Sequence
from counterapp.schemas.sequence import SequenceIn

from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from ninja import Router

count = Router(tags=['count'])

#-------------------------------------------------------------------------  

@count.get("/current", response={200: MessageOut})
def get_current(request):
    user = request.auth.get('user')
    last = Sequence.objects.filter(owner=user).last()
    if last is None: 
        sequence = Sequence.objects.create(owner=user, value=1)
        return 200, {'message': "1"}
    else: 
        return 200, {'message': str(last)}

#-------------------------------------------------------------------------  

@count.get("/next", response={200: MessageOut})
def get_current(request):
    user = request.auth.get('user')
    last = Sequence.objects.filter(owner=user).last()
    if last is None: 
        sequence = Sequence.objects.create(owner=user, value=1)
        return 200, {'message': "1"}
    else: 
        last = Sequence.objects.filter(owner=user).last()
        last = last.get_incerement()
        sequence = Sequence.objects.create(owner=user, value=last)
        return 200, {'message': str(last)}

#-------------------------------------------------------------------------  

@count.put("/current/{current}", response={200: MessageOut})
def get_current(request, current:int, payload: SequenceIn):
    user = request.auth.get('user')
    last = Sequence.objects.filter(owner=user).last()
    last.current = current
    last.save()
    return 200, {'message': str(last)}