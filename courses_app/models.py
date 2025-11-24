from django.db import models





class course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    
    
    def __str__(self):
        return f"{self.title} - {self.description[:30]}"
      