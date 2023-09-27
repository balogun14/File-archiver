from django.urls import path

from .views import ArchiverListView

urlpatterns = [
    path("", ArchiverListView.as_view(), name="archiver_list_view"),
]
