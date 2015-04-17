# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Status', '0004_auto_20150411_0544'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='ErrorEquipment',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='log',
            name='Reason',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
    ]
