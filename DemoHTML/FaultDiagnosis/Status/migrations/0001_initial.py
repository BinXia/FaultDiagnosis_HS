# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('PublicationDate', models.DateTimeField(verbose_name=b'date published')),
                ('FenDuanGuanBiZhuangZhi_1', models.BooleanField(default=True)),
                ('JieLiQiFanKui_2', models.BooleanField(default=True)),
                ('ShiGuPeiYaFa_3', models.BooleanField(default=True)),
                ('YouBengDianJi_4', models.BooleanField(default=True)),
                ('ZhuPeiYaFa_5', models.BooleanField(default=True)),
                ('ZhuJieLiQi_6', models.BooleanField(default=True)),
                ('YouZhiWuRan_7', models.BooleanField(default=True)),
                ('WuYouDianZhuan_8', models.BooleanField(default=True)),
                ('YinDaoFa_9', models.BooleanField(default=True)),
                ('ZuHeFa_10', models.BooleanField(default=True)),
                ('YouBeng_11', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
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
                ('OilNormalLevel_8', models.IntegerField(default=0)),
                ('OilPumpOne_9', models.FloatField(default=0)),
                ('OilPumpTwo_10', models.FloatField(default=0)),
                ('OilMachineStatus_11', models.IntegerField(default=0)),
                ('OilMachineCurrent_12', models.FloatField(default=0)),
                ('OilExtractionValve_13', models.BooleanField(default=True)),
                ('PIDLoad_14', models.FloatField(default=0)),
                ('ParallelLoad_15', models.FloatField(default=0)),
                ('HaltStatus_16', models.BooleanField(default=True)),
                ('BalancedDashboard_17', models.FloatField(default=0)),
                ('OilLevel_18', models.FloatField(default=0)),
                ('OilPumpLoad_19', models.FloatField(default=0)),
                ('OilPumpHalt_20', models.BooleanField(default=True)),
                ('OilFlow_21', models.FloatField(default=0)),
                ('DischargeTime_22', models.FloatField(default=0)),
                ('SoftLauncherStatus_23', models.FloatField(default=0)),
                ('OilPump3current_24', models.FloatField(default=0)),
                ('OilPump3Voltage_25', models.FloatField(default=0)),
                ('ParallelWorkingCondition_26', models.BooleanField(default=True)),
                ('LeafServomotorFeedback_27', models.FloatField(default=0)),
                ('EmergencySignal_28', models.BooleanField(default=True)),
                ('TurbidWaterSignal_29', models.FloatField(default=0)),
                ('ImpurityParticlesSignal_30', models.FloatField(default=0)),
                ('LeakBoxOilLevel_31', models.FloatField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
