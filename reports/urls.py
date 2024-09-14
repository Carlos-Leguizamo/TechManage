from django.urls import path
from . import views

urlpatterns = [
    path("reports/", views.reports, name='reports'),
    path("new_report/", views.new_report, name='new_report'),
    path("delete_report/<int:id_reportes>/", views.delete_report, name='delete_report'),
]
