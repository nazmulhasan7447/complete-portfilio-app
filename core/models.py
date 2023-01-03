from django.db import models


class homePageInfo(models.Model):
    coverImg = models.ImageField(upload_to='home_page')
    headline = models.TextField(blank=True, null=True)
    additionalInfo = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=255)
    linkedIn = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email + ' || ' + self.linkedIn + ' || ' + self.instagram