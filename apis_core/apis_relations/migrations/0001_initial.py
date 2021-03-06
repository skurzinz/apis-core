# Generated by Django 2.1.12 on 2020-01-21 12:27

import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apis_entities', '0001_initial'),
        ('apis_metainfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventEvent',
            fields=[
                ('tempentityclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_metainfo.TempEntityClass')),
            ],
            options={
                'abstract': False,
            },
            bases=('apis_metainfo.tempentityclass',),
            managers=[
                ('annotation_links', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='EventWork',
            fields=[
                ('tempentityclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_metainfo.TempEntityClass')),
            ],
            options={
                'abstract': False,
            },
            bases=('apis_metainfo.tempentityclass',),
            managers=[
                ('annotation_links', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='InstitutionEvent',
            fields=[
                ('tempentityclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_metainfo.TempEntityClass')),
            ],
            options={
                'abstract': False,
            },
            bases=('apis_metainfo.tempentityclass',),
            managers=[
                ('annotation_links', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='InstitutionInstitution',
            fields=[
                ('tempentityclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_metainfo.TempEntityClass')),
            ],
            options={
                'abstract': False,
            },
            bases=('apis_metainfo.tempentityclass',),
            managers=[
                ('annotation_links', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='InstitutionPlace',
            fields=[
                ('tempentityclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_metainfo.TempEntityClass')),
            ],
            options={
                'abstract': False,
            },
            bases=('apis_metainfo.tempentityclass',),
            managers=[
                ('annotation_links', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='InstitutionWork',
            fields=[
                ('tempentityclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_metainfo.TempEntityClass')),
            ],
            options={
                'abstract': False,
            },
            bases=('apis_metainfo.tempentityclass',),
            managers=[
                ('annotation_links', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='PersonEvent',
            fields=[
                ('tempentityclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_metainfo.TempEntityClass')),
            ],
            options={
                'abstract': False,
            },
            bases=('apis_metainfo.tempentityclass',),
            managers=[
                ('annotation_links', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='PersonInstitution',
            fields=[
                ('tempentityclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_metainfo.TempEntityClass')),
            ],
            options={
                'abstract': False,
            },
            bases=('apis_metainfo.tempentityclass',),
            managers=[
                ('annotation_links', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='PersonPerson',
            fields=[
                ('tempentityclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_metainfo.TempEntityClass')),
            ],
            options={
                'abstract': False,
            },
            bases=('apis_metainfo.tempentityclass',),
            managers=[
                ('annotation_links', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='PersonPlace',
            fields=[
                ('tempentityclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_metainfo.TempEntityClass')),
            ],
            options={
                'abstract': False,
            },
            bases=('apis_metainfo.tempentityclass',),
            managers=[
                ('annotation_links', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='PersonWork',
            fields=[
                ('tempentityclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_metainfo.TempEntityClass')),
            ],
            options={
                'abstract': False,
            },
            bases=('apis_metainfo.tempentityclass',),
            managers=[
                ('annotation_links', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='PlaceEvent',
            fields=[
                ('tempentityclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_metainfo.TempEntityClass')),
            ],
            options={
                'abstract': False,
            },
            bases=('apis_metainfo.tempentityclass',),
            managers=[
                ('annotation_links', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='PlacePlace',
            fields=[
                ('tempentityclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_metainfo.TempEntityClass')),
            ],
            options={
                'abstract': False,
            },
            bases=('apis_metainfo.tempentityclass',),
            managers=[
                ('annotation_links', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='PlaceWork',
            fields=[
                ('tempentityclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_metainfo.TempEntityClass')),
            ],
            options={
                'abstract': False,
            },
            bases=('apis_metainfo.tempentityclass',),
            managers=[
                ('annotation_links', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='WorkWork',
            fields=[
                ('tempentityclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_metainfo.TempEntityClass')),
                ('related_workA', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_workB', to='apis_entities.Work')),
                ('related_workB', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_workA', to='apis_entities.Work')),
            ],
            options={
                'abstract': False,
            },
            bases=('apis_metainfo.tempentityclass',),
            managers=[
                ('annotation_links', django.db.models.manager.Manager()),
            ],
        ),
    ]
