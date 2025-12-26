from django.contrib import admin
from .models import Service, ServiceImage, ServiceArticle, ServiceArticleImage, Contacts

class ServiceImageInline(admin.TabularInline):
    model = ServiceImage
    extra = 1
    fields = ("image", "alt_en", "alt_uk", "alt_ru", "sort")

class ServiceArticleImageInline(admin.TabularInline):
    model = ServiceArticleImage
    extra = 1
    fields = ("image", "alt_en", "alt_uk", "alt_ru", "sort")

class ServiceArticleInline(admin.TabularInline):
    model = ServiceArticle
    extra = 1
    fields = ("title_en", "title_uk", "title_ru", "sort", "is_published")

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("slug", "title_en", "is_published", "updated_at")
    list_filter = ("is_published",)
    search_fields = ("slug", "title_en", "title_uk", "title_ru", "body_en", "body_uk", "body_ru")
    fieldsets = (
        ('Service Info', {
            'fields': ('slug', 'is_published')
        }),
        ('English', {
            'fields': ('title_en', 'subtitle_en', 'body_en', 'seo_title_en', 'seo_description_en')
        }),
        ('Ukrainian', {
            'fields': ('title_uk', 'subtitle_uk', 'body_uk', 'seo_title_uk', 'seo_description_uk')
        }),
        ('German', {
            'fields': ('title_de', 'subtitle_de', 'body_de', 'seo_title_de', 'seo_description_de')
        }),
    )
    inlines = [ServiceImageInline, ServiceArticleInline]

@admin.register(ServiceArticle)
class ServiceArticleAdmin(admin.ModelAdmin):
    list_display = ("title_en", "service", "sort", "is_published", "updated_at")
    list_filter = ("is_published", "service")
    search_fields = ("title_en", "title_uk", "title_ru", "text_en", "text_uk", "text_ru")
    fieldsets = (
        ('Article Info', {
            'fields': ('service', 'sort', 'is_published')
        }),
        ('English', {
            'fields': ('title_en', 'subtitle_en', 'text_en', 'seo_title_en', 'seo_description_en')
        }),
        ('Ukrainian', {
            'fields': ('title_uk', 'subtitle_uk', 'text_uk', 'seo_title_uk', 'seo_description_uk')
        }),
        ('German', {
            'fields': ('title_de', 'subtitle_de', 'text_de', 'seo_title_de', 'seo_description_de')
        }),
    )
    inlines = [ServiceArticleImageInline]

@admin.register(ServiceImage)
class ServiceImageAdmin(admin.ModelAdmin):
    list_display = ("service", "sort", "alt_en")
    list_filter = ("service",)
    search_fields = ("service__slug", "alt_en", "alt_uk", "alt_de")
    fieldsets = (
        ('Image Info', {
            'fields': ('service', 'image', 'sort')
        }),
        ('Alt Text - English', {
            'fields': ('alt_en',)
        }),
        ('Alt Text - Ukrainian', {
            'fields': ('alt_uk',)
        }),
        ('Alt Text - German', {
            'fields': ('alt_de',)
        }),
    )

@admin.register(ServiceArticleImage)
class ServiceArticleImageAdmin(admin.ModelAdmin):
    list_display = ("article", "sort", "alt_en")
    list_filter = ("article__service",)
    search_fields = ("article__title_en", "article__title_uk", "article__title_de", "alt_en", "alt_uk", "alt_de")
    fieldsets = (
        ('Image Info', {
            'fields': ('article', 'image', 'sort')
        }),
        ('Alt Text - English', {
            'fields': ('alt_en',)
        }),
        ('Alt Text - Ukrainian', {
            'fields': ('alt_uk',)
        }),
        ('Alt Text - German', {
            'fields': ('alt_de',)
        }),
    )

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ("title_en", "phone1", "phone2", "phone3", "updated_at")
    search_fields = ("title_en", "title_uk", "title_de", "phone1", "phone2", "phone3")
    fieldsets = (
        ('Contact Info', {
            'fields': ('phone1', 'phone2', 'phone3')
        }),
        ('English', {
            'fields': ('title_en', 'text_en', 'address_en')
        }),
        ('Ukrainian', {
            'fields': ('title_uk', 'text_uk', 'address_uk')
        }),
        ('German', {
            'fields': ('title_de', 'text_de', 'address_de')
        }),
    )