from django.urls import path
from . import views

urlpatterns = [
    path("health/", views.health),
    path("sections/", views.sections_list),
    path("sections/<slug:slug>/", views.section_detail),
    path("sections/<slug:section_slug>/articles/", views.articles_list),
    path("sections/<slug:section_slug>/articles/<int:article_id>/", views.article_detail),
    path("contacts/", views.contacts),
]