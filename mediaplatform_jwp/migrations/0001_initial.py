# Generated by Django 2.0.7 on 2018-07-11 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mediaplatform', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('key', models.CharField(editable=False, max_length=64, primary_key=True, serialize=False)),
                ('updated', models.BigIntegerField(help_text='Last updated timestamp')),
                ('item', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='jwp', to='mediaplatform.MediaItem')),
            ],
        ),
    ]
