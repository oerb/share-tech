# -*- coding: utf-8 -*-
__author__ = 'oerb'
from django import forms

"""
Forms
"""

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class LocationForm(forms.Form):
    """
    Form Class to Edit and Set Location
    """
    lc_name = forms.CharField(label="Name", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Locationname'}))
    lc_geo = forms.CharField(required=False, label="GEO", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Geo Location'}))
    lc_adr = forms.CharField(required=False, label="Adresse", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'PLZ'}))
    lc_city = forms.CharField(required=False, label="Ort", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}))
    lc_www = forms.CharField(required=False, label="WWW", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'www'}))
    lc_mail = forms.CharField(required=False, label="E-Mail",widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E-Mail'}))
    lc_info = forms.CharField(required=False, label="Info", widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Info'}))


class ItemForm(forms.Form):
    """
    Form Class to Edit and Add an Item to a User
    """
    it_name = forms.CharField(label="Name", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Item Name'}))
    it_info = forms.CharField(required=False, label="Info", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Item Info'}))
    it_storageinfo = forms.CharField(required=False, label="Lagerort", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Item Info'}))
    it_back_to_owner = forms.BooleanField(label="Zurück an Besitzer".decode('utf-8'), required=False)
    it_back_to_owner.widget.attrs['class'] = 'form-control'
    it_back_to_owner.widget.attrs['placeholder'] = 'back to owner'
    it_personal_handover = forms.BooleanField(label="Persöliche Übergabe".decode('utf-8'), required=False)
    it_personal_handover.widget.attrs['class'] = 'form-control'
    it_personal_handover.widget.attrs['placeholder'] = 'personal handover'


class UserForm(forms.Form):
    """
    Form for Edit and Add User
    """
    user_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    user_email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E-Mail'}))
    user_password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    user_password2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
