# Generated by Django 4.2.3 on 2023-11-25 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_rename_yüklediğikonu_accounts_yukledigikonu_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='veriler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kullaniciadi', models.CharField(max_length=30)),
                ('sifre', models.IntegerField()),
            ],
        ),
    ]
