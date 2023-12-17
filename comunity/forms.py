from django import forms
from .models import Trip, directions

class AnnouncementForm(forms.Form):
	content = forms.CharField(label="الرسالة")

class NewTripForm(forms.Form):
	direction = forms.ChoiceField(choices=directions, label="الوجهة")
	time = forms.TimeField(label="الوقت")
	address = forms.CharField(label="العنوان")
	notes = forms.CharField(label="ملاحظات")
	notes.required = False