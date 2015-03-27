import numpy as np
import random



class OilSpill(object):
	"""docstring for OilSpill"""
	def __init__(self):
		super(OilSpill, self).__init__()

		self._perRecords = list();
		self._dayRecords = list();




###########################################################
# 01-Randomly generate data
###########################################################
	def DataGeneratgion(self,count):
		for iteration in xrange(count):
			Signal_2 = random.choice([1]+[0]*10000);
			Signal_3 = random.choice([1,0]+[0.5]*10000);
			Signal_4 = random.random();

			DataFile = open('./data/1_2_OilSplil','a');
			DataFile.write('{0}\t{1}\t{2}\n'.format(Signal_2,Signal_3,Signal_4));
			DataFile.close();

###########################################################
# 02-Process the data
###########################################################
	def LoadData(self):
		OnceCount = 0;
		record = dict();
		for datum in open('./data/1_2_OilSplil').readlines():
			datum = datum.strip().split('\t');
			Signal_2 = float(datum[0]);
			Signal_3 = float(datum[1]);
			Signal_4 = float(datum[2]);
			
			if OnceCount == 0:
				record = dict();
				record['Signal_2'] = list();
				record['Signal_3'] = list();
				record['Signal_4'] = list();
				record['Signal_4Max'] = float();
				record['Signal_4Min'] = float();
				record['Signal_4Avg'] = float();
				record['OilSpill'] = bool();

			if Signal_2 not in record['Signal_2']:
				record['Signal_2'].append(Signal_2);
			if Signal_3 not in record['Signal_3']:
				record['Signal_3'].append(Signal_3);
			record['Signal_4'].append(Signal_4);
			OnceCount += 1;

			if OnceCount == 600:
				OnceCount = 0;
				record['Signal_4Avg'] = np.average(np.array(record['Signal_4']));
				record['Signal_4Max'] = max(record['Signal_4']);
				record['Signal_4Min'] = min(record['Signal_4']);
				if len(record['Signal_2']) == 1 and len(record['Signal_3']) == 1:
					record['OilSpill'] = 1;
				else:
					record['OilSpill'] = 0;
				self._perRecords.append(record);

			# if len(self._records) > 10:
			# 	break;


	def outputReport(self):
		perRecord = dict();
		perRecord['Signal_4'] = list();
		perRecord['Signal_4Max'] = float();
		perRecord['Signal_4Min'] = float();
		perRecord['Signal_4Avg'] = float();
		for index,record in enumerate(self._perRecords):
			if record['OilSpill'] == 1:
				perRecord['Signal_4'].append(record['Signal_4Avg']);


			if (index+1)%1440 == 0:
				print index;
				perRecord['Signal_4Max'] = max(perRecord['Signal_4']);
				perRecord['Signal_4Min'] = min(perRecord['Signal_4']);
				perRecord['Signal_4Avg'] = np.average(np.array(perRecord['Signal_4']));
				self._dayRecords.append(perRecord);

				perRecord = dict();
				perRecord['Signal_4'] = list();
				perRecord['Signal_4Max'] = float();
				perRecord['Signal_4Min'] = float();
				perRecord['Signal_4Avg'] = float();

		report = open('./data/1_2_OilSpill_Report','w');
		for record in self._dayRecords:
			report.write('{0}\t{1}\t{2}\n'.format(record['Signal_4Avg'],record['Signal_4Max'],record['Signal_4Min']))
			report.flush();
		report.close();


def main():
	task = OilSpill();
	# task.DataGeneratgion(25920000);
	task.LoadData();
	task.outputReport();




if __name__ == '__main__': main();