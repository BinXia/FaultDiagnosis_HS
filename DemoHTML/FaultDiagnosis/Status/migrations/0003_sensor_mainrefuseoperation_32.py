# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Status', '0002_log'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='MainRefuseOperation_32',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
