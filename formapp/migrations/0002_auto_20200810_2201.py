# Generated by Django 3.0.3 on 2020-08-10 16:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='formdata',
            name='email',
            field=models.CharField(default='default@default.com', max_length=264, unique=True),
        ),
        migrations.AddField(
            model_name='formdata',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=264),
            preserve_default=False,
        ),
    ]
