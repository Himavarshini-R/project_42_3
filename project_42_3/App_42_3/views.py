from django.shortcuts import render
from .models import About, PortfolioItem

def home(request):
    about = About.objects.first()  # Get the first entry, if any
    if not about:
        # Fallback if no About object exists
        about = {
            'name': 'Your Name',
            'bio': 'Bio not available yet.',
            'email': 'your.email@example.com',
            'profile_picture': 'default_profile_pic.jpg',  # Replace with a default image path
        }
    
    portfolio_items = PortfolioItem.objects.all()
    
    return render(request, 'home.html', {'about': about, 'portfolio_items': portfolio_items})



