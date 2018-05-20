from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType



class Album(models.Model):
	
	catwikimedia=models.CharField(max_length=255, verbose_name='nom de la categoria Wikimedia')
		
	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')
	

	def __str__(self):
		return self.catwikimedia


class APhotos(models.Model):
	album = GenericRelation(Album, content_type_field="content_type", object_id_field="object_id", on_delete=models.SET_NULL, null=True, blank=True)  
	
    
	class Meta:
		abstract = True


class Pays(models.Model):
	code=models.CharField(max_length=10, verbose_name='còdi')
	nom_oc=models.CharField(max_length=255, verbose_name='nom occitan')
	nom_fr=models.CharField(max_length=255, verbose_name='nom français')

	def __str__(self):
		return self.nom_fr



class Departement(models.Model):
	numero=models.IntegerField(verbose_name='còdi')
	nom_oc=models.CharField(max_length=255, verbose_name='nom occitan', null=True, blank=True)
	nom_fr=models.CharField(max_length=255, verbose_name='nom français')
	pays = models.ForeignKey(Pays, on_delete=models.PROTECT, verbose_name="país", null=True, blank=True)

	def __str__(self):
		return self.nom_fr+' ('+self.pays.code+')'



class Ville(models.Model):
	nom_oc=models.CharField(max_length=255, verbose_name='nom occitan', null=True, blank=True)
	nom_fr=models.CharField(max_length=255, verbose_name='nom français')
	identifiant=models.IntegerField(verbose_name="identificant")
	cp=models.IntegerField(verbose_name="còdi postal", null=True, blank=True)
	latitud=models.IntegerField(verbose_name="latitud", null=True, blank=True)
	longitud=models.IntegerField(verbose_name="longitud", null=True, blank=True)
	departement = models.ForeignKey(Departement, on_delete=models.PROTECT, verbose_name="departament", null=True, blank=True)
	pays = models.ForeignKey(Pays, on_delete=models.PROTECT, verbose_name="país", null=True, blank=True)

	def __str__(self):
		if self.departement:
			return self.nom_fr+' ('+str(self.departement.numero)+')'
		elif self.pays:
			return self.nom_fr+' ('+self.pays.nom_oc+')'
		else:
			return self.nom_fr



class Lieu(models.Model):
	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return str(self.content_object)



class Reseau(models.Model):
	nom=models.CharField(max_length=255, verbose_name='nom')
	image=models.ImageField(upload_to="reseaux/", verbose_name='icòna', null=True)

	def __str__(self):
		return self.nom


class Style(models.Model):
	nom_oc=models.CharField(max_length=255, verbose_name='nom occitan')

	def __str__(self):
		return self.nom_oc


class Instrument(APhotos):
	nom_oc=models.CharField(max_length=255, verbose_name='nom occitan')
	image=models.ImageField(upload_to="groupes/", verbose_name='fòto', null=True)

	def __str__(self):
		return self.nom_oc


class Support(models.Model):
	nom_oc=models.CharField(max_length=255, verbose_name='nom occitan')

	def __str__(self):
		return self.nom_oc


class Langue(models.Model):
	nom_oc=models.CharField(max_length=255, verbose_name='nom occitan')
	image=models.ImageField(upload_to="langues/", verbose_name='icòna', null=True)

	def __str__(self):
		return self.nom_oc


class Danse(APhotos):
	nom_oc=models.CharField(max_length=255, verbose_name='nom occitan')
	image=models.ImageField(upload_to="danses/", verbose_name='fòto', null=True, blank=True)

	def __str__(self):
		return self.nom_oc


class Fonction(models.Model):
	nom_oc=models.CharField(max_length=255, verbose_name='nom occitan')

	def __str__(self):
		return self.nom_oc	


class ReseauGroupe(models.Model):
	url=models.URLField(max_length=255, verbose_name='URL')
	reseau=models.ForeignKey(Reseau, on_delete=models.CASCADE)

	def __str__(self):
		return self.url


class ReseauMusicien(models.Model):
	url=models.URLField(max_length=255, verbose_name='URL')
	reseau=models.ForeignKey(Reseau, on_delete=models.CASCADE)

	def __str__(self):
		return "pagina {0} de {1}".format(self.reseau, self.musicien)


class ReseauFestival(models.Model):
	url=models.URLField(max_length=255, verbose_name='URL')
	reseau=models.ForeignKey(Reseau, on_delete=models.CASCADE)

	def __str__(self):
		return "pagina {0} de {1}".format(self.reseau, self.musicien)
	



class Groupe(APhotos):
	nom=models.CharField(max_length=255, verbose_name='nom')
	image=models.ImageField(upload_to="groupes/", verbose_name='fòto')
	present=models.TextField(max_length=1000, verbose_name='presentacion', null=True, blank=True)
	site=models.URLField(max_length=255, verbose_name='site', null=True, blank=True)
	reseaux = models.ManyToManyField(ReseauGroupe, related_name='reseaux_groupe', blank=True, verbose_name="malhums")
	styles = models.ManyToManyField(Style, related_name='styles_groupe', verbose_name="estiles", blank=True)
	bal = models.BooleanField(verbose_name="anima de bals")
	mail = models.EmailField(max_length=255, verbose_name='corric')
	mailvisible = models.BooleanField(verbose_name="corric visible per totes ?")
	telefone = models.CharField(max_length=255, verbose_name='telefòne', null=True, blank=True)
	telvisible = models.BooleanField(verbose_name="telefòne visible per totes ?")
	createdDate=models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="data de creacion")
	lastModifDate=models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="darrièra modificacion")
	lieux = models.ManyToManyField(Lieu, related_name='lieux_groupes', verbose_name="luòc(s)", blank=True)

	def __str__(self):
		return self.nom


