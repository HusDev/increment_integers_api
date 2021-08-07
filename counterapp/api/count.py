
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
        sequence = Sequence.objects.create(owner=user, current=0)
        return 200, {'message': "0"}
    else: 
        return 200, {'message': str(last)}

#-------------------------------------------------------------------------  

@count.get("/next", response={200: MessageOut})
def next(request):
    user = request.auth.get('user')
    last = Sequence.objects.filter(owner=user).last()
    if last is None: 
        sequence = Sequence.objects.create(owner=user, current=0)
        return 200, {'message': "0"}
    else: 
        last = Sequence.objects.filter(owner=user).last()
        last = last.get_incerement()
        sequence = Sequence.objects.create(owner=user, current=last)
        return 200, {'message': str(last)}

#-------------------------------------------------------------------------  

@count.put("/current", response={200: MessageOut})
def update(request, sequence: SequenceIn):
    user = request.auth.get('user')
    last = Sequence.objects.filter(owner=user).last()
    last.current = sequence.current 
    last.save()
    return 200, {'message': str(last)}