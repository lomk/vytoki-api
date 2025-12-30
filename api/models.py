from django.db import models
from django.conf import settings

LANGUAGES = [
    ('en', 'English'),
    ('uk', 'Ukrainian'),
    ('ru', 'Russian'),
]

class Service(models.Model):
    slug = models.SlugField(unique=True)
    
    # English
    title_en = models.CharField(max_length=200, blank=True)
    subtitle_en = models.CharField(max_length=300, blank=True)
    body_en = models.TextField(blank=True)
    seo_title_en = models.CharField(max_length=255, blank=True)
    seo_description_en = models.CharField(max_length=255, blank=True)
    
    # Ukrainian
    title_uk = models.CharField(max_length=200, blank=True)
    subtitle_uk = models.CharField(max_length=300, blank=True)
    body_uk = models.TextField(blank=True)
    seo_title_uk = models.CharField(max_length=255, blank=True)
    seo_description_uk = models.CharField(max_length=255, blank=True)
    
    # Russian
    title_ru = models.CharField(max_length=200, blank=True)
    subtitle_ru = models.CharField(max_length=300, blank=True)
    body_ru = models.TextField(blank=True)
    seo_title_ru = models.CharField(max_length=255, blank=True)
    seo_description_ru = models.CharField(max_length=255, blank=True)

    is_published = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["slug"]

    def __str__(self):
        return f"{self.slug} - {self.title_en}"


class ServiceImage(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="services/%Y/%m/")

    # English
    alt_en = models.CharField(max_length=200, blank=True)
    
    # Ukrainian
    alt_uk = models.CharField(max_length=200, blank=True)
    
    # Russian
    alt_ru = models.CharField(max_length=200, blank=True)

    sort = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort", "id"]

    def __str__(self):
        return f"{self.service.slug} #{self.id}"


class ServiceArticle(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="articles")

    # English
    title_en = models.CharField(max_length=200, blank=True)
    subtitle_en = models.CharField(max_length=500, blank=True)
    text_en = models.TextField(blank=True)
    seo_title_en = models.CharField(max_length=255, blank=True)
    seo_description_en = models.CharField(max_length=255, blank=True)
    
    # Ukrainian
    title_uk = models.CharField(max_length=200, blank=True)
    subtitle_uk = models.CharField(max_length=500, blank=True)
    text_uk = models.TextField(blank=True)
    seo_title_uk = models.CharField(max_length=255, blank=True)
    seo_description_uk = models.CharField(max_length=255, blank=True)
    
    # Russian
    title_ru = models.CharField(max_length=200, blank=True)
    subtitle_ru = models.CharField(max_length=500, blank=True)
    text_ru = models.TextField(blank=True)
    seo_title_ru = models.CharField(max_length=255, blank=True)
    seo_description_ru = models.CharField(max_length=255, blank=True)
    
    sort = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["sort", "id"]

    def __str__(self):
        return f"{self.service.slug} - {self.title}"


class ServiceArticleImage(models.Model):
    article = models.ForeignKey(ServiceArticle, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="service_articles/%Y/%m/")
    
    alt_en = models.CharField(max_length=200, blank=True)
    alt_uk = models.CharField(max_length=200, blank=True)
    alt_ru = models.CharField(max_length=200, blank=True)

    sort = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort", "id"]

    def __str__(self):
        return f"{self.article.title} #{self.id}"
    

class Section(models.Model):
    slug = models.SlugField(unique=True)

    # English
    title_en = models.CharField(max_length=200, blank=True)
    subtitle_en = models.CharField(max_length=300, blank=True)
    body_en = models.TextField(blank=True)
    seo_title_en = models.CharField(max_length=255, blank=True)
    seo_description_en = models.CharField(max_length=255, blank=True)
    
    # Ukrainian
    title_uk = models.CharField(max_length=200, blank=True)
    subtitle_uk = models.CharField(max_length=300, blank=True)
    body_uk = models.TextField(blank=True)
    seo_title_uk = models.CharField(max_length=255, blank=True)
    seo_description_uk = models.CharField(max_length=255, blank=True)
    
    # Russian
    title_ru = models.CharField(max_length=200, blank=True)
    subtitle_ru = models.CharField(max_length=300, blank=True)
    body_ru = models.TextField(blank=True)
    seo_title_ru = models.CharField(max_length=255, blank=True)
    seo_description_ru = models.CharField(max_length=255, blank=True)

    is_published = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["slug"]

    def __str__(self):
        return f"{self.slug} - {self.title_en}"


class SectionImage(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="sections/%Y/%m/")

    alt_en = models.CharField(max_length=200, blank=True)
    alt_uk = models.CharField(max_length=200, blank=True)
    alt_ru = models.CharField(max_length=200, blank=True)

    sort = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort", "id"]

    def __str__(self):
        return f"{self.section.slug} #{self.id}"


class SectionArticle(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="articles")

    # English
    title_en = models.CharField(max_length=200, blank=True)
    subtitle_en = models.CharField(max_length=500, blank=True)
    text_en = models.TextField(blank=True)
    seo_title_en = models.CharField(max_length=255, blank=True)
    seo_description_en = models.CharField(max_length=255, blank=True)
    
    # Ukrainian
    title_uk = models.CharField(max_length=200, blank=True)
    subtitle_uk = models.CharField(max_length=500, blank=True)
    text_uk = models.TextField(blank=True)
    seo_title_uk = models.CharField(max_length=255, blank=True)
    seo_description_uk = models.CharField(max_length=255, blank=True)
    
    # Russian
    title_ru = models.CharField(max_length=200, blank=True)
    subtitle_ru = models.CharField(max_length=500, blank=True)
    text_ru = models.TextField(blank=True)
    seo_title_ru = models.CharField(max_length=255, blank=True)
    seo_description_ru = models.CharField(max_length=255, blank=True)

    is_published = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["sort", "id"]

    def __str__(self):
        return f"{self.section.slug} - {self.title_en}"


class SectionArticleImage(models.Model):
    article = models.ForeignKey(SectionArticle, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="section_articles/%Y/%m/")

    alt_en = models.CharField(max_length=200, blank=True)
    alt_uk = models.CharField(max_length=200, blank=True)
    alt_ru = models.CharField(max_length=200, blank=True)

    sort = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort", "id"]

    def __str__(self):
        return f"{self.article.title} #{self.id}"
    
class Contacts(models.Model):
    # English
    title_en = models.CharField(max_length=200, blank=True)
    text_en = models.TextField(blank=True)
    address_en = models.CharField(max_length=300, blank=True)
    
    # Ukrainian
    title_uk = models.CharField(max_length=200, blank=True)
    text_uk = models.TextField(blank=True)
    address_uk = models.CharField(max_length=300, blank=True)
    
    # Russian
    title_ru = models.CharField(max_length=200, blank=True)
    text_ru = models.TextField(blank=True)
    address_ru = models.CharField(max_length=300, blank=True)
    
    phone1 = models.CharField(max_length=20, blank=True)
    phone2 = models.CharField(max_length=20, blank=True)
    phone3 = models.CharField(max_length=20, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.title