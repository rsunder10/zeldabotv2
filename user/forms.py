from django.forms import ModelForm
from .models import Profile

class ProfileForm(ModelForm):
	class Meta:
		model=Profile
		fields = ['avatar','city','fav_food','relationship','preferrs']
