from django.contrib import admin
from .models import (
    Service, ServiceImage, ServiceArticle, ServiceArticleImage,
    Section, SectionImage, SectionArticle, SectionArticleImage,
    Contacts, BlogPost, FAQ, PricingPlan, ConsultationRequest,
)


# ─── Service ─────────────────────────────────────────────────────────────────

class ServiceImageInline(admin.TabularInline):
    model = ServiceImage
    extra = 1
    fields = ("image", "alt_en", "alt_uk", "alt_ru", "sort")


class ServiceArticleInline(admin.TabularInline):
    model = ServiceArticle
    extra = 1
    fields = ("title_uk", "title_en", "sort", "is_published")
    show_change_link = True


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("slug", "title_uk", "title_en", "is_published", "updated_at")
    list_filter = ("is_published",)
    search_fields = ("slug", "title_en", "title_uk", "title_ru")
    prepopulated_fields = {"slug": ("title_en",)}
    fieldsets = (
        ("Meta", {"fields": ("slug", "is_published")}),
        ("Ukrainian", {"fields": ("title_uk", "subtitle_uk", "body_uk", "seo_title_uk", "seo_description_uk")}),
        ("English", {"fields": ("title_en", "subtitle_en", "body_en", "seo_title_en", "seo_description_en")}),
        ("Russian", {"fields": ("title_ru", "subtitle_ru", "body_ru", "seo_title_ru", "seo_description_ru")}),
    )
    inlines = [ServiceImageInline, ServiceArticleInline]


@admin.register(ServiceArticle)
class ServiceArticleAdmin(admin.ModelAdmin):
    list_display = ("title_uk", "service", "sort", "is_published", "updated_at")
    list_filter = ("is_published", "service")
    search_fields = ("title_en", "title_uk", "title_ru")
    fieldsets = (
        ("Meta", {"fields": ("service", "sort", "is_published")}),
        ("Ukrainian", {"fields": ("title_uk", "subtitle_uk", "text_uk", "seo_title_uk", "seo_description_uk")}),
        ("English", {"fields": ("title_en", "subtitle_en", "text_en", "seo_title_en", "seo_description_en")}),
        ("Russian", {"fields": ("title_ru", "subtitle_ru", "text_ru", "seo_title_ru", "seo_description_ru")}),
    )
    inlines = [
        type("ServiceArticleImageInline", (admin.TabularInline,), {
            "model": ServiceArticleImage, "extra": 1,
            "fields": ("image", "alt_en", "alt_uk", "alt_ru", "sort"),
        })
    ]


# ─── Section ─────────────────────────────────────────────────────────────────

class SectionImageInline(admin.TabularInline):
    model = SectionImage
    extra = 1
    fields = ("image", "alt_en", "alt_uk", "alt_ru", "sort")


class SectionArticleInline(admin.TabularInline):
    model = SectionArticle
    extra = 1
    fields = ("title_uk", "title_en", "sort", "is_published")
    show_change_link = True


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ("slug", "title_uk", "title_en", "is_published", "updated_at")
    list_filter = ("is_published",)
    search_fields = ("slug", "title_en", "title_uk", "title_ru")
    prepopulated_fields = {"slug": ("title_en",)}
    fieldsets = (
        ("Meta", {"fields": ("slug", "is_published")}),
        ("Ukrainian", {"fields": ("title_uk", "subtitle_uk", "body_uk", "seo_title_uk", "seo_description_uk")}),
        ("English", {"fields": ("title_en", "subtitle_en", "body_en", "seo_title_en", "seo_description_en")}),
        ("Russian", {"fields": ("title_ru", "subtitle_ru", "body_ru", "seo_title_ru", "seo_description_ru")}),
    )
    inlines = [SectionImageInline, SectionArticleInline]


