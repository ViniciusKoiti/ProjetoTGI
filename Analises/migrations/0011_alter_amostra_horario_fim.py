# Generated by Django 4.0.4 on 2022-07-26 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Analises', '0010_alter_amostra_horario_fim'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amostra',
            name='horario_fim',
            field=models.DateTimeField(),
        ),
    ]
