from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import datetime
from django import forms

class Utilisateur(models.Model):
  id = models.IntegerField(auto_created=True)
  nom = models.CharField(max_length=255)
  email = models.EmailField(max_length=255)
  mdp = forms.PasswordInput()
  tel = PhoneNumberField(region="FR")
  date_naissance = datetime.date() # à alimenter pour création date
  permis = models.BooleanField(default=False)
  
  
class Voiture(models.Model):
  id = models.IntegerField(auto_created=True)
  YEAR_CHOICES = [(r,r) for r in range(1900, datetime.date.today().year+1)]
  V4 = "V4"
  V6 = "V6"
  V8 = "V8"
  V10 = "V10"
  V12 = "V12"
  BREAK = "Break"
  COUPE = "Coupé"
  CABRIOLE = "Cabriolé"
  SPORT = "Sport"
  DECA = "Décapotable"
  VERSION_CHOICES = [
      (BREAK, "Break"),
      (COUPE, "Coupé"),
      (CABRIOLE, "Cabriolé"),
      (SPORT, "Sport"),
      (DECA, "Décapotable"),
  ]
  CYLINDRE_CHOICES = [
      (V4, "V4"),
      (V6, "V6"),
      (V8, "V8"),
      (V10, "V10"),
      (V12, "V12"),
  ]
  marque = models.CharField(max_length=100)
  modele = models.CharField(max_length=200)
  annee_construction = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year - 40)
  cynlidre = models.CharField(max_length=3, choices=CYLINDRE_CHOICES, default=V4)
  version = models.CharField(max_length=50 ,choices=VERSION_CHOICES, null=True)
  
class Circuit:
  id = models.IntegerField(auto_created=True)
  nom = models.CharField(max_length=255)
  lieu = models.CharField(max_length=255)
  longueur = models.FloatField()
  
class Reservation:
  id = models.IntegerField(auto_created=True)
  nom = models.CharField(max_length=255)
  numResa = models.CharField(max_length=10, auto_created=True)
  dateResa = datetime.datetime() #à alimenter avec le formulaire
  circuit = models.CharField(max_length=255) #Liste de circuit
  nombrePers = models.IntegerField(default=1)
  voiture = models.CharField(max_length=255)
  resaAcceptee = models.BooleanField(default=None)
  