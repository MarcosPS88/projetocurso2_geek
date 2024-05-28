from django.urls import path
from .views import index, contato, produto, login, logout


urlpatterns = [
    path('', view=index, name='index'),
    path('contato/', view=contato, name='contato'),
    path('produto/', view=produto, name='produto'),
    path('login/', view=login, name='login'),
    path('logout/', view=logout, name='logout'),

]
