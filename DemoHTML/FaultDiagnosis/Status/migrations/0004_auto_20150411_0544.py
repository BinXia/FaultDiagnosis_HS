# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Status', '0003_sensor_mainrefuseoperation_32'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='ElectroHydraulicFeedback_3',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sensor',
            name='MainRefuseOperation_32',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
    ]
