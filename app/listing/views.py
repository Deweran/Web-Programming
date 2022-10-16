from django.shortcuts import render, redirect
from .models import Listing
from .forms import Listing_Form

# Create your views here.
# CRUD - create, retrieve(detail), update, delete, (list(out))

def listing_list(request):
    listings = Listing.objects.all()
    context = {
        'listings': listings
    }
    return render(request, 'listing/listings.html', context)

def listing_retrieve(request, pk):  # view detail
    retrieve = Listing.objects.get(id=pk)
    context = {
        'retrieve': retrieve
    }
    return render(request, "listing/retrieve.html", context)

def listing_create(request):
    form = Listing_Form()

    if request.method == 'POST':
        form = Listing_Form(request.POST)
        # print(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listing/")

    context = {
        'form': form
    }
    return render(request, 'listing/create.html', context)

def listing_update(request, pk):
    listing = Listing.objects.get(id=pk)
    form = Listing_Form(instance=listing)

    if request.method == 'POST':
        form = Listing_Form(request.POST, instance=listing)
        # print(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {
        'form': form
    }
    return render(request, 'listing/update.html', context)

def listing_delete(request, pk):
    listing = Listing.objects.get(id=pk)
    listing.delete()
    return redirect('/')