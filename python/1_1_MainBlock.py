import numpy as np
import random



class MainBlock(object):
	"""docstring for MainBlock"""
	def __init__(self):
		super(MainBlock, self).__init__()

		self._perRecords = list();
		self._dayRecords = list();




###########################################################
# 01-Randomly generate data
###########################################################
	def DataGeneratgion(self,count):
		for iteration in xrange(count):
			Signal_1 = random.random();
			Signal_2 = random.random();

			DataFile = open('./data/1_1_MainBlock','a');
			DataFile.write('{0}\t{1}\n'.format(Signal_1,Signal_2));
			DataFile.close();

###########################################################
# 02-Process the data
###########################################################
	def LoadData(self):
		


	def outputReport(self):
		


def main():
	task = MainBlock();
	task.DataGeneratgion(43200);
	# task.LoadData();
	# task.outputReport();




if __name__ == '__main__': main();