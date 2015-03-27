import numpy as np
import random



class MainZeroShift(object):
	"""docstring for MainZeroShift"""
	def __init__(self):
		super(MainZeroShift, self).__init__()

		self._perRecords = list();
		self._dayRecords = list();




###########################################################
# 01-Randomly generate data
###########################################################
	def DataGeneratgion(self,count):
		for iteration in xrange(count):
			Result_7_1 = random.choice([0,1]);
			Result_7_2 = random.choice([0,1]);
			Signal_30 = random.random();
			Signal_2 = random.random();

			DataFile = open('./data/1_1_MainZeroShift','a');
			DataFile.write('{0}\t{1}\n'.format(Signal_1,Signal_2));
			DataFile.close();

###########################################################
# 02-Process the data
###########################################################
	def LoadData(self):
		


	def outputReport(self):
		


def main():
	task = MainZeroShift();
	task.DataGeneratgion(43200);
	# task.LoadData();
	# task.outputReport();




if __name__ == '__main__': main();