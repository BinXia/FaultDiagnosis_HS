# coding=UTF-8
import numpy as np
import random
import MySQLdb
import time



class MainBlock(object):
	"""docstring for MainBlock"""
	def __init__(self):
		super(MainBlock, self).__init__()

		self._27 = list();
		self._28 = list();

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
		for index in xrange(len(self._28)):
			# can not analyze with only one datum
			if index < 5:
				self._output.append([self._28[index][0],0,'正常']);
				continue;
			# inference
			if self._28[index][1] == 1:
				globalK = np.abs((self._27[0][1] - self._27[index][1])/float(index/100.0));
				localK = np.abs((self._27[index-1][1] - self._27[index][1])/float(1/100.0));
				if globalK > threshold and localK > threshold:
					self._output.append([self._28[index][0],1,'事故配压阀异常动作']);
				elif np.abs(globalK - localK) > 0.2:
					self._output.append([self._28[index][0],1,'事故配压阀异常动作']);
				else:
					self._output.append([self._28[index][0],0,'正常']);
			else:
				self._output.append([self._28[index][0],0,'正常']);

			# if self._output[-1] == 1:
			# 	print index,globalK,localK;
		# print self._output


		# edit log
		log_record = list();
		for index in xrange(len(self._output)):
			if index == 0:
				continue;

			if self._output[index][1] == 1 and self._output[index-1][1] == 0:
				log_record.append([self._output[index][0],self._output[index][2]]);
			elif self._output[index][1] == 1 and self._output[index-1][1] == 1 and self._output[index][2] != self._output[index-1][2]:
				log_record.append([self._output[index][0],self._output[index][2]]);


		# input analysis
		database = MySQLdb.connect('localhost','root','qwert','FaultDiagnosis');
		with database:
			cursor = database.cursor();
			for x in xrange(len(self._28)):
				cursor.execute('INSERT into Status_prediction(id,PublicationDate,ShiGuPeiYaFa_3) values(\'{0}\',\'{1}\',\'{2}\')'.format(x+startTime,self._output[x][0],self._output[x][1]));
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
	startTime = 601;
	endTime = startTime+99;
	threshold = 1.3;

	task = MainBlock();

	variableName = ['LeafServomotorFeedback_27','EmergencySignal_28'];
	variable = [task._27,task._28];
	for index in range(len(variable)):
		task.LoadData(variable[index],variableName[index],startTime,endTime);

	task.outputReport(threshold,startTime);




if __name__ == '__main__': main();