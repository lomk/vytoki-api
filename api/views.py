from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Section, Service, Contacts, LANGUAGES

def get_language(request):
    """Get language from query parameter, default to 'en'"""
    lang = request.GET.get('lang', 'en')
    # Validate language code
    if lang not in [code for code, _ in LANGUAGES]:
        lang = 'en'
    return lang

def get_field(obj, field_name, lang):
    """Get translated field value"""
    return getattr(obj, f"{field_name}_{lang}", "")

@api_view(["GET"])
def health(request):
    return Response({"ok": True})

@api_view(["GET"])
def service_list(request):
    lang = get_language(request)
    qs = Service.objects.filter(is_published=True).order_by("slug")
    data = [
        {
            "slug": s.slug,
            "title": get_field(s, "title", lang),
            "subtitle": get_field(s, "subtitle", lang),
            "body": get_field(s, "body", lang),
            "seo_title": get_field(s, "seo_title", lang),
            "seo_description": get_field(s, "seo_description", lang),
            "updated_at": s.updated_at,
            "images": [
                {
                    "id": img.id,
                    "image": img.image.url,
                    "alt": get_field(img, "alt", lang),
                    "sort": img.sort
                }
                for img in s.images.all()
            ],
            "articles": [
                {
                    "id": a.id,
                    "title": get_field(a, "title", lang),
                    "subtitle": get_field(a, "subtitle", lang),
                    "text": get_field(a, "text", lang),
                    "sort": a.sort,
                    "updated_at": a.updated_at,
                    "images": [
                        {
                            "id": img.id,
                            "image": img.image.url,
                            "alt": get_field(img, "alt", lang),
                            "sort": img.sort
                        }
                        for img in a.images.all()
                    ],
                }
                for a in s.articles.filter(is_published=True)
            ],
        }
        for s in qs
    ]
    return Response(data)

@api_view(["GET"])
def service_detail(request, slug: str):
    lang = get_language(request)
    s = Service.objects.filter(is_published=True, slug=slug).first()
    if not s:
        return Response({"detail": "Not found"}, status=404)

    data = {
        "slug": s.slug,
        "title": get_field(s, "title", lang),
        "subtitle": get_field(s, "subtitle", lang),
        "body": get_field(s, "body", lang),
        "seo_title": get_field(s, "seo_title", lang),
        "seo_description": get_field(s, "seo_description", lang),
        "updated_at": s.updated_at,
        "images": [
            {
                "id": img.id,
                "image": img.image.url,
                "alt": get_field(img, "alt", lang),
                "sort": img.sort
            }
            for img in s.images.all()
        ],
        "articles": [
            {
                "id": a.id,
                "title": get_field(a, "title", lang),
                "subtitle": get_field(a, "subtitle", lang),
                "text": get_field(a, "text", lang),
                "seo_title": get_field(a, "seo_title", lang),
                "seo_description": get_field(a, "seo_description", lang),
                "sort": a.sort,
                "updated_at": a.updated_at,
                "images": [
                    {
                        "id": img.id,
                        "image": img.image.url,
                        "alt": get_field(img, "alt", lang),
                        "sort": img.sort
                    }
                    for img in a.images.all()
                ],
            }
            for a in s.articles.filter(is_published=True)
        ],
    }
    return Response(data)

