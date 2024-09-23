from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test


from .models import House, PlotOfLand
from .forms import HouseForm, PlotOfLandForm
    
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
def update(request, pk):

    '''you can deal with two forms from two teplates in one view. However you weren't need a form in
    update part in main template'''
    try:
        estate = get_object_or_404(House, id=pk)
        if request.method=='POST':
    
            form = HouseForm(request.POST, instance=estate)
            if form.is_valid():
                form.save()
            return HttpResponseRedirect('/')
        else:
    
            form = HouseForm(instance=estate)
            return render(request, 'estate/update.html', {
            'estate': estate,
            'form': form
        })
    except:
        estate = get_object_or_404(PlotOfLand, id=pk)
        if request.method=='POST':
    
            form = PlotOfLandForm(request.POST, instance=estate)
            if form.is_valid():
                form.save()
            return HttpResponseRedirect('/')
            
        else:
        
            form = PlotOfLandForm(instance=estate)
            return render(request, 'estate/update.html', {
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

    if request.user.is_authenticated:
        if estate.add_by==request.user.manager:
            owner = True
            return render(request, 'listings/estate_view.html', {
                'owner': owner,
                'estate': estate
            })
        else:
            owner = False
            return render(request, 'listings/estate_view.html', {
                'owner': owner,
                'estate': estate
            })
    else:
        return HttpResponseRedirect('/login')


def payment(request):
    pass
