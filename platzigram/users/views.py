"""User views"""

# Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


# Create your views here.

def login_view(request):
    """Login view"""

    if request.method == 'POST':
        print('*'*10)
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        print('*'*10)
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('feed')           

        else:
            # Return an 'invalid login' error message.
            return render(request,'users/login.html',{'error':'Invalid username or password'})
    return render(request,'users/login.html')
            