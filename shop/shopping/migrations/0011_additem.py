# Generated by Django 3.0 on 2019-12-21 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shopping', '0010_delete_shopping'),
    ]

    operations = [
        migrations.CreateModel(
            name='additem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter your name', max_length=10)),
                ('title', models.CharField(max_length=10)),
            ],
        ),
    ]
