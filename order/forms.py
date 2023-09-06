from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
	DIVISION_CHOICES = (
		('Dhaka', 'Dhaka'),
		('Chattagram', 'Chattagram'),
		('Rajshahi', 'Rajshahi '),
	)

	DISCRICT_CHOICES = (
		('Dhaka', 'Dhaka'), 
		('Gazipur', 'Gazipur'),
		('Narayanganj', 'Narayanganj'),
	)


	division = forms.ChoiceField(choices=DIVISION_CHOICES)
	district =  forms.ChoiceField(choices=DISCRICT_CHOICES)
	class Meta:
		model = Order
		fields = ['name', 'email', 'phone', 'address', 'division', 'district', 'zip_code']
