# middleware.py
from django.shortcuts import redirect
from django.urls import reverse

class RestrictAuthenticatedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # List of URLs to restrict for authenticated users
        restricted_urls = [
            reverse('login'),  # Replace with any other URLs you want to restrict
        ]

        if request.user.is_authenticated and request.path in restricted_urls:
            return redirect('request_list')  # Redirect authenticated users to the homepage

        return self.get_response(request)
