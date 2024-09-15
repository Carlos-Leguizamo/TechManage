from django.urls import path
from . import views

urlpatterns = [
    path("reports/", views.reports, name='reports'),
    path("new_report/", views.new_report, name='new_report'),
    path("view_report/<int:id_reportes>/", views.generate_pdf_view, name='view_report'), 
]
