# coding=UTF-8
from django.shortcuts import render
from django.http import HttpResponse
import json
import MySQLdb
import time
from datetime import datetime

# Create your views here.
def UpdataDynamicData(request):
	try:
		# dynamic data for prediction
		if request.GET['type'] == 'multiple_all':
			initORupdate = int(request.GET['data']);
			startID = request.GET['id'];
			respondData = list();

			database = MySQLdb.connect('localhost','root','qwert','FaultDiagnosis');
			with database:
				cursor = database.cursor();
				cursor.execute('SELECT * FROM Status_sensor WHERE id >= \'{0}\' LIMIT {1}'.format(startID,initORupdate));
				data = cursor.fetchall();
				for index,datum in enumerate(data):
					respondData.append([int(time.mktime(datum[1].timetuple())*1000)]);
					for count in xrange(2,len(datum)):
						respondData[index].extend([datum[count]]);
				cursor.close();
			database.close();

		elif request.GET['type'] == 'single_all':
			initORupdate = int(request.GET['data']);
			startID = request.GET['id'];
			respondData = list();

			database = MySQLdb.connect('localhost','root','qwert','FaultDiagnosis');
			with database:
				cursor = database.cursor();
				cursor.execute('SELECT * FROM Status_prediction WHERE id >= \'{0}\' LIMIT {1}'.format(startID,initORupdate));
				data = cursor.fetchall();
				for index,datum in enumerate(data):
					respondData.append([int(time.mktime(datum[1].timetuple())*1000)]);
					for count in xrange(2,len(datum)):
						if datum[count] == None:
							respondData[index].extend([-1]);
						else:
							respondData[index].extend([datum[count]]);
				cursor.close();
			database.close();

		# dynamic data for prediction
		elif request.GET['type'] == 'single':
			initORupdate = int(request.GET['data']);
			startID = request.GET['id'];
			respondData = list();

			database = MySQLdb.connect('localhost','root','qwert','FaultDiagnosis');
			with database:
				cursor = database.cursor();
				if initORupdate == 0:
					cursor.execute('SELECT * FROM Status_prediction WHERE id = \'{0}\''.format(startID));
				else:
					cursor.execute('SELECT * FROM Status_prediction WHERE id >= \'{0}\' LIMIT {1}'.format(startID,initORupdate));
				data = cursor.fetchall();
				for datum in data:
					for index in xrange(len(datum)-2):
						respondData.append([int(time.mktime(datum[1].timetuple())*1000),datum[index+2]]);
				cursor.close();
			database.close();

		# dynamic data for sensor
		else:
			initORupdate = int(request.GET['data']);
			startID = request.GET['id'];
			field = request.GET['field'];
			respondData = list();

			database = MySQLdb.connect('localhost','root','qwert','FaultDiagnosis');
			with database:
				cursor = database.cursor();
				if initORupdate == 0:
					cursor.execute('SELECT PublicationDate,{0} FROM Status_sensor WHERE id = \'{1}\''.format(field,startID));
				else:
					cursor.execute('SELECT PublicationDate,{0} FROM Status_sensor WHERE id >= \'{1}\' LIMIT {2}'.format(field,startID,initORupdate));
				data = cursor.fetchall();
				for datum in data:
					respondData.append([int(time.mktime(datum[0].timetuple())*1000),datum[1]]);
				cursor.close();
			database.close();

		message = json.dumps(respondData);
		response = HttpResponse(message,content_type='application/json');
		response['Access-Control-Allow-Origin'] = '*';
		return response;

	except Exception, e:
		print e
		response = HttpResponse(json.dumps({"error":"Hey, man error!"}),content_type='application/json');
		response['Access-Control-Allow-Origin'] = '*';
		return response;
	

def SearchForHistory(request):
	try:
		# historic data for prediction
		if request.GET['type'] == 'single':
			startTime = request.GET['startTime'];
			endTime = request.GET['endTime'];
			name = request.GET['name'];
			respondData = list();

			database = MySQLdb.connect('localhost','root','qwert','FaultDiagnosis');
			with database:
				cursor = database.cursor();
				cursor.execute('SELECT PublicationDate,{0} FROM Status_prediction WHERE id >= \'{1}\' AND id <= \'{2}\''.format(name,startTime,endTime));
				data = cursor.fetchall();
				for datum in data:
					respondData.append([int(time.mktime(datum[0].timetuple())*1000),float(datum[1])]);
				cursor.close();
			database.close();

		# historic data for sensor
		else:
			startTime = int(request.GET['startTime']);
			endTime = int(request.GET['endTime']);
			name = request.GET['name'];
			respondData = list();

			database = MySQLdb.connect('localhost','root','qwert','FaultDiagnosis');
			with database:
				cursor = database.cursor();
				if startTime > 1000000:
					startTime = datetime.fromtimestamp(startTime/1000);
					endTime = datetime.fromtimestamp(endTime/1000);
					cursor.execute('SELECT PublicationDate,{0} FROM Status_sensor WHERE PublicationDate >= \'{1}\' AND PublicationDate <= \'{2}\''.format(name,startTime,endTime));
				else:
					cursor.execute('SELECT PublicationDate,{0} FROM Status_sensor WHERE id >= \'{1}\' AND id <= \'{2}\''.format(name,startTime,endTime));
				data = cursor.fetchall();
				for datum in data:
					respondData.append([int(time.mktime(datum[0].timetuple())*1000),float(datum[1])]);
				cursor.close();
			database.close();

		message = json.dumps(respondData);
		response = HttpResponse(message,content_type='application/json');
		response['Access-Control-Allow-Origin'] = '*';
		return response;


	except Exception, e:
		response = HttpResponse(json.dumps({"error":"Hey, man error!"}),content_type='application/json');
		response['Access-Control-Allow-Origin'] = '*';
		return response;


def RecordForHistory(request):
	try:
		currentTime = int(request.GET['currentTime']);
		respondData = list();

		database = MySQLdb.connect('localhost','root','qwert','FaultDiagnosis',charset='utf8');
		with database:
			cursor = database.cursor();
			if currentTime == 0:
				cursor.execute('SELECT PublicationDate,ErrorEquipment,LogInformation,Reason FROM Status_log');
			else:
				currentTime = datetime.fromtimestamp(int(request.GET['currentTime'])/1000)
				cursor.execute('SELECT PublicationDate,ErrorEquipment,LogInformation,Reason FROM Status_log WHERE PublicationDate <= \'{0}\''.format(currentTime));
			data = cursor.fetchall();
			for datum in data:
				respondData.append([int(time.mktime(datum[0].timetuple())),datum[1],datum[2],datum[3]]);
			cursor.close();
		database.close();
		respondData.reverse();

		message = json.dumps(respondData);
		response = HttpResponse(message,content_type='application/json');
		response['Access-Control-Allow-Origin'] = '*';
		return response;

	except Exception, e:
		response = HttpResponse(json.dumps({"error":"Hey, man error!"}),content_type='application/json');
		response['Access-Control-Allow-Origin'] = '*';
		return response;


