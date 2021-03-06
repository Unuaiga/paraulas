# Generated by Django 2.0 on 2018-04-07 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catwikimedia', models.CharField(max_length=255, verbose_name='nom de la categoria Wikimedia')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='Chanson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255, verbose_name='títol')),
                ('paroles', models.TextField(blank=True, max_length=5000, null=True, verbose_name='paraulas')),
                ('image', models.ImageField(upload_to='groupes/', verbose_name='cobèrta')),
            ],
        ),
        migrations.CreateModel(
            name='Danse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_oc', models.CharField(max_length=255, verbose_name='nom occitan')),
                ('image', models.ImageField(blank=True, null=True, upload_to='danses/', verbose_name='fòto')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(verbose_name='còdi')),
                ('nom_oc', models.CharField(blank=True, max_length=255, null=True, verbose_name='nom occitan')),
                ('nom_fr', models.CharField(max_length=255, verbose_name='nom français')),
            ],
        ),
        migrations.CreateModel(
            name='Disque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255, verbose_name='títol')),
                ('image', models.ImageField(upload_to='groupes/', verbose_name='cobèrta')),
                ('annee', models.PositiveIntegerField(verbose_name='annada de parucion')),
                ('dateParution', models.DateField(blank=True, null=True, verbose_name='data exacta de parucion')),
                ('createdDate', models.DateTimeField(auto_now_add=True, verbose_name='data de creacion')),
                ('lastModifDate', models.DateTimeField(auto_now=True, verbose_name='darrièra modificacion')),
            ],
        ),
        migrations.CreateModel(
            name='Festival',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255, verbose_name='nom')),
                ('periode', models.CharField(max_length=255, verbose_name='periòde')),
                ('site', models.URLField(blank=True, max_length=255, null=True, verbose_name='site')),
                ('toujours', models.BooleanField(verbose_name='existís totjorn ?')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Fonction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_oc', models.CharField(max_length=255, verbose_name='nom occitan')),
            ],
        ),
        migrations.CreateModel(
            name='Groupe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255, verbose_name='nom')),
                ('image', models.ImageField(upload_to='groupes/', verbose_name='fòto')),
                ('present', models.TextField(blank=True, max_length=1000, null=True, verbose_name='presentacion')),
                ('site', models.URLField(blank=True, max_length=255, null=True, verbose_name='site')),
                ('bal', models.BooleanField(verbose_name='anima de bals')),
                ('mail', models.EmailField(max_length=255, verbose_name='corric')),
                ('mailvisible', models.BooleanField(verbose_name='corric visible per totes ?')),
                ('telefone', models.CharField(blank=True, max_length=255, null=True, verbose_name='telefòne')),
                ('telvisible', models.BooleanField(verbose_name='telefòne visible per totes ?')),
                ('createdDate', models.DateTimeField(auto_now_add=True, verbose_name='data de creacion')),
                ('lastModifDate', models.DateTimeField(auto_now=True, verbose_name='darrièra modificacion')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GroupeChanson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chanson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musica.Chanson')),
                ('fonction', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='musica.Fonction')),
                ('groupe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musica.Groupe')),
            ],
        ),
        migrations.CreateModel(
            name='GroupeMusicien',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toujours', models.BooleanField(verbose_name='totjorn present dins lo grop ?')),
                ('groupe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musica.Groupe')),
            ],
        ),
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_oc', models.CharField(max_length=255, verbose_name='nom occitan')),
                ('image', models.ImageField(null=True, upload_to='groupes/', verbose_name='fòto')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Langue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_oc', models.CharField(max_length=255, verbose_name='nom occitan')),
                ('image', models.ImageField(null=True, upload_to='langues/', verbose_name='icòna')),
            ],
        ),
        migrations.CreateModel(
            name='Lieu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='Musicien',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255, verbose_name='nom')),
                ('prenom', models.CharField(max_length=255, verbose_name='prenom')),
                ('image', models.ImageField(upload_to='groupes/', verbose_name='fòto')),
                ('present', models.TextField(blank=True, max_length=1000, null=True, verbose_name='presentacion')),
                ('site', models.URLField(blank=True, max_length=255, null=True, verbose_name='site')),
                ('mail', models.EmailField(max_length=255, verbose_name='corric')),
                ('mailvisible', models.BooleanField(verbose_name='corric visible per totes ?')),
                ('telefòne', models.CharField(blank=True, max_length=255, null=True, verbose_name='telefòne')),
                ('telvisible', models.BooleanField(verbose_name='telefòne visible per totes ?')),
                ('createdDate', models.DateTimeField(auto_now_add=True, verbose_name='data de creacion')),
                ('lastModifDate', models.DateTimeField(auto_now=True, verbose_name='darrièra modificacion')),
                ('groupes', models.ManyToManyField(blank=True, related_name='groupes_musicien', through='musica.GroupeMusicien', to='musica.Groupe', verbose_name='grops')),
                ('instruments', models.ManyToManyField(related_name='instruments_musicien', to='musica.Instrument', verbose_name='instruments jogats')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MusicienChanson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chanson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musica.Chanson')),
                ('fonction', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='musica.Fonction')),
                ('musicien', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musica.Musicien')),
            ],
        ),
        migrations.CreateModel(
            name='Pays',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, verbose_name='còdi')),
                ('nom_oc', models.CharField(max_length=255, verbose_name='nom occitan')),
                ('nom_fr', models.CharField(max_length=255, verbose_name='nom français')),
            ],
        ),
        migrations.CreateModel(
            name='Reseau',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255, verbose_name='nom')),
                ('image', models.ImageField(null=True, upload_to='reseaux/', verbose_name='icòna')),
            ],
        ),
        migrations.CreateModel(
            name='ReseauFestival',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=255, verbose_name='URL')),
                ('reseau', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musica.Reseau')),
            ],
        ),
        migrations.CreateModel(
            name='ReseauGroupe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=255, verbose_name='URL')),
                ('reseau', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musica.Reseau')),
            ],
        ),
        migrations.CreateModel(
            name='ReseauMusicien',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=255, verbose_name='URL')),
                ('reseau', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musica.Reseau')),
            ],
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_oc', models.CharField(max_length=255, verbose_name='nom occitan')),
            ],
        ),
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_oc', models.CharField(max_length=255, verbose_name='nom occitan')),
            ],
        ),
        migrations.CreateModel(
            name='Ville',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_oc', models.CharField(blank=True, max_length=255, null=True, verbose_name='nom occitan')),
                ('nom_fr', models.CharField(max_length=255, verbose_name='nom français')),
                ('identifiant', models.IntegerField(verbose_name='identificant')),
                ('cp', models.IntegerField(blank=True, null=True, verbose_name='còdi postal')),
                ('latitud', models.IntegerField(blank=True, null=True, verbose_name='latitud')),
                ('longitud', models.IntegerField(blank=True, null=True, verbose_name='longitud')),
                ('departement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='musica.Departement', verbose_name='departament')),
                ('pays', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='musica.Pays', verbose_name='país')),
            ],
        ),
        migrations.AddField(
            model_name='musicien',
            name='reseaux',
            field=models.ManyToManyField(blank=True, related_name='reseaux_musicien', to='musica.ReseauMusicien', verbose_name='malhums'),
        ),
        migrations.AddField(
            model_name='musicien',
            name='styles',
            field=models.ManyToManyField(related_name='styles_musicien', to='musica.Style', verbose_name='estiles'),
        ),
        migrations.AddField(
            model_name='groupemusicien',
            name='musicien',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musica.Musicien'),
        ),
        migrations.AddField(
            model_name='groupe',
            name='lieux',
            field=models.ManyToManyField(related_name='lieux_groupes', to='musica.Lieu', verbose_name='luòc(s)'),
        ),
        migrations.AddField(
            model_name='groupe',
            name='reseaux',
            field=models.ManyToManyField(blank=True, related_name='reseaux_groupe', to='musica.ReseauGroupe', verbose_name='malhums'),
        ),
        migrations.AddField(
            model_name='groupe',
            name='styles',
            field=models.ManyToManyField(related_name='styles_groupe', to='musica.Style', verbose_name='estiles'),
        ),
        migrations.AddField(
            model_name='festival',
            name='lieux',
            field=models.ManyToManyField(related_name='lieux_festivals', to='musica.Lieu', verbose_name='luòc(s)'),
        ),
        migrations.AddField(
            model_name='festival',
            name='reseaux',
            field=models.ManyToManyField(blank=True, related_name='reseaux_festival', to='musica.ReseauFestival', verbose_name='malhums'),
        ),
        migrations.AddField(
            model_name='disque',
            name='groupes',
            field=models.ManyToManyField(related_name='groupes_cd', to='musica.Groupe', verbose_name='grop(s)'),
        ),
        migrations.AddField(
            model_name='disque',
            name='instruments',
            field=models.ManyToManyField(blank=True, null=True, related_name='instruments_cd', to='musica.Instrument', verbose_name='instruments jogats'),
        ),
        migrations.AddField(
            model_name='disque',
            name='musiciens',
            field=models.ManyToManyField(blank=True, null=True, related_name='musiciens_cd', to='musica.Musicien', verbose_name='musicians'),
        ),
        migrations.AddField(
            model_name='disque',
            name='support',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='musica.Support', verbose_name='supòrt'),
        ),
        migrations.AddField(
            model_name='departement',
            name='pays',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='musica.Pays', verbose_name='país'),
        ),
        migrations.AddField(
            model_name='chanson',
            name='danse',
            field=models.ManyToManyField(related_name='danses_chanson', to='musica.Danse', verbose_name='dança(s)'),
        ),
        migrations.AddField(
            model_name='chanson',
            name='groupes',
            field=models.ManyToManyField(blank=True, related_name='groupes_chanson', through='musica.GroupeChanson', to='musica.Groupe', verbose_name='grops intervenents'),
        ),
        migrations.AddField(
            model_name='chanson',
            name='langues',
            field=models.ManyToManyField(related_name='langues_chanson', to='musica.Langue', verbose_name='lenga(s)'),
        ),
        migrations.AddField(
            model_name='chanson',
            name='musiciens',
            field=models.ManyToManyField(blank=True, related_name='musiciens_chanson', through='musica.MusicienChanson', to='musica.Musicien', verbose_name='musicians intervenents'),
        ),
    ]
