from django import forms
from .models import Groupe, Lieu
import floppyforms

class FiltreGroupeForm(forms.ModelForm):
	nom = forms.CharField(required=False)
	lieux = forms.CharField(required=False)
	

	class Meta:
		model = Groupe
		fields = ('nom','styles','bal', 'lieux')
		
		listegroupes=set()
		for groupe in Groupe.objects.all():
			listegroupes.add(groupe.nom)
		listegroupes=list(listegroupes)
		listegroupes.sort()
		
		listelieux=set()
		for lieu in Lieu.objects.all():
			listelieux.add(str(lieu.content_object))
		listelieux=list(listelieux)
		listelieux.sort()
				
		
		widgets = {
			'nom': floppyforms.widgets.Input(datalist=listegroupes),
			'styles': floppyforms.widgets.CheckboxSelectMultiple(),
			'lieux': floppyforms.widgets.Input(datalist=listelieux)
		}
