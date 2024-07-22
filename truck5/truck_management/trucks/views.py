from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse
from trucks.models import Truck
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def weighbridge_ticket_view(request, vehicle_number):
    truck = get_object_or_404(Truck, vehicle_number=vehicle_number)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="ticket_{truck.vehicle_number}.pdf"'
    p = canvas.Canvas(response, pagesize=letter)
    p.drawString(100, 750, f"Company: {truck.company_name}")
    p.drawString(100, 725, f"Vehicle Number: {truck.vehicle_number}")
    p.showPage()
    p.save()
    return response

def home_view(request):
    return render(request, 'home.html')

