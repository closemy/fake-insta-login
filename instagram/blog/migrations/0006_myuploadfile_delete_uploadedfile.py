# Generated by Django 4.2.3 on 2023-08-10 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_myfilemodel_uploadedfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='myuploadfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=255)),
                ('myfiles', models.FileField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='UploadedFile',
        ),
    ]