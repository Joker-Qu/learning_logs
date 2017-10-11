from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# 用户学习的主题
class Topic(models.Model):
  text = models.CharField(max_length=200)
  date_added = models.DateTimeField(auto_now_add=True)
  owner = models.ForeignKey(User)
  def __str__(self):
    return self.text

# 某个主题的具体知识
class Entry(models.Model):
  topic = models.ForeignKey(Topic)
  text = models.TextField()
  date_added = models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name_plural = 'entries'
  def __str__(self):
    return self.text[:50]+'...'


