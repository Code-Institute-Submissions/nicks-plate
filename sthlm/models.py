from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Meal(models.Model):
    todays_meal = models.CharField(max_length=50)
    description = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.todays_meal


class Environment(models.Model):
    environment_title = models.CharField(max_length=50)
    description = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.environment_title


class Staff(models.Model):
    staff_title = models.CharField(max_length=50)
    description = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.staff_title


class Policy(models.Model):
    policy_title = models.CharField(max_length=50)
    description = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.policy_title


