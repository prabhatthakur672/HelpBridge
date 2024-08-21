from django.contrib.auth.models import User
from django.db import models

class HelpRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="photos/", blank = True, null = True)
    is_fulfilled = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    
class HelpOffer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request = models.ForeignKey(HelpRequest, on_delete=models.CASCADE)
    message = models.TextField()
    accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message[:25]

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class RequestHistory(models.Model):
    request = models.ForeignKey(HelpRequest, on_delete=models.CASCADE)
    status_change = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)


class RequestView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request = models.ForeignKey(HelpRequest, on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'request')  



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_images/', default='default.jpg')
    phone_no = models.CharField(max_length=15, blank=True)  # Changed to CharField for better phone number handling
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
        


