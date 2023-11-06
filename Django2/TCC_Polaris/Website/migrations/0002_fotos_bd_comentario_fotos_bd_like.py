# Generated by Django 4.2.7 on 2023-11-06 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotos_bd',
            name='comentario',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Website.comentarios_bd'),
        ),
        migrations.AddField(
            model_name='fotos_bd',
            name='like',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Website.like_bd'),
        ),
    ]
