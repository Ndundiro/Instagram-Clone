# Generated by Django 2.2.6 on 2019-10-14 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Instagram', '0003_auto_20191013_0051'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='images'),
        ),
    ]