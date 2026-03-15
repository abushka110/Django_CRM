from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Count
from django.utils.translation import gettext as _
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Map state codes (stored in the database) to full state names for display purposes
STATE_DICT = dict(Record.STATE_CHOICES)

# Home view: shows all records and handles login form submission
def home(request):
    records = Record.objects.all()

    if request.method == "POST":
        # Handle login
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, _("Successfully logged in!"))
            return redirect('home')
        else:
            messages.error(request, _("Username or Password is incorrect! Please try again."))
            return redirect('home')
    else:
        # Render homepage with list of records
        return render(request, 'home.html', {'records': records})

# Logout view: logs out the user and redirects to home
def logout_user(request):
    logout(request)
    messages.success(request, _("You have been successfully logged out!"))
    return redirect('home')

# Registration view: handles user signup
def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Save user and log them in automatically
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, _("You have successfully registered!"))
            return redirect('home')
    else:
        # Display empty registration form
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

# Add a new customer record
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, _("Record Added successfully!"))
                return redirect('home')
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.error(request, _("You must be logged in!"))
        return redirect('home')

# View details of a specific customer record by primary key (id)
def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.error(request, _("You must be logged in!"))
        return redirect('home')

# Delete a customer record
def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_record = Record.objects.get(id=pk)
        delete_record.delete()
        messages.success(request, _("Record has been deleted!"))
        return redirect('home')
    else:
        messages.error(request, _("You must be logged in!"))
        return redirect('home')

# Update an existing customer record
def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, _("Record has been Updated successfully!"))
            return redirect('record', pk=current_record.id)
        return render(request, 'update_record.html', {
            'form': form,
            'current_record': current_record
        })
    else:
        messages.error(request, _("You must be logged in!"))
        return redirect('home')

# Dashboard view: shows overview statistics
def dashboard(request):
    if request.user.is_authenticated:
        total_customers = Record.objects.count()

        # Customers grouped by state (top 3 only)
        customers_by_state = (
            Record.objects.values('state')
            .annotate(total=Count('state'))
            .order_by('-total')
        )
        customers_by_state_full = [{'state': STATE_DICT.get(s['state'], s['state']), 'total': s['total']} for s in customers_by_state]
        customers_by_state_top3 = customers_by_state_full[:3]

        # Top email domains
        emails = Record.objects.values_list('email', flat=True)
        domains = [email.split('@')[1] for email in emails if email and '@' in email]
        domain_counts = {}
        for d in domains:
            domain_counts[d] = domain_counts.get(d, 0) + 1
        domain_counts_top5 = sorted(domain_counts.items(), key=lambda x: x[1], reverse=True)[:5]

        # Top first names
        first_name_counts = (
            Record.objects.values('first_name')
            .annotate(total=Count('first_name'))
            .order_by('-total')
        )[:5]

        # Top last names
        last_name_counts = (
            Record.objects.values('last_name')
            .annotate(total=Count('last_name'))
            .order_by('-total')
        )[:5]

        # Top cities
        city_counts = (
            Record.objects.values('city')
            .annotate(total=Count('city'))
            .order_by('-total')
        )[:5]

        context = {
            "total_customers": total_customers,
            "customers_by_state": customers_by_state_top3,
            "domain_counts": domain_counts_top5,
            "first_name_counts": first_name_counts,
            "last_name_counts": last_name_counts,
            "city_counts": city_counts
        }
        return render(request, "dashboard.html", context)
    else:
        messages.error(request, _("You must be logged in!"))
        return redirect('home')

# Full state statistics view
def full_state_stats(request):
    if request.user.is_authenticated:
        customers_by_state = (
            Record.objects.values('state')
            .annotate(total=Count('state'))
            .order_by('-total')
        )
        customers_by_state_full = [
            {'state': STATE_DICT.get(s['state'], s['state']), 'total': s['total']}
            for s in customers_by_state
        ]
        return render(request, "full_state_stats.html", {"customers_by_state": customers_by_state_full})
    else:
        messages.error(request, _("You must be logged in!"))
        return redirect('home')

# Full email domain statistics
def full_email_stats(request):
    if request.user.is_authenticated:
        emails = Record.objects.values_list('email', flat=True)
        domains = [email.split('@')[1] for email in emails if email and '@' in email]
        domain_counts = {}
        for d in domains:
            domain_counts[d] = domain_counts.get(d, 0) + 1

        domain_counts_full = sorted(
            [{'domain': domain, 'total': count} for domain, count in domain_counts.items()],
            key=lambda x: x['total'],
            reverse=True
        )
        return render(request, "full_email_stats.html", {"domain_counts": domain_counts_full})
    else:
        messages.error(request, _("You must be logged in!"))
        return redirect('home')

# Full first name statistics
def full_first_name_stats(request):
    if request.user.is_authenticated:
        stats = Record.objects.values('first_name').annotate(total=Count('first_name')).order_by('-total')
        return render(request, "full_first_name_stats.html", {"stats": stats})
    else:
        messages.error(request, _("You must be logged in!"))
        return redirect('home')

# Full last name statistics
def full_last_name_stats(request):
    if request.user.is_authenticated:
        stats = Record.objects.values('last_name').annotate(total=Count('last_name')).order_by('-total')
        return render(request, "full_last_name_stats.html", {"stats": stats})
    else:
        messages.error(request, _("You must be logged in!"))
        return redirect('home')

# Full city statistics
def full_city_stats(request):
    if request.user.is_authenticated:
        stats = Record.objects.values('city').annotate(total=Count('city')).order_by('-total')
        return render(request, "full_city_stats.html", {"stats": stats})
    else:
        messages.error(request, _("You must be logged in!"))
        return redirect('home')