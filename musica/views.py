from django.shortcuts import render
from .forms import FiltreGroupeForm
from .models import Groupe, Ville, Departement, Pays
import re

def ListGroup(request):

	listenoms=set()
	for groupe in Groupe.objects.all():
		listenoms.add(groupe.nom)
	listenoms=list(listenoms)
	listenoms.sort()
	print('----------')
	print(listenoms)

	groupe_list=Groupe.objects.all()
	print(groupe_list)
	if request.GET:
		filtreform=FiltreGroupeForm(request.GET)
		print('------------')
		print(request.GET)
		
		if 'nom' in request.GET and request.GET['nom']!='':
			groupe_list=groupe_list.filter(nom__contains=request.GET['nom'])
		
		if 'styles' in request.GET and request.GET.getlist('styles'):
			groupe_list=groupe_list.filter(styles__in=request.GET.getlist('styles'))
		if 'bal' in request.GET:
			groupe_list=groupe_list.filter(bal=True)
		
		if 'lieux' in request.GET and request.GET['lieux']!='':
			lieu=request.GET['lieux']
			
			match=re.search(r'^([^\(]*?) \(([^\)]*?)\)', lieu)
			if match:
				nom=match.group(1)
				par=match.group(2)
				
				
				
				
				
				if len(Ville.objects.filter(nom_fr=nom, departement__numero=par))>0:
					villedep=villedep=Ville.objects.filter(nom_fr=nom, departement__numero=par)
					groupe_list=groupe_list.filter(lieux__content_object__in=villedep)
				elif len(Ville.objects.filter(nom_fr=nom, pays__nom_fr=par))>0:
					villepays=Ville.objects.filter(nom_fr=nom, pays__nom_fr=par)
					groupe_list=groupe_list.filter(lieux__content_object__in=villepays)
				elif len(Departement.objects.filter(nom_fr=nom, pays__code=par))>0:
					deppays=Departement.objects.filter(nom_fr=nom, pays__code=par)
					#Filtrer si département ou ville.departement=deppays
					contlieu=deppays
			else:
				
				
				
				
				if len(Ville.objects.filter(nom_fr=lieu))>0:
					ville=Ville.objects.filter(nom_fr=lieu)
					groupe_list=groupe_list.filter(lieux__content_object__in=ville)
				elif len(Departement.objects.filter(nom_fr=lieu))>0:
					dep=Departement.objects.filter(nom_fr=lieu)
					#Filtrer si département ou ville.departement=deppays
					contlieu=dep
				elif len(Pays.objects.filter(nom_fr=lieu))>0:
					pays=Pays.objects.filter(nom_fr=lieu)
					#Filtrer si pays ou ville.pays ou departement.pays ou ville.departement.pays=deppays
					contlieu=pays
			
				
			
		
			
		
			
		
	else:
		filtreform=FiltreGroupeForm()
		
	
	print(groupe_list)
	return render(request, 'musica/liste_groupes.html', locals())
