from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User



class Keyword(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __unicode__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __unicode__(self):
        return self.name

class Document(models.Model):
    
    CSV = "csv"
    TXT = "txt"
    
    DOCUMENT_TYPES = (
        ("CSV", CSV),
        ("TXT", TXT),
    )

    of_type = models.CharField(max_length=10, choices=DOCUMENT_TYPES)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.title

class Context(models.Model):
    document = models.ForeignKey(Document)
    keyword = models.ForeignKey(Keyword)
    position_from = models.IntegerField()
    position_to = models.IntegerField()
    text = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.text

class Review(models.Model):
    
    PENDING = "pending"
    APPROVED = "approved"
    
    STATUS_TYPES = (
        ("pending", PENDING),
        ("approved", APPROVED),
    )

    context = models.ForeignKey(Context)
    keyword = models.ForeignKey(Keyword)
    category = models.ForeignKey(Category)
    user = models.ForeignKey(User, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_TYPES)

    def __unicode__(self):
        return self.status
