from django.urls import path
from . import views

urlpatterns = [
    path('editor/', views.code_editor, name='code_editor'),
]
