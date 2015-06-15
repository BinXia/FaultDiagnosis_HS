#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include "DataProcess.c"

#define ERROR_COUNT 2 		// 故障種類數量
#define I_THRE 0.7 			// 油泵电机三相电流閾值
#define V_THRE 0.5 			// 油泵电机三相电壓閾值

// 健康狀態預測
// 輸入：
//		int time_point:		時間點
// 輸出：
//		int *error:			健康狀態預測
//			[0]	油泵电机三相电流异常,油泵电机电流超过额定值
//			[1]	油泵电机三相电压异常,油泵电机电压超过额定值
int *Prediction(int time_point)
{	
	// 獲取實時數據
	char mission_id[] = "3.2";	//任務ID
	double *data = ReturnData(mission_id,time_point);
	// 故障標誌
	int *error = (int *)malloc(sizeof(int)*ERROR_COUNT);
	for (int i = 0; i < ERROR_COUNT; ++i)
		error[i] = 0;

	// 分析數據
	if (data[0] == 1){
		// 油泵电机三相电流异常,油泵电机电流超过额定值
		if (data[1] > I_THRE)		
			error[0] = 1;
		// 油泵电机三相电压异常,油泵电机电压超过额定值
		if (data[2] > V_THRE)		
			error[1] = 1;
	}
		
	/////////////
	// 測試部份 //
	/////////////

	// 觀測故障情況
	// printf("%d\t%d\n", error[0],error[1]);
	
	return error;
}








int main(int argc, char const *argv[])
{
	//數據分析
	for (int i = 801; i < 1001; ++i){
		Prediction(i);
	}
	return 0;
}