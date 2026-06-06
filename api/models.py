from django.db import models
from django.utils.translation import gettext_lazy as _

LANGUAGES = [
    ('en', 'English'),
    ('uk', 'Ukrainian'),
    ('ru', 'Russian'),
]


class Service(models.Model):
    slug = models.SlugField(unique=True, verbose_name=_("Slug"))
    title_en = models.CharField(max_length=200, blank=True)
    subtitle_en = models.CharField(max_length=300, blank=True)
    body_en = models.TextField(blank=True)
    seo_title_en = models.CharField(max_length=255, blank=True)
    seo_description_en = models.CharField(max_length=255, blank=True)
    title_uk = models.CharField(max_length=200, blank=True)
    subtitle_uk = models.CharField(max_length=300, blank=True)
    body_uk = models.TextField(blank=True)
    seo_title_uk = models.CharField(max_length=255, blank=True)
    seo_description_uk = models.CharField(max_length=255, blank=True)
    title_ru = models.CharField(max_length=200, blank=True)
    subtitle_ru = models.CharField(max_length=300, blank=True)
    body_ru = models.TextField(blank=True)
    seo_title_ru = models.CharField(max_length=255, blank=True)
    seo_description_ru = models.CharField(max_length=255, blank=True)
    is_published = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["slug"]
        verbose_name = _("Послуга")
        verbose_name_plural = _("Послуги")

    def __str__(self):
        return f"{self.slug} – {self.title_en or self.title_uk}"


class ServiceImage(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="services/%Y/%m/")
    alt_en = models.CharField(max_length=200, blank=True)
    alt_uk = models.CharField(max_length=200, blank=True)
    alt_ru = models.CharField(max_length=200, blank=True)
    sort = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort", "id"]
        verbose_name = _("Зображення послуги")
        verbose_name_plural = _("Зображення послуг")

    def __str__(self):
        return f"{self.service.slug} image #{self.id}"


class ServiceArticle(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="articles")
    title_en = models.CharField(max_length=200, blank=True)
    subtitle_en = models.CharField(max_length=500, blank=True)
    text_en = models.TextField(blank=True)
    seo_title_en = models.CharField(max_length=255, blank=True)
    seo_description_en = models.CharField(max_length=255, blank=True)
    title_uk = models.CharField(max_length=200, blank=True)
    subtitle_uk = models.CharField(max_length=500, blank=True)
    text_uk = models.TextField(blank=True)
    seo_title_uk = models.CharField(max_length=255, blank=True)
    seo_description_uk = models.CharField(max_length=255, blank=True)
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
        verbose_name = _("Стаття послуги")
        verbose_name_plural = _("Статті послуг")

    def __str__(self):
        return f"{self.service.slug} – {self.title_en or self.title_uk}"


class ServiceArticleImage(models.Model):
    article = models.ForeignKey(ServiceArticle, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="service_articles/%Y/%m/")
    alt_en = models.CharField(max_length=200, blank=True)
    alt_uk = models.CharField(max_length=200, blank=True)
    alt_ru = models.CharField(max_length=200, blank=True)
    sort = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort", "id"]
        verbose_name = _("Зображення статті послуги")
        verbose_name_plural = _("Зображення статей послуг")

    def __str__(self):
        return f"Article image #{self.id}"


class Section(models.Model):
    slug = models.SlugField(unique=True)
    title_en = models.CharField(max_length=200, blank=True)
    subtitle_en = models.CharField(max_length=300, blank=True)
    body_en = models.TextField(blank=True)
    seo_title_en = models.CharField(max_length=255, blank=True)
    seo_description_en = models.CharField(max_length=255, blank=True)
    title_uk = models.CharField(max_length=200, blank=True)
    subtitle_uk = models.CharField(max_length=300, blank=True)
    body_uk = models.TextField(blank=True)
    seo_title_uk = models.CharField(max_length=255, blank=True)
    seo_description_uk = models.CharField(max_length=255, blank=True)
    title_ru = models.CharField(max_length=200, blank=True)
    subtitle_ru = models.CharField(max_length=300, blank=True)
    body_ru = models.TextField(blank=True)
    seo_title_ru = models.CharField(max_length=255, blank=True)
    seo_description_ru = models.CharField(max_length=255, blank=True)
    is_published = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["slug"]
        verbose_name = _("Розділ")
        verbose_name_plural = _("Розділи")

    def __str__(self):
        return f"{self.slug} – {self.title_en or self.title_uk}"


class SectionImage(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="sections/%Y/%m/")
    alt_en = models.CharField(max_length=200, blank=True)
    alt_uk = models.CharField(max_length=200, blank=True)
    alt_ru = models.CharField(max_length=200, blank=True)
    sort = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort", "id"]
        verbose_name = _("Зображення розділу")
        verbose_name_plural = _("Зображення розділів")

    def __str__(self):
        return f"{self.section.slug} image #{self.id}"


class SectionArticle(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="articles")
    title_en = models.CharField(max_length=200, blank=True)
    subtitle_en = models.CharField(max_length=500, blank=True)
    text_en = models.TextField(blank=True)
    seo_title_en = models.CharField(max_length=255, blank=True)
    seo_description_en = models.CharField(max_length=255, blank=True)
    title_uk = models.CharField(max_length=200, blank=True)
    subtitle_uk = models.CharField(max_length=500, blank=True)
    text_uk = models.TextField(blank=True)
    seo_title_uk = models.CharField(max_length=255, blank=True)
    seo_description_uk = models.CharField(max_length=255, blank=True)
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
        verbose_name = _("Стаття розділу")
        verbose_name_plural = _("Статті розділів")

    def __str__(self):
        return f"{self.section.slug} – {self.title_en or self.title_uk}"


