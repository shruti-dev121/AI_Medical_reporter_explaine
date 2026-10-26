from django.urls import path
from . import views

urlpatterns = [
    path("", views.upload_report, name="upload_report"),
    path("history/", views.report_history, name="report_history"),

]