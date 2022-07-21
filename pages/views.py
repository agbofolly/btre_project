from django.shortcuts import render
from django.http import HttpResponse
from btre_project.listings.views import listing
# Create your views here.
from listings.models import Listing

def  index(request):
    listings = Listing.order_by('-listing_date').filter(is_published=True)[:3]
    return render(request,'pages/index.html')

def about(request):
    return render(request,'pages/about.html')
    
