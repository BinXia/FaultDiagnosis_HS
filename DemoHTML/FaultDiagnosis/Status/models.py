import datetime

from django.db import models

# Create your models here.
class Sensor(models.Model):
	# 0
	PublicationDate = models.DateTimeField('date published');
	# 1
	ServomotorFeedback_1 = models.FloatField(default=0);
	# 2
	RegulatorOutput_2 = models.FloatField(default=0);
	# 3
	ElectroHydraulicFeedback_3 = models.FloatField(default=0);
	# 4
	Leakage_4 = models.FloatField(default=0);
	# 5
	ServomotorCap_5 = models.FloatField(default=0);
	# 6
	ServomotorCloseTime_6 = models.FloatField(default=0);
	# 7
	OilPumpCurrent_7 = models.FloatField(default=0);
	# 8
	OilNormalLevel_8 = models.IntegerField(default=0);
	# 9
	OilPumpOne_9 = models.FloatField(default=0);
	# 10
	OilPumpTwo_10 = models.FloatField(default=0);
	# 11
	OilMachineStatus_11 = models.IntegerField(default=0);
	# 12
	OilMachineCurrent_12 = models.FloatField(default=0);
	# 13
	OilExtractionValve_13 = models.BooleanField(default=True);
	# 14
	PIDLoad_14 = models.FloatField(default=0);
	# 15
	ParallelLoad_15 = models.FloatField(default=0);
	# 16
	HaltStatus_16 = models.BooleanField(default=True);
	# 17
	BalancedDashboard_17 = models.FloatField(default=0);
	# 18
	OilLevel_18 = models.FloatField(default=0);
	# 19
	OilPumpLoad_19 = models.FloatField(default=0);
	# 20
	OilPumpHalt_20 = models.BooleanField(default=True);
	# 21
	OilFlow_21 = models.FloatField(default=0);
	# 22
	DischargeTime_22 = models.FloatField(default=0);
	# 23
	SoftLauncherStatus_23 = models.FloatField(default=0);
	# 24
	OilPump3current_24 = models.FloatField(default=0);
	# 25
	OilPump3Voltage_25 = models.FloatField(default=0);
	# 26
	ParallelWorkingCondition_26 = models.BooleanField(default=True);
	# 27
	LeafServomotorFeedback_27 = models.FloatField(default=0);
	# 28
	EmergencySignal_28 = models.BooleanField(default=True);
	# 29
	TurbidWaterSignal_29 = models.FloatField(default=0);
	# 30
	ImpurityParticlesSignal_30 = models.FloatField(default=0);
	# 31
	LeakBoxOilLevel_31 = models.FloatField(default=0);
	# 32
	MainRefuseOperation_32 = models.FloatField(default=0);

	def __unicode__(self):              # __unicode__ on Python 2
		return self.PublicationDate;



class Prediction(models.Model):
	# 0
	PublicationDate = models.DateTimeField('date published');
	# 1
	FenDuanGuanBiZhuangZhi_1 = models.BooleanField(default=True);
	# 2
	JieLiQiFanKui_2 = models.BooleanField(default=True);
	# 3
	ShiGuPeiYaFa_3 = models.BooleanField(default=True);
	# 4
	YouBengDianJi_4 = models.BooleanField(default=True);
	# 5
	ZhuPeiYaFa_5 = models.BooleanField(default=True);
	# 6
	ZhuJieLiQi_6 = models.BooleanField(default=True);
	# 7
	YouZhiWuRan_7 = models.BooleanField(default=True);
	# 8
	WuYouDianZhuan_8 = models.BooleanField(default=True);
	# 9
	YinDaoFa_9 = models.BooleanField(default=True);
	# 10
	ZuHeFa_10 = models.BooleanField(default=True);
	# 11
	YouBeng_11 = models.BooleanField(default=True);


class Log(models.Model):
	# 0
	PublicationDate = models.DateTimeField('date published');
	# 1
	ErrorEquipment = models.TextField(default="");
	# 2
	LogInformation = models.TextField(default="");
	# 3
	Reason = models.TextField(default="");




