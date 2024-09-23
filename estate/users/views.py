from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect

from .forms import UserAccountForm

User = get_user_model()

def SignUP(request):

    if request.method=='POST':
        form = request.POST
        if form.is_valid():
            if form['is_realtor'] == True:
                
            login(request, user)
            manager = Manager.objects.create(name=user.username, by=user)
            manager.save()
        elif not form.is_valid():
            return render(request, 'book/sign_up.html', {
                'form': form
            })
        return HttpResponseRedirect('/')
    else:
        form = UserAccountForm
        return render(request, 'book/sign_up.html', {
            'form': form
        })
