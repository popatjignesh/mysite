from django.db import models
from django.utils import timezone


class Post(models.Model):

	post_type = (
			('article', 'Article'),
			('blog', 'Blog'), 
			('question', 'Question'),
		)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	post_type = models.CharField(choices=post_type, max_length=10, null=True, blank=True)
	is_active = models.BooleanField(default=True)

	class Meta:
		verbose_name = "Post"
		verbose_name_plural = "Posts"

	def __str__(self):
		return self.title


class Comment(models.Model):
	post = models.ForeignKey(Post)
	text = models.TextField(null=True, blank=True, help_text="Post comment")

	class Meta:
		verbose_name = "Comment"
		verbose_name_plural = "Comments"

	def __str__(self):
		return self.post.title + '-' + self.text[:10]
