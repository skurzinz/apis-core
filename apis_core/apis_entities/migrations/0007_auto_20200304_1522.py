# Generated by Django 2.1.9 on 2020-03-04 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis_vocabularies', '0004_auto_20191115_1224'),
        ('apis_entities', '0006_auto_20200203_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='passage',
            name='kind_new',
            field=models.ManyToManyField(blank=True, related_name='passage_set_new', to='apis_vocabularies.PassageType'),
        ),
        migrations.AddField(
            model_name='publication',
            name='kind_new',
            field=models.ManyToManyField(blank=True, related_name='publication_set_new', to='apis_vocabularies.PassageType'),
        ),
    ]