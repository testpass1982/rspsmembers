from django.db import models

# Create your models here.
class Region(models.Model):
    title = models.CharField(max_length=100)
    has_division = models.BooleanField()

    def __str__(self):
        return self.title

class RspsDiv(models.Model):
    title = models.CharField(max_length=200)
    region = models.ForeignKey(Region)
    telephone = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.title

class RspsMember(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    job = models.CharField(max_length=100)
    is_a_leader = models.BooleanField()
    rsps_div = models.ForeignKey(RspsDiv)
    education = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return u'%s %s %s' %(self.first_name, self.middle_name, self.last_name)

