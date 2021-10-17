from django.db import models

# Create your models here.

#schema for djangoClasses database model
class djangoClasses(models.Model):
    title = models.CharField(max_length=60, default="", blank=False, null=False)
    courseNum = models.IntegerField(blank=False, null=False)
    instructorName = models.CharField(max_length=60, default="", blank=False, null=False)
    duration = models.FloatField(default=0)

    objects = models.Manager()
# Allows the admin database to display the title of each djangoClass object instead of the generic "djangoClasses object()
    def __str__(self):
        return self.title
