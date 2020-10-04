from ckeditor.fields import RichTextField
from django.db import models
# Create your models here.
from django.template.defaultfilters import slugify

from Job import settings


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(default=None, editable=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def job_count(self):
        return self.jobs.all().count()


class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=300)
    CHOICES = (
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('freelance', 'Freelance'),
        ('internship', 'Internship'),
        ('temporary', 'Temporary'),
    )

    job_type = models.CharField(max_length=20, blank=False, default=None, choices=CHOICES)
    location = models.CharField(max_length=200, blank=False, default=None)
    description = RichTextField(blank=False, default=None)
    publishing_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(default=None, editable=False)
    employer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    employee = models.ManyToManyField(settings.AUTH_USER_MODEL, default=None, blank=True, related_name="job_employee")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="jobs", default=None)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-id',)
