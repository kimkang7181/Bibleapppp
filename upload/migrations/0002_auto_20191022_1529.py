# Generated by Django 2.0.13 on 2019-10-22 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='post',
        ),
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.FileField(default='', upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='File',
        ),
    ]