@api_view(["GET"])
def section_detail(request, slug: str):
    lang = get_language(request)
    s = Section.objects.filter(is_published=True, slug=slug).first()
    if not s:
        return Response({"detail": "Not found"}, status=404)

    data = {
        "slug": s.slug,
        "title": get_field(s, "title", lang),
        "subtitle": get_field(s, "subtitle", lang),
        "body": get_field(s, "body", lang),
        "seo_title": get_field(s, "seo_title", lang),
        "seo_description": get_field(s, "seo_description", lang),
        "updated_at": s.updated_at,
        "images": [
            {
                "id": img.id,
                "image": img.image.url,
                "alt": get_field(img, "alt", lang),
                "sort": img.sort
            }
            for img in s.images.all()
        ],
        "articles": [
            {
                "id": a.id,
                "title": get_field(a, "title", lang),
                "subtitle": get_field(a, "subtitle", lang),
                "text": get_field(a, "text", lang),
                "seo_title": get_field(a, "seo_title", lang),
                "seo_description": get_field(a, "seo_description", lang),
                "sort": a.sort,
                "updated_at": a.updated_at,
                "images": [
                    {
                        "id": img.id,
                        "image": img.image.url,
                        "alt": get_field(img, "alt", lang),
                        "sort": img.sort
                    }
                    for img in a.images.all()
                ],
            }
            for a in s.articles.filter(is_published=True)
        ],
    }
    return Response(data)

@api_view(["GET"])
def service_articles_list(request, service_slug: str):
    lang = get_language(request)
    service = Service.objects.filter(is_published=True, slug=service_slug).first()
    if not service:
        return Response({"detail": "Service not found"}, status=404)

    articles = service.articles.filter(is_published=True)
    data = [
        {
            "id": a.id,
            "title": get_field(a, "title", lang),
            "subtitle": get_field(a, "subtitle", lang),
            "text": get_field(a, "text", lang),
            "sort": a.sort,
            "updated_at": a.updated_at,
            "images": [
                {
                    "id": img.id,
                    "image": img.image.url,
                    "alt": get_field(img, "alt", lang),
                    "sort": img.sort
                }
                for img in a.images.all()
            ],
        }
        for a in articles
    ]
    return Response(data)

@api_view(["GET"])
def section_articles_list(request, section_slug: str):
    lang = get_language(request)
    section = Section.objects.filter(is_published=True, slug=section_slug).first()
    if not section:
        return Response({"detail": "Section not found"}, status=404)

    articles = section.articles.filter(is_published=True)
    data = [
        {
            "id": a.id,
            "title": get_field(a, "title", lang),
            "subtitle": get_field(a, "subtitle", lang),
            "text": get_field(a, "text", lang),
            "sort": a.sort,
            "updated_at": a.updated_at,
            "images": [
                {
                    "id": img.id,
                    "image": img.image.url,
                    "alt": get_field(img, "alt", lang),
                    "sort": img.sort
                }
                for img in a.images.all()
            ],
        }
        for a in articles
    ]
    return Response(data)

@api_view(["GET"])
def service_article_detail(request, service_slug: str, article_id: int):
    lang = get_language(request)
    service = Service.objects.filter(is_published=True, slug=service_slug).first()
    if not service:
        return Response({"detail": "Section not found"}, status=404)

    article = service.articles.filter(is_published=True, id=article_id).first()
    if not article:
        return Response({"detail": "Article not found"}, status=404)

    data = {
        "id": article.id,
        "title": get_field(article, "title", lang),
        "subtitle": get_field(article, "subtitle", lang),
        "text": get_field(article, "text", lang),
        "sort": article.sort,
        "updated_at": article.updated_at,
        "seo_title": get_field(article, "seo_title", lang),
        "seo_description": get_field(article, "seo_description", lang),
        "images": [
            {
                "id": img.id,
                "image": img.image.url,
                "alt": get_field(img, "alt", lang),
                "sort": img.sort
            }
            for img in article.images.all()
        ],
    }
    return Response(data)

@api_view(["GET"])
def contacts(request):
    lang = get_language(request)
    contact = Contacts.objects.first()
    if not contact:
        return Response({"detail": "Not found"}, status=404)

    data = {
        "title": get_field(contact, "title", lang),
        "text": get_field(contact, "text", lang),
        "phone1": contact.phone1,
        "phone2": contact.phone2,
        "phone3": contact.phone3,
        "address": get_field(contact, "address", lang),
        "updated_at": contact.updated_at,
    }
    return Response(data)