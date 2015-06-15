#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include "DataProcess.c"

#define ERROR_COUNT 2 		// 故障種類數量
#define Turbid_THRE 0.5 	// 油質渾濁閾值
#define Impurity_THRE 0.7 	// 油質雜質閾值

// 健康狀態預測
// 輸入：
//		int time_point:		時間點
// 輸出：
//		int *error:			健康狀態預測
//			[0]	油中混水,油中混水超标
//			[1]	杂质颗粒度过多,杂质颗粒度过多
int *Prediction(int time_point)
{	
	// 獲取實時數據
	char mission_id[] = "3.3";	//任務ID
	double *data = ReturnData(mission_id,time_point);
	// 故障標誌
	int *error = (int *)malloc(sizeof(int)*ERROR_COUNT);
	for (int i = 0; i < ERROR_COUNT; ++i)
		error[i] = 0;

	// 分析數據
		// 油中混水,油中混水超标
	if (data[0] > Turbid_THRE)
		error[0] = 1;
		// 杂质颗粒度过多,杂质颗粒度过多
	if (data[1] > Impurity_THRE)
		error[1] = 1;
		
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