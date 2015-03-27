import datetime

from django.db import models

# Create your models here.
class Sensor(models.Model):
	# 0、生成时间
	PublicationDate = models.DateTimeField('date published');
	# 1、接力器反馈（接力器位移）---接力器
	ServomotorFeedback_1 = models.FloatField(default=0);
	# 2、调节器输出信号---调节器
	RegulatorOutput_2 = models.FloatField(default=0);
	# 3、电液转换器反馈传感器---电液转换器、伺服电机
	ElectroHydraulicFeedback_3 = models.IntegerField(default=0);
	# 4、主配漏油量---管路漏油量检测传感器
	Leakage_4 = models.FloatField(default=0);
	# 5、接力器端盖---接力器
	ServomotorCap_5 = models.FloatField(default=0);
	# 6、导叶关闭时间---接力器、伺服电机
	ServomotorCloseTime_6 = models.FloatField(default=0);
	# 7、油泵电机电流---油泵电机
	OilPumpCurrent_7 = models.FloatField(default=0);
	# 8、排油阀门---排油阀门
	OilExtractionValve_8 = models.BooleanField(default=True);
	# 9、调节信号---PID调节器
	ConditioningSignal_9 = models.FloatField(default=0);
	# 10、负荷---PID调节器
	PIDLoad_10 = models.FloatField(default=0);
	# 11、负荷---并网
	ParallelLoad_11 = models.FloatField(default=0);
	# 12、停机状态---
	HaltStatus_12 = models.BooleanField(default=True);
	# 13、平衡表（偏差）---
	BalancedDashboard_13 = models.FloatField(default=0);
	# 14、主配拒动开关---电液转换器
	RefuseSwitch_14 = models.BooleanField(default=True);
	# 15、油位---回油箱
	OilLevel_15 = models.FloatField(default=0);
	# 16、流量传感器---卸载阀至压力油罐的油管
	FlowSensor_16 = models.FloatField(default=0);
	# 17、负载状态---油泵
	OilPumpLoad_17 = models.FloatField(default=0);
	# 18、停机状态---油泵
	OilPumpHalt_18 = models.BooleanField(default=True);
	# 19、油流量---组合阀至压力油罐的流量传感器
	OilFlow_19 = models.FloatField(default=0);
	# 20、卸载时间---油泵电机
	DischargeTime_20 = models.FloatField(default=0);
	# 21、软启动器工作状态---软启动器
	SoftLauncherStatus_21 = models.FloatField(default=0);
	# 22、三相电流---油泵电机
	OilPump3current_22 = models.FloatField(default=0);
	# 23、三相电压---油泵电机
	OilPump3Voltage_23 = models.FloatField(default=0);
	# 24、工况---并网
	ParallelWorkingCondition_24 = models.BooleanField(default=True);
	# 25、事故信号（事故配压阀）---
	EmergencySignal_25 = models.BooleanField(default=True);
	# 26、油混水监测信号---混水传感器
	TurbidWaterSignal_26 = models.FloatField(default=0);
	# 27、杂质颗粒监测信号---油质检测仪
	ImpurityParticlesSignal_27 = models.FloatField(default=0);
	# 28、电液转换器反馈传感器电流（伺服电机电流变化）---电液转换器
	ElectroHydraulicCurrent_28 = models.FloatField(default=0);

	def __unicode__(self):              # __unicode__ on Python 2
        return self.PublicationDate;
		