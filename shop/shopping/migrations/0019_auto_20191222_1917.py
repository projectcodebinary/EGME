# Generated by Django 3.0 on 2019-12-22 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0018_auto_20191221_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='additem',
            name='pic1',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='additem',
            name='pic2',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='additem',
            name='pic3',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='additem',
            name='pic4',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
