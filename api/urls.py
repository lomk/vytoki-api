from django.urls import path
from . import views

urlpatterns = [
    path("health/", views.health),
    path("services/", views.service_list),
    path("services/<slug:slug>/", views.service_detail),
    path("services/<slug:service_slug>/articles/", views.service_articles_list),
    path("services/<slug:service_slug>/articles/<int:article_id>/", views.article_detail),
    path("sections/", views.sections_list),
    path("sections/<slug:slug>/", views.section_detail),
    path("sections/<slug:section_slug>/articles/", views.section_articles_list),
    path("sections/<slug:section_slug>/articles/<int:article_id>/", views.article_detail),
    path("contacts/", views.contacts),
]