from __future__ import unicode_literals

from django.db import models

class PartCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        if self.parent:
            return str(self.parent) + "/" + self.name
        else:
            return self.name
        
class Part(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True)
    IPN = models.CharField(max_length=100, blank=True)
    category = models.ForeignKey(PartCategory, on_delete=models.CASCADE)
    
    def __str__(self):
        if self.IPN:
            return "{name} ({ipn})".format(
                ipn = self.IPN,
                name = self.name)
        else:
            return self.name