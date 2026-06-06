from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Section, Service, Contacts, BlogPost, FAQ, PricingPlan, ConsultationRequest, LANGUAGES


def get_language(request):
    lang = request.GET.get('lang', 'uk')
    valid = [code for code, _ in LANGUAGES]
    return lang if lang in valid else 'uk'


def get_field(obj, field_name, lang):
    return getattr(obj, f"{field_name}_{lang}", "") or ""


def service_data(s, lang):
    return {
        "slug": s.slug,
        "title": get_field(s, "title", lang),
        "subtitle": get_field(s, "subtitle", lang),
        "body": get_field(s, "body", lang),
        "seo_title": get_field(s, "seo_title", lang),
        "seo_description": get_field(s, "seo_description", lang),
        "updated_at": s.updated_at,
        "images": [
            {"id": img.id, "image": img.image.url, "alt": get_field(img, "alt", lang), "sort": img.sort}
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
                    {"id": img.id, "image": img.image.url, "alt": get_field(img, "alt", lang), "sort": img.sort}
                    for img in a.images.all()
                ],
            }
            for a in s.articles.filter(is_published=True)
        ],
    }


def section_data(s, lang):
    return {
        "slug": s.slug,
        "title": get_field(s, "title", lang),
        "subtitle": get_field(s, "subtitle", lang),
        "body": get_field(s, "body", lang),
        "seo_title": get_field(s, "seo_title", lang),
        "seo_description": get_field(s, "seo_description", lang),
        "updated_at": s.updated_at,
        "images": [
            {"id": img.id, "image": img.image.url, "alt": get_field(img, "alt", lang), "sort": img.sort}
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
                    {"id": img.id, "image": img.image.url, "alt": get_field(img, "alt", lang), "sort": img.sort}
                    for img in a.images.all()
                ],
            }
            for a in s.articles.filter(is_published=True)
        ],
    }


@api_view(["GET"])
def health(request):
    return Response({"ok": True})


# ─── Services ───────────────────────────────────────────────────────────────

@api_view(["GET"])
def service_list(request):
    lang = get_language(request)
    qs = Service.objects.filter(is_published=True)
    return Response([service_data(s, lang) for s in qs])


@api_view(["GET"])
def service_detail(request, slug):
    lang = get_language(request)
    s = Service.objects.filter(is_published=True, slug=slug).first()
    if not s:
        return Response({"detail": "Not found"}, status=404)
    return Response(service_data(s, lang))


@api_view(["GET"])
def service_articles_list(request, service_slug):
    lang = get_language(request)
    service = Service.objects.filter(is_published=True, slug=service_slug).first()
    if not service:
        return Response({"detail": "Not found"}, status=404)
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
                {"id": img.id, "image": img.image.url, "alt": get_field(img, "alt", lang), "sort": img.sort}
                for img in a.images.all()
            ],
        }
        for a in articles
    ]
    return Response(data)


@api_view(["GET"])
def service_article_detail(request, service_slug, article_id):
    lang = get_language(request)
    service = Service.objects.filter(is_published=True, slug=service_slug).first()
    if not service:
        return Response({"detail": "Not found"}, status=404)
    article = service.articles.filter(is_published=True, id=article_id).first()
    if not article:
        return Response({"detail": "Not found"}, status=404)
    return Response({
        "id": article.id,
        "title": get_field(article, "title", lang),
        "subtitle": get_field(article, "subtitle", lang),
        "text": get_field(article, "text", lang),
        "seo_title": get_field(article, "seo_title", lang),
        "seo_description": get_field(article, "seo_description", lang),
        "sort": article.sort,
        "updated_at": article.updated_at,
        "images": [
            {"id": img.id, "image": img.image.url, "alt": get_field(img, "alt", lang), "sort": img.sort}
            for img in article.images.all()
        ],
    })


# ─── Sections ────────────────────────────────────────────────────────────────

@api_view(["GET"])
def sections_list(request):
    lang = get_language(request)
    qs = Section.objects.filter(is_published=True)
    return Response([section_data(s, lang) for s in qs])


@api_view(["GET"])
def section_detail(request, slug):
    lang = get_language(request)
    s = Section.objects.filter(is_published=True, slug=slug).first()
    if not s:
        return Response({"detail": "Not found"}, status=404)
    return Response(section_data(s, lang))


@api_view(["GET"])
def section_articles_list(request, section_slug):
    lang = get_language(request)
    section = Section.objects.filter(is_published=True, slug=section_slug).first()
    if not section:
        return Response({"detail": "Not found"}, status=404)
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
                {"id": img.id, "image": img.image.url, "alt": get_field(img, "alt", lang), "sort": img.sort}
                for img in a.images.all()
            ],
        }
        for a in articles
    ]
    return Response(data)


