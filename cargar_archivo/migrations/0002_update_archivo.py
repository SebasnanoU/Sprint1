# Generated by Django 4.2 on 2023-04-26 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargar_archivo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='update_archivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archivo', models.FileField(upload_to='archivos/')),
            ],
        ),
    ]
