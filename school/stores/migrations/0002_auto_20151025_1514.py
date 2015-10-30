# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='country',
            field=models.CharField(default=b'India', max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='ip',
            field=models.CharField(default=b'', max_length=50, null=True, blank=True),
        ),
    ]
