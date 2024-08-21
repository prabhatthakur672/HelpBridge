from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.db.models import Q


@login_required
def request_list(request):
    if request.user.is_authenticated:
        # Display all unfulfilled requests or fulfilled requests created by the user
        help_request = HelpRequest.objects.filter(Q(user=request.user) | Q(is_fulfilled=False)).order_by('-created_at')

        
    else:
        # If the user is not authenticated, only show unfulfilled requests
        help_request = HelpRequest.objects.filter(is_fulfilled=False).order_by('-created_at')
    
    if request.method=="POST":
        searched_data = request.POST.get('search-box')
        if request.user.is_authenticated:
        # For authenticated users, show their requests or unfulfilled requests matching the search
            help_request = HelpRequest.objects.filter(
                (Q(user=request.user) | Q(is_fulfilled=False)), 
                title__icontains=searched_data
            ).order_by('-created_at')
        else:
            # For anonymous users, only show unfulfilled requests matching the search
            help_request = HelpRequest.objects.filter(
                is_fulfilled=False, 
                title__icontains=searched_data
            ).order_by('-created_at')


    profile = Profile.objects.get(user=request.user)

    # Get the logged-in user's notifications
    notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
    return render(request, "request_list.html", {'data':help_request, 'profile':profile, 'notifications': notifications})

@login_required
def create_request(request):
    if request.method == "POST":
        form = HelpRequestform(request.POST, request.FILES)
        if form.is_valid():
            helprequest = form.save(commit=False)
            helprequest.user = request.user
            helprequest.save()


            # Create notifications for all users except the one who created the request
            users = User.objects.exclude(id=request.user.id)
            for user in users:
                Notification.objects.create(
                    user=user,
                    content=f"New help request created: {helprequest.title}",
                )
            return redirect("request_list")
        
    else:
        form = HelpRequestform()
    return render(request, "request_form.html", {'form':form})    
    
@login_required
def edit_request(request, req_id):
    helprequest = get_object_or_404(HelpRequest, pk=req_id, user=request.user) 
    if request.method == "POST":
        form = HelpRequestform(request.POST, request.FILES, instance=helprequest)
        if form.is_valid():
            helprequest = form.save(commit=False)
            helprequest.user = request.user
            helprequest.save()
            return redirect("request_list")
        
    else:
        form = HelpRequestform(instance=helprequest)
    return render(request, "request_form.html", {'form':form}) 

@login_required
def delete_request(request, req_id):
    helprequest = get_object_or_404(HelpRequest, pk=req_id, user=request.user) 
    if request.method=="POST":
        helprequest.delete()
        return redirect('request_list')
    return render(request, "request_delete_form.html")



def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('request_list')
    else:
        form = UserRegistrationForm()

    return render(request, "registration/register.html", {'form':form})    



@login_required
def offer_help(request, req_id):
    helprequest = get_object_or_404(HelpRequest, pk = req_id)
    if request.method == "POST":
        form = HelpOfferForm(request.POST)
        if form.is_valid():
            help_offer = form.save(commit=False)
            help_offer.user = request.user           
            help_offer.request = helprequest
            help_offer.id = req_id
            help_offer.save()

            if help_offer.accepted:
                # Update the HelpRequest's is_fulfilled field
                helprequest.is_fulfilled = True
                helprequest.save()
            return redirect('request_list')
    else:
        form = HelpOfferForm()

    return render(request, "offer_help.html", {'form':form, 'data': helprequest})

@login_required
def offer_help_details(request, req_id):
    help_offer_detail = get_object_or_404(HelpOffer, pk=req_id)
    return render(request, "request_fulfill.html", {'details': help_offer_detail})

@login_required
def user_profile(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    profile, created = Profile.objects.get_or_create(user=user)
    return render(request, "user_profile.html", {'user':user, 'profile':profile})




def notifications(request):
    notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'notifications.html', {'notifications': notifications})


def mark_notification_as_read(request, notification_id):
    notification = get_object_or_404(Notification, pk=notification_id)

    # Ensure the notification belongs to the current user
    if notification.user != request.user:
        return redirect('notifications')  # or handle unauthorized access

    # Mark the notification as read
    notification.is_read = True
    notification.save()

    # Find the associated help request (if needed) and update request history
    help_request = notification.content.split("New help request created: ")[-1]  # Extract request title
    help_request_obj = get_object_or_404(HelpRequest, title=help_request)

    # Log the request status in history
    RequestHistory.objects.create(
        request=help_request_obj,
        status_change='Notification read',
        timestamp=notification.created_at
    )

    return redirect('notifications')


def request_history(request, request_id):
    help_request = get_object_or_404(HelpRequest, id=request_id)
    
    # Track the view
    if request.user.is_authenticated:
        RequestView.objects.get_or_create(user=request.user, request=help_request)
    
    # Get the history related to this HelpRequest
    history = RequestHistory.objects.filter(request=help_request).order_by('-timestamp')

    # Count the number of users who have viewed this request
    
    return render(request, 'request_history.html', {
        'help_request': help_request,
        'history': history,
        'view_count': len(history)
    })


def aboutUs(request):
    return render(request,"about.html")

def contactUs(request):
    return render(request,"contact.html")








