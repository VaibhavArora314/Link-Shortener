from django.urls import path
from . import views

app_name = 'links'

urlpatterns = [
    path('',views.CreateLink.as_view(), name = 'create-link'),
    path('s/<str:tag>/',views.RedirectLink.as_view(), name='redirect'),
    path('not-found/',views.NotFound, name='not-found'),
    path('my-links/',views.ListLink.as_view(),name='my-links')
]
