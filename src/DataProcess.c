// #include "DataProcess.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 实时数据
double DataStream[1800][34];


char LoadDataFromFile()
{
	// 文件读取相关参数
	FILE *fp;
	char *line = NULL;
	size_t len = 0;
	ssize_t read;

	fp = fopen("./DataFile","r");
	if (fp == NULL)
		printf("數據文件異常！");

	for (int r_id = 0; r_id < 1800; ++r_id){
		if ((read = getline(&line, &len, fp)) == -1) break;
		// 文本數據存儲
		for (int field_i = 0; field_i < 33; ++field_i){
			if ((line = strtok(line,"\t")) != NULL){
				DataStream[r_id][field_i] = atof(line);
				line = NULL;
			}
			else break;
		}
	}
	fclose(fp);
	return 0;
}

double *ReturnData(char mission_id[], int time_point)
{
	// 獲取數據
	LoadDataFromFile();
	double *data = NULL;
	int n;

	if (mission_id[0] == '1')		// 電液隨動系統
	{
		switch(mission_id[2]){
			case '1':			// 主配健康狀態預測
				n = 7;
				data = (double *)malloc(sizeof(double)*n);
				data[0] = DataStream[time_point][1];
				data[1] = DataStream[time_point][2];
				data[2] = DataStream[time_point][3];
				data[3] = DataStream[time_point][4];
				data[4] = DataStream[time_point][6];
				data[5] = DataStream[time_point][15];
				data[6] = DataStream[time_point][17];
				return data;
				break;
			case '2':			// 引導閥健康狀態預測
				n = 4;
				data = (double *)malloc(sizeof(double)*n);
				data[0] = DataStream[time_point][2];
				data[1] = DataStream[time_point][3];
				data[2] = DataStream[time_point][7];
				data[3] = DataStream[time_point][32];
				return data;
				break;
			case '3':			// 接力器健康狀態預測
				n = 5;
				data = (double *)malloc(sizeof(double)*n);
				data[0] = DataStream[time_point][1];	//壓差
				data[0] = DataStream[time_point][1];	//接力器反饋信號
				data[0] = DataStream[time_point][1];	//PID調節器輸出的調節信號
				data[0] = DataStream[time_point][1];	//功率
				data[0] = DataStream[time_point][1];	//停機備用狀態
				return data;
				break;
		}
	}
	else if (mission_id[0] == '2')	// 安全附加設備
	{
		switch(mission_id[2]){
			case '1':			// 分段關閉裝置健康狀態預測
				n = 3;
				data = (double *)malloc(sizeof(double)*n);
				data[0] = DataStream[time_point][3];
				data[1] = DataStream[time_point][26];
				data[2] = DataStream[time_point][27];
				return data;
				break;
			case '2':			// 事故配壓閥健康狀態預測
				n = 2;
				data = (double *)malloc(sizeof(double)*n);
				data[0] = DataStream[time_point][27];
				data[1] = DataStream[time_point][28];
				return data;
				break;
		}
	}
	else if (mission_id[0] == '3')	// 油壓裝置
	{
		switch(mission_id[2]){
			case '1':			// 組合閥及油泵健康狀態預測
				n = 1;
				data = (double *)malloc(sizeof(double)*n);
				data[0] = DataStream[time_point][1];
				return data;
				break;
			case '2':			// 油泵電機健康狀態預測
				n = 3;
				data = (double *)malloc(sizeof(double)*n);
				data[0] = DataStream[time_point][23];
				data[1] = DataStream[time_point][24];
				data[2] = DataStream[time_point][25];
				return data;
				break;
			case '3':			// 油質污染預測
				n = 2;
				data = (double *)malloc(sizeof(double)*n);
				data[0] = DataStream[time_point][29];
				data[1] = DataStream[time_point][30];
				return data;
				break;
			case '4':			// 油泵啟動頻繁
				n = 1;
				data = (double *)malloc(sizeof(double)*n);
				data[0] = DataStream[time_point][1];
				return data;
				break;
		}
	}

	return data;
}











// int main(int argc, char const *argv[])
// {
// 	char mission_id[] = "1.1";
// 	int time_point = 0;

// 	ReturnData(mission_id, time_point);
// 	return 0;
// }







