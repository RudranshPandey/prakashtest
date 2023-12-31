# Generated by Django 4.2.1 on 2023-06-19 15:42

from django.db import migrations, models
import shortuuid.main


class Migration(migrations.Migration):

    dependencies = [
        ('volunteers', '0008_alter_volunteer_profiles_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer_profiles',
            name='id',
            field=models.CharField(default=shortuuid.main.ShortUUID.uuid, editable=False, max_length=22, primary_key=True, serialize=False),
        ),
    ]
