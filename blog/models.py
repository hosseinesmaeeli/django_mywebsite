from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    image =models.ImageField(upload_to='blog/',default='blog/default.jpg')
    #'blog/' means in media folder we have blog file. we must make media folder
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    # use set_nll to set null for deleted posts
    # null=true means : can be empty
    
    title = models.CharField(max_length=255)
    content = models.TextField()
    # tags = 
    # category = 
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created_date']

    
    def __str__(self):
        return self.title

