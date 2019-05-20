# Generated by Django 2.1.2 on 2019-04-18 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apis_metainfo', '0001_initial'),
        ('apis_vocabularies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('tempentityclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_metainfo.TempEntityClass')),
                ('kind', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='apis_vocabularies.EventType')),
            ],
            bases=('apis_metainfo.tempentityclass',),
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('tempentityclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_metainfo.TempEntityClass')),
                ('kind', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='apis_vocabularies.InstitutionType')),
            ],
            bases=('apis_metainfo.tempentityclass',),
        ),
        migrations.CreateModel(
            name='Passage',
            fields=[
                ('tempentityclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_metainfo.TempEntityClass')),
                ('topics', models.ManyToManyField(blank=True, null=True, to='apis_vocabularies.PassageTopics')),
            ],
            bases=('apis_metainfo.tempentityclass',),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('tempentityclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_metainfo.TempEntityClass')),
                ('first_name', models.CharField(blank=True, help_text='The persons´s forename. In case of more then one name...', max_length=255, null=True)),
                ('gender', models.CharField(blank=True, choices=[('female', 'female'), ('male', 'male')], max_length=15)),
                ('profession', models.ManyToManyField(blank=True, to='apis_vocabularies.ProfessionType')),
                ('title', models.ManyToManyField(blank=True, to='apis_vocabularies.Title')),
            ],
            bases=('apis_metainfo.tempentityclass',),
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('tempentityclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_metainfo.TempEntityClass')),
                ('lat', models.FloatField(blank=True, null=True, verbose_name='latitude')),
                ('lng', models.FloatField(blank=True, null=True, verbose_name='longitude')),
                ('kind', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='apis_vocabularies.PlaceType')),
            ],
            bases=('apis_metainfo.tempentityclass',),
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('tempentityclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_metainfo.TempEntityClass')),
                ('migne_number', models.CharField(blank=True, max_length=1024, null=True)),
                ('clavis_number', models.CharField(blank=True, max_length=1024, null=True)),
                ('publication_description', models.TextField(blank=True, null=True)),
                ('kind', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='apis_vocabularies.PassageType')),
                ('language', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='apis_vocabularies.PassageLanguage')),
            ],
            bases=('apis_metainfo.tempentityclass',),
        ),
    ]
