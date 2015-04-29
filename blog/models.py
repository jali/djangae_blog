from django.db import models

# Create your models here.

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.text import slugify
from djangae.fields import RelatedSetField


class Entry(models.Model):
	owner = models.ForeignKey('djangae.GaeDatastoreUser')
	title = models.CharField(max_length=200)
	body = models.TextField()
	slug = models.SlugField(max_length=200, unique=True)
	created = models.DateTimeField(auto_now_add=True)
	tags = models.CharField(max_length=50)

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("entry-detail", kwargs={"slug": self.slug})


	class Meta:
		verbose_name = "Blog Entry"
		verbose_name_plural = "Blog Entries"
		ordering = ["-created"]


	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		super(Entry, self).save(*args, **kwargs)
