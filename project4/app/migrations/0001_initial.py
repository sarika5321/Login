# Generated by Django 5.0.4 on 2024-05-02 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('pno', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('un', models.CharField(max_length=50)),
                ('pw', models.CharField(max_length=50)),
            ],
        ),
    ]