class SectionArticleImage(models.Model):
    article = models.ForeignKey(SectionArticle, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="section_articles/%Y/%m/")
    alt_en = models.CharField(max_length=200, blank=True)
    alt_uk = models.CharField(max_length=200, blank=True)
    alt_ru = models.CharField(max_length=200, blank=True)
    sort = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort", "id"]
        verbose_name = _("Зображення статті розділу")
        verbose_name_plural = _("Зображення статей розділів")

    def __str__(self):
        return f"Section article image #{self.id}"


class Contacts(models.Model):
    title_en = models.CharField(max_length=200, blank=True)
    text_en = models.TextField(blank=True)
    address_en = models.CharField(max_length=300, blank=True)
    title_uk = models.CharField(max_length=200, blank=True)
    text_uk = models.TextField(blank=True)
    address_uk = models.CharField(max_length=300, blank=True)
    title_ru = models.CharField(max_length=200, blank=True)
    text_ru = models.TextField(blank=True)
    address_ru = models.CharField(max_length=300, blank=True)
    phone1 = models.CharField(max_length=20, blank=True)
    phone2 = models.CharField(max_length=20, blank=True)
    phone3 = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    telegram = models.CharField(max_length=100, blank=True, help_text="Username (without @) or full t.me link")
    viber = models.CharField(max_length=50, blank=True, help_text="Phone number in international format")
    whatsapp = models.CharField(max_length=50, blank=True, help_text="Phone number in international format")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Контакти")
        verbose_name_plural = _("Контакти")

    def __str__(self):
        return self.title_en or self.title_uk or "Контакти"


class BlogPost(models.Model):
    slug = models.SlugField(unique=True)
    cover_image = models.ImageField(upload_to="blog/%Y/%m/", blank=True, null=True)
    title_en = models.CharField(max_length=255, blank=True)
    subtitle_en = models.CharField(max_length=500, blank=True)
    body_en = models.TextField(blank=True)
    seo_title_en = models.CharField(max_length=255, blank=True)
    seo_description_en = models.CharField(max_length=255, blank=True)
    title_uk = models.CharField(max_length=255, blank=True)
    subtitle_uk = models.CharField(max_length=500, blank=True)
    body_uk = models.TextField(blank=True)
    seo_title_uk = models.CharField(max_length=255, blank=True)
    seo_description_uk = models.CharField(max_length=255, blank=True)
    title_ru = models.CharField(max_length=255, blank=True)
    subtitle_ru = models.CharField(max_length=500, blank=True)
    body_ru = models.TextField(blank=True)
    seo_title_ru = models.CharField(max_length=255, blank=True)
    seo_description_ru = models.CharField(max_length=255, blank=True)
    published_at = models.DateTimeField(null=True, blank=True)
    is_published = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-published_at"]
        verbose_name = _("Публікація")
        verbose_name_plural = _("Публікації")

    def __str__(self):
        return f"{self.slug} – {self.title_en or self.title_uk}"


class FAQ(models.Model):
    question_en = models.CharField(max_length=500, blank=True)
    answer_en = models.TextField(blank=True)
    question_uk = models.CharField(max_length=500, blank=True)
    answer_uk = models.TextField(blank=True)
    question_ru = models.CharField(max_length=500, blank=True)
    answer_ru = models.TextField(blank=True)
    category = models.CharField(max_length=100, blank=True)
    sort = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ["sort", "id"]
        verbose_name = _("Питання та відповідь")
        verbose_name_plural = _("Питання та відповіді")

    def __str__(self):
        return self.question_en or self.question_uk or f"FAQ #{self.id}"


class PricingPlan(models.Model):
    slug = models.SlugField(unique=True)
    name_en = models.CharField(max_length=200, blank=True)
    description_en = models.TextField(blank=True)
    features_en = models.TextField(blank=True, help_text="One feature per line")
    price_display_en = models.CharField(max_length=100, blank=True)
    name_uk = models.CharField(max_length=200, blank=True)
    description_uk = models.TextField(blank=True)
    features_uk = models.TextField(blank=True, help_text="One feature per line")
    price_display_uk = models.CharField(max_length=100, blank=True)
    name_ru = models.CharField(max_length=200, blank=True)
    description_ru = models.TextField(blank=True)
    features_ru = models.TextField(blank=True, help_text="One feature per line")
    price_display_ru = models.CharField(max_length=100, blank=True)
    sort = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ["sort"]
        verbose_name = _("Тарифний план")
        verbose_name_plural = _("Тарифні плани")

    def __str__(self):
        return f"{self.slug} – {self.name_en or self.name_uk}"


class ConsultationRequest(models.Model):
    CONTACT_METHOD_CHOICES = [
        ('phone', 'Phone'),
        ('email', 'Email'),
        ('telegram', 'Telegram'),
        ('viber', 'Viber'),
        ('whatsapp', 'WhatsApp'),
    ]
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    contact_method = models.CharField(max_length=20, choices=CONTACT_METHOD_CHOICES, default='phone')
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = _("Заявка на консультацію")
        verbose_name_plural = _("Заявки на консультацію")

    def __str__(self):
        ts = self.created_at.strftime('%Y-%m-%d %H:%M') if self.created_at else ''
        return f"{self.name} ({self.contact_method}) – {ts}"
