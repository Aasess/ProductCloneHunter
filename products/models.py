from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add = True)
    votes_total = models.IntegerField(default = 1)
    image = models.ImageField(upload_to = 'images/')
    icon = models.ImageField(upload_to = 'images/')
    body = models.TextField()
    usernameID = models.ForeignKey(User,on_delete = models.CASCADE)

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e,%Y')

    def summary(self):
        if(len(self.body)>=300):
            return f"{self.body[:300]}.........."
        else:
            return self.body