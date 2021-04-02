"""User views"""

# Django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from users.models import Profile
# Forms
from users.forms import ProfileForm


# Create your views here.

@login_required
def update_profile(request):
    """Update a user's profile view."""
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()

            return redirect('update_profile')

    else:
        form = ProfileForm()

    return render(
        request=request,
        template_name='users/update_profile.html',
        context={
            'profile': profile,
            'user': request.user,
            'form': form
        }
    )

def login_view(request):
    """Login view"""

    if request.method == 'POST':
        #print('*'*10)
        username = request.POST['username']
        password = request.POST['password']
        #print(username,password)
        #print('*'*10)
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('feed')           

        else:
            # Return an 'invalid login' error message.
            return render(request,'users/login.html',{'error':'Invalid username or password'})
    return render(request,'users/login.html')

@login_required
def logout_view(request):
    logout(request)
    # Redirect to a success page
    return redirect('login')           


def signup_view(request):
    '''Signup view'''

    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST.get('password', True)
        password_confirm = request.POST.get('password_confirm', True)

        
        # PASSWORD VALIDATION
        if password != password_confirm:
            error = 'The passwords do not match.'
            return render(request, 'users/signup.html', {'error': error})
        
        # EMAIL VALIDATION
        u = User.objects.filter(email=email)
        if u:
            error = f'There is another account using {email}'
            return render(request, 'users/signup.html', {'error': error})
        
        # USERNAME VALIDATION 
        try:
            user = User.objects.create_user(username=username, password=password)
            user.email = email
            user.save()

            profile = Profile(user=user)
            profile.save()

            login(request, user)
            return redirect('feed') # CAMBIAR >> Redireccionar a completar perfil
        except IntegrityError as ie:
            error = f'There is another account using {usermame}'
            return render(request, 'users/signup.html', {'error': error})

    return render(request, 'users/signup.html')