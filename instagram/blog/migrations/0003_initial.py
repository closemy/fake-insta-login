# Generated by Django 4.2.3 on 2023-07-24 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0002_delete_mymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=25)),
                ('soyisim', models.CharField(max_length=35)),
                ('email', models.CharField(max_length=100)),
                ('calistigibirim', models.CharField(max_length=45)),
                ('maas', models.IntegerField()),
            ],
        ),
    ]
