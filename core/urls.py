from django.urls import path
from .views import index, contato, produto


urlpatterns = [
    path('', view=index, name='index'),
    path('contato/', view=contato, name='contato'),
    path('produto/', view=produto, name='produto'),
]
