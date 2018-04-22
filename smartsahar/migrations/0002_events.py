# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartsahar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event', models.CharField(blank=True, max_length=20, choices=[(b'Health', b'Health'), (b'Education', b'Education'), (b'Transport', b'Transport')])),
                ('Description', models.CharField(max_length=200)),
                ('posted_by', models.CharField(max_length=200, blank=True)),
                ('citizensip_no', models.CharField(max_length=20)),
                ('District', models.CharField(blank=True, max_length=100, choices=[(b'Kathmandu', b'Kathmandu'), (b'Pokhara', b'Pokhara'), (b'Chitawan', b'Chitawan'), (b'Bhairahawa', b'Bhairahawa'), (b'Nuwakot', b'Nuwakot')])),
                ('Location', models.CharField(max_length=100, blank=True)),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('is_considered', models.BooleanField(default=False)),
            ],
        ),
    ]
