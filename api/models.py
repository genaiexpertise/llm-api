from django.db import models

# Create your models here.


class SummarizeText(models.Model):
    text = models.TextField()
    summary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text