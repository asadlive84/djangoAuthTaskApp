from django import forms
from django.contrib.auth.forms import UserCreationForm
from user.models import CustomUser
from django.contrib.auth.forms import AuthenticationForm

# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = CustomUser
		fields = ("email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user



