# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartsahar', '0002_events'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='is_considered',
        ),
    ]
