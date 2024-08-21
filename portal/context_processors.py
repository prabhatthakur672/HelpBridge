# myapp/context_processors.py
from django.contrib.auth.models import User
from .models import Profile

def user_profile_context(request):
    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(user=request.user)
            return {
                'user_profile_image': profile.profile_image.url,
                'user_username': request.user.username,
            }
        except Profile.DoesNotExist:
            return {}
    return {}
