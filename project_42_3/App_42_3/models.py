from django.db import models

class About(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_pics/')
    email = models.EmailField()

    def __str__(self):
        return f'About {self.name}'

class PortfolioItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField()
    image = models.ImageField(upload_to='portfolio_images/')

    def __str__(self):
        return self.title
