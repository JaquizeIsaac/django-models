from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Snack(models.Model):
    name = models.CharField(max_length=128)
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField()
    rating = models.IntegerField(default=1, choices=[(i, i) for i in range(1, 6)])
    reviewer = models.ForeignKey(get_user_model(), related_name='reviewer', on_delete=models.CASCADE, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.reviewer_id:
            default_reviewer = get_user_model().objects.get(username='Big Monkey')
            self.reviewer = default_reviewer
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name