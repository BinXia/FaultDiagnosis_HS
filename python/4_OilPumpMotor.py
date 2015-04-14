# coding=UTF-8
import numpy as np
import random
import MySQLdb
import time



class MainBlock(object):
	"""docstring for MainBlock"""
	def __init__(self):
		super(MainBlock, self).__init__()

		self._23 = list();
		self._24 = list();
		self._25 = list();

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
		for index in xrange(len(self._23)):
			# inference
			if self._23[index][1] == 1:
				if self._24[index][1] > threshold['I']:
					self._output.append([self._23[index][0],1,'油泵电机三相电流异常']);
				elif self._25[index][1] > threshold['V']:
					self._output.append([self._23[index][0],1,'油泵电机三相电压异常']);
				else:
					self._output.append([self._23[index][0],0,'正常']);


		# print self._output


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


		# input analysis
		database = MySQLdb.connect('localhost','root','qwert','FaultDiagnosis');
		with database:
			cursor = database.cursor();
			for x in xrange(len(self._23)):
				cursor.execute('INSERT into Status_prediction(id,PublicationDate,YouBengDianJi_4) values(\'{0}\',\'{1}\',\'{2}\')'.format(x+startTime,self._output[x][0],self._output[x][1]));
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
	startTime = 901;
	endTime = startTime+99;

	threshold = {'V':0.5,'I':0.7};

	task = MainBlock();

	variableName = ['SoftLauncherStatus_23','OilPump3current_24','OilPump3Voltage_25'];
	variable = [task._23,task._24,task._25];
	for index in range(len(variable)):
		task.LoadData(variable[index],variableName[index],startTime,endTime);

	task.outputReport(threshold,startTime);




if __name__ == '__main__': main();