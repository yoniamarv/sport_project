from django import forms
from session_app.models import Selection

class SelectionForm(forms.ModelForm):
	class Meta:
		model = Selection
		fields = ['nbre_person_a', 'nbre_person_z','lieu', 'niveau', 'age_search']
		widgets = {
			'nbre_person_a': forms.TextInput(attrs={
				'id': 'selection-nbre_person_a',
				'placeholder': 'Nombre de personnes veulent etre inscrites',
				'required': True
				}),
			'nbre_person_z': forms.TextInput(attrs={
				'id': 'selection-nbre_person_z',
				'placeholder': 'Nombre de personnes deja inscrites',
				'required': True
				}),
			'lieu': forms.TextInput(attrs={
				'id': 'selection-lieu',
				'placeholder': 'lieu du match',
				'required': True
				}),
			'niveau': forms.TextInput(attrs={
				'id': 'selection-niveau',
				'placeholder': 'Niveau du joueur',
				'required': True
				}),
			'age_search': forms.TextInput(attrs={
				'id': 'selection-age_search',
				'placeholder': 'Age du joueur',
				'required': True
				}),
			# 'date': forms.(attrs={
			# 	'id': 'selection-date',
			# 	'placeholder': 'Date de reservation',
			# 	'required': False
			# 	}),

		}