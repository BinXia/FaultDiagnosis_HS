import MySQLdb


########################################################################################
# 01-Output data from MySQL to file
########################################################################################
class DataTool(object):
	def __init__(self):
		pass

	def FromMySQLToFile(self):
		DataFile = open('../src/DataFile','w')

		database = MySQLdb.connect('localhost','root','qwert','FaultDiagnosis')
		with database:
			cursor = database.cursor()
			cursor.execute('SELECT * FROM Status_sensor')
			data = cursor.fetchall()
			for datum in data:
				for index in xrange(len(datum)):
					if index == 1:
						continue;
					DataFile.write('{0}\t'.format(datum[index]))
				DataFile.write('\n')
		database.close()
		DataFile.close()




















def main():
	task = DataTool()
	task.FromMySQLToFile()

if __name__ == '__main__':
	main()