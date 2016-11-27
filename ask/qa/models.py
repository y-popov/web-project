from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class QuestionManager(models.Manager):
	def new():
		pass
	def popular():
		pass

class Question(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateField(auto_now_add=True)
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(User)
	likes = models.ManyToManyField(User)#, related_name="question_likes_user")
	objects = QuestionManager()

"""
class QuestionManager(models.Manager):
	def new():
		from django.db import connections
		cur = connections['ask_db'].cursor()
		return cur.execute('SELECT * FROM Question ORDER BY added_at DESC')
	def popular():
		from django.db import connections
		cur = connections['ask_db'].cursor()
		return cur.execute('SELECT * FROM Question ORDER BY rating')
"""

class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateField(auto_now_add=True)
	question = models.ForeignKey(Question)
	author = models.ForeignKey(User)