@api_view(["GET"])
def section_article_detail(request, section_slug, article_id):
    lang = get_language(request)
    section = Section.objects.filter(is_published=True, slug=section_slug).first()
    if not section:
        return Response({"detail": "Not found"}, status=404)
    article = section.articles.filter(is_published=True, id=article_id).first()
    if not article:
        return Response({"detail": "Not found"}, status=404)
    return Response({
        "id": article.id,
        "title": get_field(article, "title", lang),
        "subtitle": get_field(article, "subtitle", lang),
        "text": get_field(article, "text", lang),
        "seo_title": get_field(article, "seo_title", lang),
        "seo_description": get_field(article, "seo_description", lang),
        "sort": article.sort,
        "updated_at": article.updated_at,
        "images": [
            {"id": img.id, "image": img.image.url, "alt": get_field(img, "alt", lang), "sort": img.sort}
            for img in article.images.all()
        ],
    })


# ─── Contacts ────────────────────────────────────────────────────────────────

@api_view(["GET"])
def contacts(request):
    lang = get_language(request)
    contact = Contacts.objects.first()
    if not contact:
        return Response({"detail": "Not found"}, status=404)
    return Response({
        "title": get_field(contact, "title", lang),
        "text": get_field(contact, "text", lang),
        "address": get_field(contact, "address", lang),
        "phone1": contact.phone1,
        "phone2": contact.phone2,
        "phone3": contact.phone3,
        "email": contact.email,
        "telegram": contact.telegram,
        "viber": contact.viber,
        "whatsapp": contact.whatsapp,
        "updated_at": contact.updated_at,
    })


# ─── Blog ─────────────────────────────────────────────────────────────────────

@api_view(["GET"])
def blog_list(request):
    lang = get_language(request)
    qs = BlogPost.objects.filter(is_published=True)
    data = [
        {
            "slug": p.slug,
            "title": get_field(p, "title", lang),
            "subtitle": get_field(p, "subtitle", lang),
            "seo_description": get_field(p, "seo_description", lang),
            "cover_image": p.cover_image.url if p.cover_image else None,
            "published_at": p.published_at,
        }
        for p in qs
    ]
    return Response(data)


@api_view(["GET"])
def blog_detail(request, slug):
    lang = get_language(request)
    post = BlogPost.objects.filter(is_published=True, slug=slug).first()
    if not post:
        return Response({"detail": "Not found"}, status=404)
    return Response({
        "slug": post.slug,
        "title": get_field(post, "title", lang),
        "subtitle": get_field(post, "subtitle", lang),
        "body": get_field(post, "body", lang),
        "seo_title": get_field(post, "seo_title", lang),
        "seo_description": get_field(post, "seo_description", lang),
        "cover_image": post.cover_image.url if post.cover_image else None,
        "published_at": post.published_at,
        "updated_at": post.updated_at,
    })


# ─── FAQ ──────────────────────────────────────────────────────────────────────

@api_view(["GET"])
def faq_list(request):
    lang = get_language(request)
    qs = FAQ.objects.filter(is_published=True)
    data = [
        {
            "id": f.id,
            "question": get_field(f, "question", lang),
            "answer": get_field(f, "answer", lang),
            "category": f.category,
            "sort": f.sort,
        }
        for f in qs
    ]
    return Response(data)


# ─── Pricing ──────────────────────────────────────────────────────────────────

@api_view(["GET"])
def pricing_list(request):
    lang = get_language(request)
    qs = PricingPlan.objects.filter(is_published=True)
    data = [
        {
            "slug": p.slug,
            "name": get_field(p, "name", lang),
            "description": get_field(p, "description", lang),
            "features": [f.strip() for f in get_field(p, "features", lang).splitlines() if f.strip()],
            "price_display": get_field(p, "price_display", lang),
            "is_featured": p.is_featured,
            "sort": p.sort,
        }
        for p in qs
    ]
    return Response(data)


# ─── Consultations ────────────────────────────────────────────────────────────

@csrf_exempt
@api_view(["POST"])
def consultation_create(request):
    name = (request.data.get("name") or "").strip()
    if not name:
        return Response({"detail": "Name is required"}, status=400)

    valid_methods = [c[0] for c in ConsultationRequest.CONTACT_METHOD_CHOICES]
    contact_method = request.data.get("contact_method", "phone")
    if contact_method not in valid_methods:
        contact_method = "phone"

    ConsultationRequest.objects.create(
        name=name,
        email=(request.data.get("email") or "").strip(),
        phone=(request.data.get("phone") or "").strip(),
        contact_method=contact_method,
        message=(request.data.get("message") or "").strip(),
    )
    return Response({"detail": "Request received"}, status=201)
