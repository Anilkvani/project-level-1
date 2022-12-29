from django.urls import path
from app.views import *
app_name='somathing1'

urlpatterns=[
    path('jinja_print/',jinja_print,name='jinja_print'),
]