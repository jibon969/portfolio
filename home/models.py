from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save
from .utils import blog_unique_slug_generator


class BlogBanner(models.Model):
    title = models.CharField(max_length=120, blank=True, null=True, help_text='Banner title')
    largeDevices = models.ImageField(upload_to='blog/', null=True, blank=True, help_text="1400x400")
    mediumDevices = models.ImageField(upload_to='blog/', null=True, blank=True, help_text="800X400")
    smallDevices = models.ImageField(upload_to='blog/', null=True, blank=True, help_text="600x400")
    url_field = models.URLField(max_length=120, null=True, blank=True)
    value = models.IntegerField(null=True, blank=True, verbose_name="Position")
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']


class Blog(models.Model):
    title = models.CharField(max_length=120, blank=True, null=True)
    image = models.ImageField(upload_to="blog/", blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True, max_length=50)
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    publish = models.DateTimeField(default=timezone.now)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-publish',)


def blog_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = blog_unique_slug_generator(instance)


pre_save.connect(blog_pre_save_receiver, sender=Blog)


class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField(blank=True, null=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approve = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)


