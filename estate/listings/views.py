from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test

from django.urls import reverse
from django.conf import settings

from paypal.standard.forms import PayPalPaymentsForm

import uuid

from .models import House, PlotOfLand
from .forms import HouseForm, PlotOfLandForm
from users.models import UserAccount
    
def search(request):
    
    if request.method=='POST':
        seeked = request.POST['seeked'].capitalize()
        founded_estate = {}
        if House.objects.filter(title=seeked):
            founded_estate =  House.objects.filter(title=seeked)
        elif PlotOfLand.objects.filter(title=seeked):
            founded_estate = PlotOfLand.objects.filter(title=seeked)
        return render(request, 'estate/search.html', {
            'founded_estate': founded_estate,
        })
    else:
        return HttpResponseRedirect('/')

@login_required
def create_house(request):

    form = HouseForm
    user = request.user
    if request.method=='GET':
        return render(request, 'listings/create_house.html', {
            'form': form,
            'user': user
        })
    elif request.method=='POST':
        inputed = form(request.POST)
        if inputed.is_valid():
            inputed.save()

        return HttpResponseRedirect('/')
    return HttpResponse('Not available command')

@login_required
def create_plot_of_land(request):

    form = PlotOfLandForm
    user = request.user
    if request.method=='GET':
        return render(request, 'listings/create_plot_of_land.html', {
            'form': form,
            'user': user
        })
    elif request.method=='POST':
        inputed = form(request.POST)
        if inputed.is_valid():
            inputed.save()

        return HttpResponseRedirect('/')
    return HttpResponse('Not available command')


@login_required    
def update(request, slug):

    '''you can deal with two forms from two teplates in one view. However you weren't need a form in
    update part in main template'''
    try:
        estate = get_object_or_404(House, slug=slug)
        if request.method=='POST':
    
            form = HouseForm(request.POST, instance=estate)
            if form.is_valid():
                form.save()
            return HttpResponseRedirect('/')
        else:
    
            form = HouseForm(instance=estate)
            return render(request, 'listings/update.html', {
            'estate': estate,
            'form': form
        })
    except:
        estate = get_object_or_404(PlotOfLand, slug=slug)
        if request.method=='POST':
    
            form = PlotOfLandForm(request.POST, instance=estate)
            if form.is_valid():
                form.save()
            return HttpResponseRedirect('/')
            
        else:
        
            form = PlotOfLandForm(instance=estate)
            return render(request, 'listings/update.html', {
                'estate': estate,
                'form': form
            })

def delete(request):

    plot_id = request.POST['plot_id']
    house_id = request.POST['house_id']
    if plot_id:
        id = plot_id
    else:
        id = house_id
    try:
        estate = get_object_or_404(House, id=id)
    except:
        estate = get_object_or_404(PlotOfLand, id=id)

    estate.delete()
    return HttpResponseRedirect('/')

def dashboard(request):

    houses = House.objects.all()
    plots = PlotOfLand.objects.all()
    return render(request, 'listings/dashboard.html', {
        'houses': houses,
        'plots': plots,
    })
    

def estates_list(request):

    houses = House.objects.all()
    plots = PlotOfLand.objects.all()
    user = request.user
    return render(request, 'listings/estates_list.html', {
        'houses': houses,
        'plots': plots,
        'user': user
    })

def estate_view(request, slug):

    try:
        estate = get_object_or_404(House, slug=slug)
    except:
        estate = get_object_or_404(PlotOfLand, slug=slug)

    estate_realtor = UserAccount.objects.using('users').get(email=estate.realtor)

    if request.user.is_authenticated:
        if estate_realtor==request.user:
            owner = True
            return render(request, 'listings/estate_view.html', {
                'owner': owner,
                'estate': estate,
                'realtor': estate_realtor
            })
        else:
            owner = False
            return render(request, 'listings/estate_view.html', {
                'owner': owner,
                'estate': estate,
                'realtor': estate_realtor
            })
    else:
        return HttpResponseRedirect('/login')


def payment(request):
    
    estate_slug = request.POST['estate_slug']
    try:
        estate = get_object_or_404(House, slug=estate_slug)
    except:
        estate = get_object_or_404(PlotOfLand, slug=estate_slug)
    host = request.get_host()
    paypal_dict = {
        'buisness': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': estate.price,
        'item_name': 'Estate Order',
        'invoice': str(uuid.uuid4()),
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
        'success_url': 'http://{}{}'.format(host, reverse('payment_success')),
        'cancel_return': 'http://{}{}'.format(host, reverse('payment_failed')),
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    if request.user.is_authenticated:
        return render(request, 'listings/payment.html', {
            'form': form,
        })
    else:
        return HttpResponseRedirect('/accounts/login/')

def payment_success(request):
    return render(request, 'listings/payment_success.html')

def payment_failed(request):
    return render(request, 'listings/payment_failed.html')
