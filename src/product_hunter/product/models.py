from django.db import models
from django.contrib.auth.models import User


class product(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    url = models.TextField()
    image = models.ImageField(upload_to="../static/static_img/uploads")
    icon = models.ImageField(upload_to="../static/static_img/uploads_icons")
    votes = models.IntegerField(default=1)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[0:max]

    def pub_date_awsome(self):
        return self.pub_date.strftime('%b %e')

    

    

    