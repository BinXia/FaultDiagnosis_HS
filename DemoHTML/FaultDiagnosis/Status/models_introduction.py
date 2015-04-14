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
	# 6、导叶关闭时间（主配关闭最大行程）---接力器、伺服电机
	ServomotorCloseTime_6 = models.FloatField(default=0);
	# 7、油泵电机电流（电液转换器驱动器电流）---油泵电机
	OilPumpCurrent_7 = models.FloatField(default=0);
	# 8、回油箱油位正常液位
	OilNormalLevel_8 = models.IntegerField(default=0);
	# 9、油泵输油量1
	OilPumpOne_9 = models.FloatField(default=0);
	# 10、油泵输油量2
	OilPumpTwo_10 = models.FloatField(default=0);
	# 11、油泵电机运行工况（起、停机）
	OilMachineStatus_11 = models.IntegerField(default=0);
	# 12、油泵电机电流
	OilMachineCurrent_12 = models.FloatField(default=0);
	# 13、排油阀门---排油阀门
	OilExtractionValve_13 = models.BooleanField(default=True);
	# 14、负荷---PID调节器
	PIDLoad_14 = models.FloatField(default=0);
	# 15、负荷---并网
	ParallelLoad_15 = models.FloatField(default=0);
	# 16、停机状态---
	HaltStatus_16 = models.BooleanField(default=True);
	# 17、平衡表（偏差）--- 调节器输出信号与导叶接力器反馈信号差值
	BalancedDashboard_17 = models.FloatField(default=0);
	# 18、油位---回油箱
	OilLevel_18 = models.FloatField(default=0);
	# 19、负载状态---油泵
	OilPumpLoad_19 = models.FloatField(default=0);
	# 20、停机状态---油泵
	OilPumpHalt_20 = models.BooleanField(default=True);
	# 21、油流量---组合阀至压力油罐的流量传感器
	OilFlow_21 = models.FloatField(default=0);
	# 22、卸载时间---油泵电机
	DischargeTime_22 = models.FloatField(default=0);
	# 23、软启动器工作状态---软启动器
	SoftLauncherStatus_23 = models.FloatField(default=0);
	# 24、三相电流---油泵电机
	OilPump3current_24 = models.FloatField(default=0);
	# 25、三相电压---油泵电机
	OilPump3Voltage_25 = models.FloatField(default=0);
	# 26、工况---并网
	ParallelWorkingCondition_26 = models.BooleanField(default=True);
	# 27、导叶接力器反馈
	LeafServomotorFeedback_27 = models.FloatField(default=0);
	# 28、事故信号（事故配压阀）---
	EmergencySignal_28 = models.BooleanField(default=True);
	# 29、油混水监测信号---混水传感器
	TurbidWaterSignal_29 = models.FloatField(default=0);
	# 30、杂质颗粒监测信号---油质检测仪
	ImpurityParticlesSignal_30 = models.FloatField(default=0);
	# 31、漏油箱液位
	LeakBoxOilLevel_31 = models.FloatField(default=0);

	def __unicode__(self):              # __unicode__ on Python 2
        return self.PublicationDate;

class Prediction(models.Model):
	# 0 生成时间
	PublicationDate = models.DateTimeField('date published');
	# 1 分段关闭装置
	FenDuanGuanBiZhuangZhi_1 = models.BooleanField(default=True);
	# 2 接力器反馈
	JieLiQiFanKui_2 = models.BooleanField(default=True);
	# 3 事故配压阀
	ShiGuPeiYaFa_3 = models.BooleanField(default=True);
	# 4 油泵电机
	YouBengDianJi_4 = models.BooleanField(default=True);
	# 5 主配压阀
	ZhuPeiYaFa_5 = models.BooleanField(default=True);
	# 6 主接力器
	ZhuJieLiQi_6 = models.BooleanField(default=True);
	# 7 油质污染
	YouZhiWuRan_7 = models.BooleanField(default=True);
	# 8 无油电转
	WuYouDianZhuan_8 = models.BooleanField(default=True);
	# 9 引导阀
	YinDaoFa_9 = models.BooleanField(default=True);
	# 10 组合阀
	ZuHeFa_10 = models.BooleanField(default=True);
	# 11 油泵
	YouBeng_11 = models.BooleanField(default=True);