from django.shortcuts import render, get_object_or_404,redirect
from .models import Truck, Material, WeighbridgeTicket
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from reportlab.pdfgen import canvas
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def truck_list(request):
    trucks = Truck.objects.all()
    return render(request, 'truck_list.html', {'trucks': trucks})

def add_truck(request):
    return render(request, 'add_truck.html')


def truck_detail(request, pk):
    truck = get_object_or_404(Truck, pk=pk)
    ticket = get_object_or_404(WeighbridgeTicket, truck=truck)  # Adjust as needed
    return render(request, 'truck_detail.html', {'truck': truck, 'ticket': ticket})

def weighbridge_ticket(request):
    return render(request, 'ticket_list.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login.html')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('success.html')  # Redirect to the home page or another page
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')  # Redirect to the login page or another page

def material_list(request):
    materials = Material.objects.all()
    return render(request, 'material_list.html', {'materials': materials})

def ticket_list(request):
    tickets = WeighbridgeTicket.objects.all()
    return render(request, 'ticket_list.html', {'tickets': tickets})

def ticket_detail(request, pk):
    ticket = get_object_or_404(WeighbridgeTicket, pk=pk)
    return render(request, 'ticket_detail.html', {'ticket': ticket})

def download_ticket(request, pk):
    ticket = get_object_or_404(WeighbridgeTicket, pk=pk)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="ticket_{ticket.id}.pdf"'

    p = canvas.Canvas(response)
    p.setFont("Helvetica", 12)

    # Title
    p.drawString(100, 800, "Weighbridge Ticket")

    # Company Name
    p.drawString(100, 780, f"Company: {ticket.truck.company_name}")

    # Vehicle Number
    p.drawString(100, 760, f"Vehicle Number: {ticket.truck.vehicle_number}")

    # Date and Time
    p.drawString(100, 740, f"Date and Time: {ticket.date_time}")

    # Footer
    p.drawString(100, 720, "Thank you for using our service!")

    p.showPage()
    p.save()
    return response

