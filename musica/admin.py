from django.contrib import admin

from .models import Groupe, Musicien, Disque, Festival, Chanson, Album, Reseau, Style, Instrument, Support, Langue, Danse, Fonction, Lieu, ReseauGroupe, ReseauMusicien, ReseauFestival, GroupeMusicien, GroupeChanson, MusicienChanson, Ville, Departement, Pays


admin.site.register(Groupe)
admin.site.register(Musicien)
admin.site.register(Disque)
admin.site.register(Festival)
admin.site.register(Chanson)
admin.site.register(Instrument)
admin.site.register(Album)
admin.site.register(Reseau)
admin.site.register(Style)
admin.site.register(Support)
admin.site.register(Langue)
admin.site.register(Danse)
admin.site.register(Fonction)
admin.site.register(Ville)
admin.site.register(Departement)
admin.site.register(Pays)
admin.site.register(Lieu)
admin.site.register(ReseauGroupe)
admin.site.register(ReseauMusicien)
admin.site.register(ReseauFestival)
admin.site.register(GroupeMusicien)
admin.site.register(GroupeChanson)
admin.site.register(MusicienChanson)