class Musicien(APhotos):
	nom=models.CharField(max_length=255, verbose_name='nom')
	prenom=models.CharField(max_length=255, verbose_name='prenom')
	image=models.ImageField(upload_to="groupes/", verbose_name='fòto')
	present=models.TextField(max_length=1000, verbose_name='presentacion', null=True, blank=True)
	site=models.URLField(max_length=255, verbose_name='site', null=True, blank=True)
	reseaux = models.ManyToManyField(ReseauMusicien, related_name='reseaux_musicien', blank=True, verbose_name="malhums")
	styles = models.ManyToManyField(Style, related_name='styles_musicien', verbose_name="estiles")
	mail = models.EmailField(max_length=255, verbose_name='corric')
	mailvisible = models.BooleanField(verbose_name="corric visible per totes ?")
	telefòne = models.CharField(max_length=255, verbose_name='telefòne', null=True, blank=True)
	telvisible = models.BooleanField(verbose_name="telefòne visible per totes ?")
	
	instruments = models.ManyToManyField(Instrument, related_name='instruments_musicien', verbose_name="instruments jogats")
	createdDate=models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="data de creacion")
	lastModifDate=models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="darrièra modificacion")

	def __str__(self):
		return self.prenom+" "+self.nom


class Disque(models.Model):
	titre=models.CharField(max_length=255, verbose_name='títol')
	image=models.ImageField(upload_to="groupes/", verbose_name='cobèrta')
	groupes = models.ManyToManyField(Groupe, related_name='disques_groupe', verbose_name="grop(s)")
	musiciens = models.ManyToManyField(Musicien, related_name='disques_musicien', verbose_name="musicians", null=True, blank=True)
	instruments = models.ManyToManyField(Instrument, related_name='instruments_cd', verbose_name="instruments jogats", null=True, blank=True)
	annee = models.PositiveIntegerField(verbose_name="annada de parucion")
	dateParution=models.DateField(null=True, blank=True, verbose_name="data exacta de parucion")
	support = models.ForeignKey(Support, on_delete=models.PROTECT, verbose_name="supòrt")
	
	createdDate=models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="data de creacion")
	lastModifDate=models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="darrièra modificacion")

	def __str__(self):
		return self.titre



class Chanson(models.Model):
	titre=models.CharField(max_length=255, verbose_name='títol')
	paroles=models.TextField(max_length=5000, verbose_name='paraulas', null=True, blank=True)
	langues = models.ManyToManyField(Langue, related_name='langues_chanson', verbose_name="lenga(s)", blank=True)
	danse = models.ManyToManyField(Danse, related_name='danses_chanson', verbose_name="dança(s)", blank=True)

	def __str__(self):
		return self.titre
	




class Festival(APhotos):
	nom=models.CharField(max_length=255, verbose_name='nom')
	periode=models.CharField(max_length=255, verbose_name='periòde')
	lieux = models.ManyToManyField(Lieu, related_name='lieux_festivals', verbose_name="luòc(s)")
	site=models.URLField(max_length=255, verbose_name='site', null=True, blank=True)
	reseaux = models.ManyToManyField(ReseauFestival, related_name='reseaux_festival', blank=True, verbose_name="malhums")
	toujours=models.BooleanField(verbose_name="existís totjorn ?")

	def __str__(self):
		return self.nom
	
	
	
				

class GroupeMusicien(models.Model):
	toujours=models.BooleanField(verbose_name="totjorn present dins lo grop ?")
	groupe = models.ForeignKey(Groupe, related_name='musiciens_groupe', on_delete=models.CASCADE, verbose_name="grop")
	musicien = models.ForeignKey(Musicien, related_name='groupes_musicien', verbose_name="musician", on_delete=models.CASCADE)

	def __str__(self):
		return "{0} {1} sòci de {2}".format(self.musicien.prenom, self.musicien.nom, self.groupe.nom)
		

class GroupeChanson(models.Model):
	fonction=models.ForeignKey(Fonction, on_delete=models.PROTECT)
	chanson=models.ForeignKey(Chanson, on_delete=models.CASCADE, related_name='groupes_chanson', verbose_name="cançon")
	groupe=models.ForeignKey(Groupe, on_delete=models.CASCADE, related_name='chansons_groupe', verbose_name="grop")

	def __str__(self):
		return "{0} {1} de {2}".format(self.groupe.nom, self.fonction, self.chanson.titre)
		

class MusicienChanson(models.Model):
	fonction=models.ForeignKey(Fonction, on_delete=models.PROTECT)
	chanson=models.ForeignKey(Chanson, on_delete=models.CASCADE, related_name='musiciens_chanson', verbose_name="cançon")
	musicien=models.ForeignKey(Musicien, on_delete=models.CASCADE, related_name='chansons_musicien', verbose_name="musician")

	def __str__(self):
		return "{0} {1} {2} de {3}".format(self.musicien.prenom, self.musicien.nom, self.fonction, self.chanson.titre)
