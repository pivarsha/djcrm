from django.urls import path
from .views import home_page,landing_page,lead_create,lead_detail,lead_update,lead_delete,LandingPageView,LeadListView,LeadDetailView,LeadCreateView,LeadUpdateView,LeadDeleteView
# from .views import *

app_name = "leads"

urlpatterns = [
    path("",LandingPageView.as_view(),name="home"),
    # path("home",home_page,name="h"),
    path("home",LeadListView.as_view(),name="h"),
    # path("create",lead_create,name="create"),
    path("create",LeadCreateView.as_view(),name="create"),
    # path("<int:pk>",lead_detail,name="detail"),
    path("<int:pk>",LeadDetailView.as_view(),name="detail"),
    # path("<int:pk>/update",lead_update,name="update"),
    path("<int:pk>/update",LeadUpdateView.as_view(),name="update"),
    # path("<int:pk>/delete",lead_delete,name="delete"),
    path("<int:pk>/delete",LeadDeleteView.as_view(),name="delete"),
]