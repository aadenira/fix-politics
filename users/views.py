from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm, ProfileForm
from .models import Profile

# Create your views here.


def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display blank registration form.
        form = UserCreationForm()
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect to home page.
            login(request, new_user)
            return redirect('users:update')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'registration/register.html', context)


@login_required
def show_profile(request):
    user = request.user
    location = user.profile.location
    impacts = user.profile.impacts.all()
       
    context = {'user': user, 
               'location': location, 
                'impacts': impacts}
    return render(request, 'registration/profile.html', context)


@login_required
@transaction.atomic
def update_profile(request):

    if request.method != 'POST':
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    else:
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            if user.profile.critera.exists():
                user.profile.criteria.location = request.user.location
                selected = user.profile.impacts.all()
                for impact in Impact.objects.all():
                    if impact in selected:
                        user.profile.impacts.add(impact)
                    else:
                        user.profile.impacts.remove(impact)

            else:
                cr = Criteria(location=user.profile.location)
                cr.save()
                for impact in user.profile.impacts.all():
                    cr.impacts.add(impact)
                user.profile.criteria = cr

            return redirect('fixpol:index')


    context = { 'user_form': user_form,
                'profile_form': profile_form}

    return render(request, 'registration/update.html', context)



