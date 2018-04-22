# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, choices=[(b'Kathmandu', b'Kathmandu'), (b'Pokhara', b'Pokhara'), (b'Chitawan', b'Chitawan'), (b'Bhairahawa', b'Bhairahawa'), (b'Nuwakot', b'Nuwakot')])),
                ('state', models.CharField(unique=True, max_length=20, choices=[(b'state1', b'state1'), (b'state2', b'state2'), (b'state3', b'state3'), (b'state4', b'state4'), (b'state5', b'state5'), (b'state6', b'state6'), (b'state7', b'state7')])),
                ('governor', models.CharField(max_length=30)),
            ],
        ),
    ]
