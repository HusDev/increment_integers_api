from counterapp.permissions import IsAuthenticated
from ninja import NinjaAPI
from counterapp.api.auth import auth

api = NinjaAPI(version='0.0.1',
title='Incerement Integers',
description='Incerement Integers API',
auth = IsAuthenticated())
api.add_router('/auth', auth)