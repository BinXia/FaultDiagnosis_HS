# coding=UTF-8
import numpy as np
import random
import MySQLdb
import time



class MainBlock(object):
	"""docstring for MainBlock"""
	def __init__(self):
		super(MainBlock, self).__init__()

		self._2 = list();
		self._3 = list();
		self._7 = list();
		self._32 = list();

		self._output = list();

###########################################################
# 01-Process the data
###########################################################
	def LoadData(self,feature,name,startTime,endTime):
		database = MySQLdb.connect('localhost','root','qwert','FaultDiagnosis');
		with database:
			cursor = database.cursor();
			cursor.execute('SELECT PublicationDate,{0} FROM Status_sensor WHERE id >= \'{1}\' AND id <= \'{2}\''.format(name,startTime,endTime));
			data = cursor.fetchall();
			for datum in data:
				feature.append([datum[0],float(datum[1])]);
			cursor.close();
		database.close();


	def outputReport(self,threshold,startTime):
		# analyze feature
		for index in xrange(len(self._32)):

			if self._2[index][1] == 1 and self._3[index][1] < threshold and self._7[index][1] == 0:
				if self._32[index][1] == 0:
					self._output.append([self._32[index][0],0,'正常']);
				else:
					self._output.append([self._32[index][0],1,'引导阀工作不正常，有发卡情况']);

			else:
				self._output.append([self._32[index][0],0,'正常']);


		print self._output


		# edit log
		log_record = list();
		for index in xrange(len(self._output)):
			if index == 0 and self._output[index][1] == 1:
				log_record.append([self._output[index][0],self._output[index][2]]);
			elif index == 0 and self._output[index][1] == 0:
				continue;

			if self._output[index][1] == 1 and self._output[index-1][1] == 0:
				log_record.append([self._output[index][0],self._output[index][2]]);
			elif self._output[index][1] == 1 and self._output[index-1][1] == 1 and self._output[index][2] != self._output[index-1][2]:
				log_record.append([self._output[index][0],self._output[index][2]]);

		print log_record


		# input analysis
		database = MySQLdb.connect('localhost','root','qwert','FaultDiagnosis');
		with database:
			cursor = database.cursor();
			for x in xrange(len(self._output)):
				cursor.execute('INSERT into Status_prediction(id,PublicationDate,YinDaoFa_9) values(\'{0}\',\'{1}\',\'{2}\')'.format(x+startTime,self._output[x][0],self._output[x][1]));
				database.commit();
			cursor.close();
		database.close();

		# input log
		database = MySQLdb.connect('localhost','root','qwert','FaultDiagnosis');
		with database:
			cursor = database.cursor();
			for index in xrange(len(log_record)):
				cursor.execute('INSERT into Status_log(PublicationDate,LogInformation) values(\'{0}\',\'{1}\')'.format(log_record[index][0],log_record[index][1]));
				database.commit();
			cursor.close();
		database.close();


def main():
	# initialize
	startTime = 1701;
	endTime = startTime+99;
	threshold = 0.6;

	task = MainBlock();

	variableName = ['RegulatorOutput_2','ElectroHydraulicFeedback_3','OilPumpCurrent_7','MainRefuseOperation_32'];
	variable = [task._2,task._3,task._7,task._32];
	for index in range(len(variable)):
		task.LoadData(variable[index],variableName[index],startTime,endTime);

	task.outputReport(threshold,startTime);




if __name__ == '__main__': main();