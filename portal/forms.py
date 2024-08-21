from .models import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class HelpRequestform(forms.ModelForm):
    class Meta:
        model = HelpRequest
        fields = ['title', 'description', 'image']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control my-custom-class',
                'placeholder': 'Enter the title of your request',
                'style': 'background-color: #2b2b2b; color: #c2f9bb; border-color: #4CAF50;',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control my-custom-class',
                'placeholder': 'Describe your request',
                'rows': 4,
                'style': 'background-color: #2b2b2b; color: #c2f9bb; border-color: #4CAF50;',
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control my-custom-class',
                'style': 'background-color: #2b2b2b; color: #c2f9bb; border-color: #4CAF50;',
            }),
        }


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your email',
        'style': 'background-color: #333; color: #eee;',
    }))
    
    profile_image = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={
        'class': 'form-control',
        'style': 'background-color: #333; color: #eee;',
    }))

    phone_no = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your phone number',
        'style': 'background-color: #333; color: #eee;',
    }))

    bio = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your bio',
        'style': 'background-color: #333; color: #eee;',
    }), required=False)

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        print("Email:", user.email)
        print("Profile Image:", self.cleaned_data['profile_image'])
        print("Phone No:", self.cleaned_data['phone_no'])
        print("Bio:", self.cleaned_data['bio'])
        
        
        user.save()
        
        # Get or create the profile instance
        profile, created = Profile.objects.get_or_create(user=user)
        print(f"Profile created: {created}")
        
        # Set the profile fields
        profile.profile_image = self.cleaned_data.get('profile_image')
        profile.phone_no = self.cleaned_data.get('phone_no')
        profile.bio = self.cleaned_data.get('bio')

        # Save the profile
        profile.save()
        print("Profile saved:", profile)

        
        return user
    

class HelpOfferForm(forms.ModelForm):
    class Meta:
        model = HelpOffer
        fields = ['message', 'accepted']
        widgets = {
            'message': forms.Textarea(attrs={
                'class': 'form-control my-custom-class bg-dark text-white',
                'placeholder': 'Enter your message here',
                'rows': 4,
            }),
            'accepted': forms.CheckboxInput(attrs={
                'class': 'form-check-input my-custom-class bg-dark text-white',
                
            }),
        }
