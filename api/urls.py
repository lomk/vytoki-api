from django.urls import path
from . import views

urlpatterns = [
    path("health/", views.health),

    # Services
    path("services/", views.service_list),
    path("services/<slug:slug>/", views.service_detail),
    path("services/<slug:service_slug>/articles/", views.service_articles_list),
    path("services/<slug:service_slug>/articles/<int:article_id>/", views.service_article_detail),

    # Sections (legacy + generic content pages)
    path("sections/", views.sections_list),
    path("sections/<slug:slug>/", views.section_detail),
    path("sections/<slug:section_slug>/articles/", views.section_articles_list),
    path("sections/<slug:section_slug>/articles/<int:article_id>/", views.section_article_detail),

    # Contacts
    path("contacts/", views.contacts),

    # Blog
    path("blog/", views.blog_list),
    path("blog/<slug:slug>/", views.blog_detail),

    # FAQ & Pricing
    path("faq/", views.faq_list),
    path("pricing/", views.pricing_list),

    # Consultation requests
    path("consultations/", views.consultation_create),
]
