# Generated by Django 2.1.9 on 2020-08-20 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apis_vocabularies', '0006_professiontype_temporary_field_for_workaround'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professiontype',
            name='vocabsbaseclass_ptr',
        ),
        migrations.DeleteModel(
            name='ProfessionType',
        ),
    ]