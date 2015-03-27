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
	ElectroHydraulicFeedback_3 = models.IntegerField(default=0);
	# 4
	Leakage_4 = models.FloatField(default=0);
	# 5
	ServomotorCap_5 = models.FloatField(default=0);
	# 6
	ServomotorCloseTime_6 = models.FloatField(default=0);
	# 7
	OilPumpCurrent_7 = models.FloatField(default=0);
	# 8
	OilExtractionValve_8 = models.BooleanField(default=True);
	# 9
	ConditioningSignal_9 = models.FloatField(default=0);
	# 10
	PIDLoad_10 = models.FloatField(default=0);
	# 11
	ParallelLoad_11 = models.FloatField(default=0);
	# 12
	HaltStatus_12 = models.BooleanField(default=True);
	# 13
	BalancedDashboard_13 = models.FloatField(default=0);
	# 14
	RefuseSwitch_14 = models.BooleanField(default=True);
	# 15
	OilLevel_15 = models.FloatField(default=0);
	# 16
	FlowSensor_16 = models.FloatField(default=0);
	# 17
	OilPumpLoad_17 = models.FloatField(default=0);
	# 18
	OilPumpHalt_18 = models.BooleanField(default=True);
	# 19
	OilFlow_19 = models.FloatField(default=0);
	# 20
	DischargeTime_20 = models.FloatField(default=0);
	# 21
	SoftLauncherStatus_21 = models.FloatField(default=0);
	# 22
	OilPump3current_22 = models.FloatField(default=0);
	# 23
	OilPump3Voltage_23 = models.FloatField(default=0);
	# 24
	ParallelWorkingCondition_24 = models.BooleanField(default=True);
	# 25
	EmergencySignal_25 = models.BooleanField(default=True);
	# 26
	TurbidWaterSignal_26 = models.FloatField(default=0);
	# 27
	ImpurityParticlesSignal_27 = models.FloatField(default=0);
	# 28
	ElectroHydraulicCurrent_28 = models.FloatField(default=0);

	def __unicode__(self):              # __unicode__ on Python 2
		return self.PublicationDate;
		