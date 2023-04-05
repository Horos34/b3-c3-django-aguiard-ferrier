from django import forms
from resavia.models import Reservation

class ConnexionForm(forms.Form):
    email = forms.CharField(max_length=63, label='Email')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['nom', 'prenom', 'date_reservation', 'heure_reservation', 'niveau_pilote', 'commentaire']
        widgets = {
            'date_reservation': forms.TextInput(attrs={'type': 'date'}),
            'heure_reservation': forms.TextInput(attrs={'type': 'time'})
        }