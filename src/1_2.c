#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include "DataProcess.c"

#define ERROR_COUNT 1 		// 故障種類數量
#define I_THRE 0.6 			// 伺服電機驅動器電流閾值


// 健康狀態預測
// 輸入：
//		int time_point:		時間點
// 輸出：
//		int *error:			健康狀態預測
//			[0]	引导阀工作不正常,引导阀发卡
int *Prediction(int time_point)
{	
	// 獲取實時數據
	char mission_id[] = "1.2";	//任務ID
	double *data = ReturnData(mission_id,time_point);
	// 故障標誌
	int *error = (int *)malloc(sizeof(int)*ERROR_COUNT);
	for (int i = 0; i < ERROR_COUNT; ++i)
		error[i] = 0;

	// 分析數據
		// 引导阀工作不正常,引导阀发卡
	if (data[0] == 1 && data[1] < I_THRE && data[2] == 0 && data[3] != 0)		
		error[0] = 1;



	/////////////
	// 測試部份 //
	/////////////

	// 觀測故障情況
	printf("%d\n", error[0]);
	
	return error;
}








int main(int argc, char const *argv[])
{
	//數據分析
	for (int i = 1701; i < 1801; ++i){
		Prediction(i);
	}
	return 0;
}