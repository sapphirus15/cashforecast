from django.urls import path
from . import views

app_name = "cashs"

urlpatterns = [
    path("", views.CashListView.as_view(), name="cashs_home"),
]