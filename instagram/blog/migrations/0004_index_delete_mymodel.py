# Generated by Django 4.2.3 on 2023-07-24 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('isim', models.CharField(max_length=25)),
                ('soyisim', models.CharField(max_length=35)),
                ('email', models.CharField(max_length=100)),
                ('calistigibirim', models.CharField(max_length=45)),
                ('maas', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='MyModel',
        ),
    ]
