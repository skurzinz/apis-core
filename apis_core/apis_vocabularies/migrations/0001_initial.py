# Generated by Django 2.1.2 on 2019-06-14 10:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apis_metainfo', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='VocabNames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='VocabsBaseClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('description', models.TextField(blank=True, help_text='Brief description of the used term.')),
                ('status', models.CharField(choices=[('rej', 'rejected'), ('ac', 'accepted'), ('can', 'candidate'), ('del', 'deleted')], default='can', max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='VocabsUri',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uri', models.URLField()),
                ('domain', models.CharField(blank=True, max_length=255)),
                ('rdf_link', models.URLField(blank=True)),
                ('loaded', models.BooleanField(default=False)),
                ('loaded_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CollectionType',
            fields=[
                ('vocabsbaseclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_vocabularies.VocabsBaseClass')),
            ],
            bases=('apis_vocabularies.vocabsbaseclass',),
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('vocabsbaseclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_vocabularies.VocabsBaseClass')),
            ],
            bases=('apis_vocabularies.vocabsbaseclass',),
        ),
        migrations.CreateModel(
            name='InstitutionType',
            fields=[
                ('vocabsbaseclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_vocabularies.VocabsBaseClass')),
            ],
            bases=('apis_vocabularies.vocabsbaseclass',),
        ),
        migrations.CreateModel(
            name='LabelType',
            fields=[
                ('vocabsbaseclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_vocabularies.VocabsBaseClass')),
            ],
            bases=('apis_vocabularies.vocabsbaseclass',),
        ),
        migrations.CreateModel(
            name='PassageLanguage',
            fields=[
                ('vocabsbaseclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_vocabularies.VocabsBaseClass')),
            ],
            bases=('apis_vocabularies.vocabsbaseclass',),
        ),
        migrations.CreateModel(
            name='PassageTopics',
            fields=[
                ('vocabsbaseclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_vocabularies.VocabsBaseClass')),
            ],
            bases=('apis_vocabularies.vocabsbaseclass',),
        ),
        migrations.CreateModel(
            name='PassageType',
            fields=[
                ('vocabsbaseclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_vocabularies.VocabsBaseClass')),
            ],
            bases=('apis_vocabularies.vocabsbaseclass',),
        ),
        migrations.CreateModel(
            name='PlaceType',
            fields=[
                ('vocabsbaseclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_vocabularies.VocabsBaseClass')),
            ],
            bases=('apis_vocabularies.vocabsbaseclass',),
        ),
        migrations.CreateModel(
            name='ProfessionType',
            fields=[
                ('vocabsbaseclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_vocabularies.VocabsBaseClass')),
            ],
            bases=('apis_vocabularies.vocabsbaseclass',),
        ),
        migrations.CreateModel(
            name='RelationBaseClass',
            fields=[
                ('vocabsbaseclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_vocabularies.VocabsBaseClass')),
                ('name_reverse', models.CharField(blank=True, help_text='Inverse relation like: "is sub-class of" vs. "is super-class of".', max_length=255, verbose_name='Name reverse')),
            ],
            bases=('apis_vocabularies.vocabsbaseclass',),
        ),
        migrations.CreateModel(
            name='SundayRepresentations',
            fields=[
                ('vocabsbaseclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_vocabularies.VocabsBaseClass')),
            ],
            bases=('apis_vocabularies.vocabsbaseclass',),
        ),
        migrations.CreateModel(
            name='TextType',
            fields=[
                ('vocabsbaseclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_vocabularies.VocabsBaseClass')),
                ('entity', models.CharField(max_length=255)),
                ('collections', models.ManyToManyField(blank=True, to='apis_metainfo.Collection')),
            ],
            bases=('apis_vocabularies.vocabsbaseclass',),
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('vocabsbaseclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_vocabularies.VocabsBaseClass')),
                ('abbreviation', models.CharField(blank=True, max_length=10)),
            ],
            bases=('apis_vocabularies.vocabsbaseclass',),
        ),
        migrations.AddField(
            model_name='vocabsuri',
            name='vocab',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apis_vocabularies.VocabsBaseClass'),
        ),
        migrations.AddField(
            model_name='vocabsbaseclass',
            name='parent_class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apis_vocabularies.VocabsBaseClass'),
        ),
        migrations.AddField(
            model_name='vocabsbaseclass',
            name='userAdded',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='vocabsbaseclass',
            name='vocab_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='apis_vocabularies.VocabNames'),
        ),
        migrations.CreateModel(
            name='EventEventRelation',
            fields=[
                ('relationbaseclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_vocabularies.RelationBaseClass')),
            ],
            bases=('apis_vocabularies.relationbaseclass',),
        ),
        migrations.CreateModel(
            name='EventPassageRelation',
            fields=[
                ('relationbaseclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_vocabularies.RelationBaseClass')),
            ],
            bases=('apis_vocabularies.relationbaseclass',),
        ),
        migrations.CreateModel(
            name='EventPublicationRelation',
            fields=[
                ('relationbaseclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_vocabularies.RelationBaseClass')),
            ],
            bases=('apis_vocabularies.relationbaseclass',),
        ),
        migrations.CreateModel(
            name='InstitutionEventRelation',
            fields=[
                ('relationbaseclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_vocabularies.RelationBaseClass')),
            ],
            bases=('apis_vocabularies.relationbaseclass',),
        ),
        migrations.CreateModel(
            name='InstitutionInstitutionRelation',
            fields=[
                ('relationbaseclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_vocabularies.RelationBaseClass')),
            ],
            bases=('apis_vocabularies.relationbaseclass',),
        ),
        migrations.CreateModel(
            name='InstitutionPassageRelation',
            fields=[
                ('relationbaseclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_vocabularies.RelationBaseClass')),
            ],
            bases=('apis_vocabularies.relationbaseclass',),
        ),
        migrations.CreateModel(
            name='InstitutionPlaceRelation',
            fields=[
                ('relationbaseclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_vocabularies.RelationBaseClass')),
            ],
            bases=('apis_vocabularies.relationbaseclass',),
        ),
        migrations.CreateModel(
            name='InstitutionPublicationRelation',
            fields=[
                ('relationbaseclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_vocabularies.RelationBaseClass')),
            ],
            bases=('apis_vocabularies.relationbaseclass',),
        ),
        migrations.CreateModel(
            name='PassagePassageRelation',
            fields=[
                ('relationbaseclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_vocabularies.RelationBaseClass')),
            ],
            bases=('apis_vocabularies.relationbaseclass',),
        ),
        migrations.CreateModel(
            name='PassagePublicationRelation',
            fields=[
                ('relationbaseclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_vocabularies.RelationBaseClass')),
            ],
            bases=('apis_vocabularies.relationbaseclass',),
        ),
        migrations.CreateModel(
            name='PersonEventRelation',
            fields=[
                ('relationbaseclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_vocabularies.RelationBaseClass')),
            ],
            bases=('apis_vocabularies.relationbaseclass',),
        ),
        migrations.CreateModel(
            name='PersonInstitutionRelation',
            fields=[
                ('relationbaseclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_vocabularies.RelationBaseClass')),
            ],
            bases=('apis_vocabularies.relationbaseclass',),
        ),
        migrations.CreateModel(
            name='PersonPassageRelation',
            fields=[
                ('relationbaseclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_vocabularies.RelationBaseClass')),
            ],
            bases=('apis_vocabularies.relationbaseclass',),
        ),
        migrations.CreateModel(
            name='PersonPersonRelation',
            fields=[
                ('relationbaseclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_vocabularies.RelationBaseClass')),
            ],
            bases=('apis_vocabularies.relationbaseclass',),
        ),
        migrations.CreateModel(
            name='PersonPlaceRelation',
            fields=[
                ('relationbaseclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_vocabularies.RelationBaseClass')),
            ],
            bases=('apis_vocabularies.relationbaseclass',),
        ),
        migrations.CreateModel(
            name='PersonPublicationRelation',
            fields=[
                ('relationbaseclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_vocabularies.RelationBaseClass')),
            ],
            bases=('apis_vocabularies.relationbaseclass',),
        ),
        migrations.CreateModel(
            name='PlaceEventRelation',
            fields=[
                ('relationbaseclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_vocabularies.RelationBaseClass')),
            ],
            bases=('apis_vocabularies.relationbaseclass',),
        ),
        migrations.CreateModel(
            name='PlacePassageRelation',
            fields=[
                ('relationbaseclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_vocabularies.RelationBaseClass')),
            ],
            bases=('apis_vocabularies.relationbaseclass',),
        ),
        migrations.CreateModel(
            name='PlacePlaceRelation',
            fields=[
                ('relationbaseclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_vocabularies.RelationBaseClass')),
            ],
            bases=('apis_vocabularies.relationbaseclass',),
        ),
        migrations.CreateModel(
            name='PlacePublicationRelation',
            fields=[
                ('relationbaseclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_vocabularies.RelationBaseClass')),
            ],
            bases=('apis_vocabularies.relationbaseclass',),
        ),
        migrations.CreateModel(
            name='PublicationPublicationRelation',
            fields=[
                ('relationbaseclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_vocabularies.RelationBaseClass')),
            ],
            bases=('apis_vocabularies.relationbaseclass',),
        ),
    ]
