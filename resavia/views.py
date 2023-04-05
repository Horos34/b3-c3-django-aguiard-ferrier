from django.shortcuts import render, get_object_or_404, redirect
from resavia.authentification import forms
from .authentification.forms import ReservationForm
from .models import Reservation
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Reservation

def home(request):
    return render(request, 'base.html')

class ReservationListView(ListView):
    model = Reservation
    template_name = 'reservation_list.html'
    context_object_name = 'reservations'

class ReservationCreateView(CreateView):
    model = Reservation
    template_name = 'reservation_create.html'
    fields = ['nom', 'prenom', 'date_reservation', 'heure_reservation', 'voiture_souhaite', 'commentaire']
    success_url = reverse_lazy('reservation_list')

class ReservationDetailView(DetailView):
    model = Reservation
    template_name = 'reservation_detail.html'
    context_object_name = 'reservation'

class ReservationUpdateView(UpdateView):
    model = Reservation
    template_name = 'reservation_update.html'
    fields = ['nom', 'prenom', 'date_reservation', 'heure_reservation', 'voiture_souhaite', 'commentaire']
    context_object_name = 'reservation'

class ReservationDeleteView(DeleteView):
    model = Reservation
    template_name = 'reservation_delete.html'
    success_url = reverse_lazy('reservation_list')
    context_object_name = 'reservation'

def connexion_page(request):
    form = forms.ConnexionForm()
    if request.method == 'POST':
        form = forms.ConnexionForm(request.POST)
        if form.is_valid():
            pass
    return render(request, 'connexion.html', context={'form': form})



def home(request):
    return render(request, 'base.html')
def reservation_view(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('details', pk=form.instance.pk)
    else:
        form = ReservationForm()
    return render(request, 'reservation.html', {'form': form})

def details_view(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    return render(request, 'details_reservation.html.html', {'reservation': reservation})

def cancel_view(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == 'POST':
        reservation.delete()
        return redirect('home')
    return render(request, 'cancel.html', {'reservation': reservation})