# Generated by Django 3.0.6 on 2020-05-13 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gea', '0003_auto_20200506_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antecedente',
            name='expediente_modificado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='expediente_modificado', to='gea.Expediente'),
        ),
    ]