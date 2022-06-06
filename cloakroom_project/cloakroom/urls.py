from django.urls import include, path
from . import views


app_name = 'cloakroom'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('update-label/<int:label_id>/', views.UpdateLabelView.as_view(), name='update-label'),
]
