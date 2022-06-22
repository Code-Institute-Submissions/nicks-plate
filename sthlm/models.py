from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Meal(models.Model):
    """ Chef adds meal """
    todays_meal = models.CharField(max_length=50)
    description = models.TextField()
    featured_image = CloudinaryField()
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.todays_meal


class Environment(models.Model):
    """ add esg uppdate """
    environment_title = models.CharField(max_length=50)
    description = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.environment_title


class Staff(models.Model):
    """ Staff gives input """
    staff_title = models.CharField(max_length=50)
    description = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.staff_title


class Policy(models.Model):
    """ gives the policy """
    policy_title = models.CharField(max_length=50)
    description = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.policy_title


