# Generated by Django 4.0.6 on 2022-07-26 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_comments_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.regions'),
        ),
    ]
