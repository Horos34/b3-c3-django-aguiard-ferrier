from django.shortcuts import render
from resavia.authentification import forms

def connexion_page(request):
    form = forms.ConnexionForm()
    if request.method == 'POST':
        form = forms.ConnexionForm(request.POST)
        if form.is_valid():
            pass
    return render(request, 'templates/connexion.html', context={'form': form})