@admin.register(SectionArticle)
class SectionArticleAdmin(admin.ModelAdmin):
    list_display = ("title_uk", "section", "sort", "is_published", "updated_at")
    list_filter = ("is_published", "section")
    search_fields = ("title_en", "title_uk", "title_ru")
    fieldsets = (
        ("Meta", {"fields": ("section", "sort", "is_published")}),
        ("Ukrainian", {"fields": ("title_uk", "subtitle_uk", "text_uk", "seo_title_uk", "seo_description_uk")}),
        ("English", {"fields": ("title_en", "subtitle_en", "text_en", "seo_title_en", "seo_description_en")}),
        ("Russian", {"fields": ("title_ru", "subtitle_ru", "text_ru", "seo_title_ru", "seo_description_ru")}),
    )
    inlines = [
        type("SectionArticleImageInline", (admin.TabularInline,), {
            "model": SectionArticleImage, "extra": 1,
            "fields": ("image", "alt_en", "alt_uk", "alt_ru", "sort"),
        })
    ]


# ─── Contacts ────────────────────────────────────────────────────────────────

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ("__str__", "email", "phone1", "telegram", "updated_at")
    fieldsets = (
        ("Contact channels", {"fields": ("phone1", "phone2", "phone3", "email", "telegram", "viber", "whatsapp")}),
        ("Ukrainian", {"fields": ("title_uk", "text_uk", "address_uk")}),
        ("English", {"fields": ("title_en", "text_en", "address_en")}),
        ("Russian", {"fields": ("title_ru", "text_ru", "address_ru")}),
    )


# ─── Blog ─────────────────────────────────────────────────────────────────────

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("slug", "title_uk", "is_published", "published_at", "updated_at")
    list_filter = ("is_published",)
    search_fields = ("slug", "title_en", "title_uk", "title_ru")
    prepopulated_fields = {"slug": ("title_en",)}
    fieldsets = (
        ("Meta", {"fields": ("slug", "cover_image", "is_published", "published_at")}),
        ("Ukrainian", {"fields": ("title_uk", "subtitle_uk", "body_uk", "seo_title_uk", "seo_description_uk")}),
        ("English", {"fields": ("title_en", "subtitle_en", "body_en", "seo_title_en", "seo_description_en")}),
        ("Russian", {"fields": ("title_ru", "subtitle_ru", "body_ru", "seo_title_ru", "seo_description_ru")}),
    )


# ─── FAQ ──────────────────────────────────────────────────────────────────────

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question_uk", "category", "sort", "is_published")
    list_filter = ("is_published", "category")
    search_fields = ("question_en", "question_uk", "question_ru")
    fieldsets = (
        ("Meta", {"fields": ("category", "sort", "is_published")}),
        ("Ukrainian", {"fields": ("question_uk", "answer_uk")}),
        ("English", {"fields": ("question_en", "answer_en")}),
        ("Russian", {"fields": ("question_ru", "answer_ru")}),
    )


# ─── Pricing ─────────────────────────────────────────────────────────────────

@admin.register(PricingPlan)
class PricingPlanAdmin(admin.ModelAdmin):
    list_display = ("slug", "name_uk", "is_featured", "sort", "is_published")
    list_filter = ("is_published", "is_featured")
    search_fields = ("slug", "name_en", "name_uk", "name_ru")
    prepopulated_fields = {"slug": ("name_en",)}
    fieldsets = (
        ("Meta", {"fields": ("slug", "sort", "is_featured", "is_published")}),
        ("Ukrainian", {"fields": ("name_uk", "description_uk", "features_uk", "price_display_uk")}),
        ("English", {"fields": ("name_en", "description_en", "features_en", "price_display_en")}),
        ("Russian", {"fields": ("name_ru", "description_ru", "features_ru", "price_display_ru")}),
    )


# ─── Consultation Requests ────────────────────────────────────────────────────

@admin.register(ConsultationRequest)
class ConsultationRequestAdmin(admin.ModelAdmin):
    list_display = ("name", "contact_method", "email", "phone", "is_read", "created_at")
    list_filter = ("is_read", "contact_method")
    search_fields = ("name", "email", "phone", "message")
    readonly_fields = ("name", "email", "phone", "contact_method", "message", "created_at")
    list_editable = ("is_read",)

    def has_add_permission(self, request):
        return False
