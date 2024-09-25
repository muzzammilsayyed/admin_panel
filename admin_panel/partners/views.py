from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Partner
from .forms import PartnerForm



def home_view(request):
    return redirect('login')

@login_required
def dashboard(request):
    partners = Partner.objects.all()  # Fetch all partners
    context = {
        'partners_count': partners.count(),  # Count of partners
        'partners': partners,  # Pass partners to the template
    }
    return render(request, 'dashboard.html', context)


def partner_list(request):
    partners = Partner.objects.all()  # Fetch all partners
    query = request.GET.get('search')  # Get the search query from the URL
    if query:
        partners = Partner.objects.filter(name__icontains=query)  # Filter by name
    else:
        partners = Partner.objects.all()  # Fetch all partners if no search query

    context = {
        'partners': partners,  # Pass the filtered or full partner list to the template
        'search_query': query,  # Pass the search query back to the template to retain the value in the search box
    }
    
    return render(request, 'partners/partner_list.html', context)


def add_partner(request):
    if request.method == 'POST':
        form = PartnerForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('partner_list')  # Redirect to the partner list after submission
    else:
        form = PartnerForm()

    return render(request, 'partners/add_partner.html', {'form': form})


def partner_details(request, pk):
    partner = get_object_or_404(Partner, pk=pk)  # Retrieve partner by primary key (ID)
    return render(request, 'partners/partner_details.html', {'partner': partner})

def edit_partner(request, pk):
    partner = get_object_or_404(Partner, pk=pk)
    
    if request.method == 'POST':
        form = PartnerForm(request.POST, instance=partner)
        if form.is_valid():
            form.save()
            return redirect('partner_list')  # Redirect to the partner listing page
    else:
        form = PartnerForm(instance=partner)
    
    return render(request, 'partners/edit_partner.html', {'form': form, 'partner': partner})

