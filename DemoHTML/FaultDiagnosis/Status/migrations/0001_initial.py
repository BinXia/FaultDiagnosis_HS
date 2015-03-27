# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('PublicationDate', models.DateTimeField(verbose_name=b'date published')),
                ('ServomotorFeedback_1', models.FloatField(default=0)),
                ('RegulatorOutput_2', models.FloatField(default=0)),
                ('ElectroHydraulicFeedback_3', models.IntegerField(default=0)),
                ('Leakage_4', models.FloatField(default=0)),
                ('ServomotorCap_5', models.FloatField(default=0)),
                ('ServomotorCloseTime_6', models.FloatField(default=0)),
                ('OilPumpCurrent_7', models.FloatField(default=0)),
                ('OilExtractionValve_8', models.BooleanField(default=True)),
                ('ConditioningSignal_9', models.FloatField(default=0)),
                ('PIDLoad_10', models.FloatField(default=0)),
                ('ParallelLoad_11', models.FloatField(default=0)),
                ('HaltStatus_12', models.BooleanField(default=True)),
                ('BalancedDashboard_13', models.FloatField(default=0)),
                ('RefuseSwitch_14', models.BooleanField(default=True)),
                ('OilLevel_15', models.FloatField(default=0)),
                ('FlowSensor_16', models.FloatField(default=0)),
                ('OilPumpLoad_17', models.FloatField(default=0)),
                ('OilPumpHalt_18', models.BooleanField(default=True)),
                ('OilFlow_19', models.FloatField(default=0)),
                ('DischargeTime_20', models.FloatField(default=0)),
                ('SoftLauncherStatus_21', models.FloatField(default=0)),
                ('OilPump3current_22', models.FloatField(default=0)),
                ('OilPump3Voltage_23', models.FloatField(default=0)),
                ('ParallelWorkingCondition_24', models.BooleanField(default=True)),
                ('EmergencySignal_25', models.BooleanField(default=True)),
                ('TurbidWaterSignal_26', models.FloatField(default=0)),
                ('ImpurityParticlesSignal_27', models.FloatField(default=0)),
                ('ElectroHydraulicCurrent_28', models.FloatField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
