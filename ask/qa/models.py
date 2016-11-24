from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateField()
	rating = models.IntegerField()
	author = models.ForeignKey(User)
	likes = models.ManyToManyField(User)

class QuestionManager(models.Manager):
	def new():
		from django.db import connections
		cur = connections['ask_db'].cursor()
		return cur.execute('SELECT * FROM Question ORDER BY added_at DESC')
	def popular():
		from django.db import connections
		cur = connections['ask_db'].cursor()
		return cur.execute('SELECT * FROM Question ORDER BY rating')

class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateField()
	question = models.ForeignKey(Question)
	author = models.ForeignKey(User)
