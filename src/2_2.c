#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include "DataProcess.c"
#include "PreDataList.c"

#define PreSIZE 100 		// 歷史數據大小
#define ParCOUNT 2 			// 變量數量
#define TIME_THRE 1.3 		// 判斷關閉時間閾值
#define CHAN_THRE 0.2 		// 判斷突變閾值
#define ERROR_COUNT 2 		// 故障種類數量


DNode PreDataStream[ParCOUNT];

int constructPreData()
{
	// 構建歷史數據存儲鏈表
	for (int i = 0; i < ParCOUNT; ++i)
	{	
		if (i == 0)
			create(&PreDataStream[i],PreSIZE,1.0);
		else
			create(&PreDataStream[i],PreSIZE,0.0);
	}
	return 0;
}



// 健康狀態預測
// 輸入：
//		int time_point:		時間點
//		DNode pre_data[]:	歷史數據
// 輸出：
//		int *error:			健康狀態預測
//			[0]	拐点变化、关机时间整定值发生变化,导叶接力器关闭过程特性曲线陡峭
//			[1]	接力器至导叶的传动系统有卡阻,导叶接力器关闭过程有突变点
int *Prediction(int time_point, DNode pre_data[])
{	
	// 獲取實時數據
	char mission_id[] = "2.2";	//任務ID
	double *data = ReturnData(mission_id,time_point);
	// 故障標誌
	int *error = (int *)malloc(sizeof(int)*ERROR_COUNT);
	for (int i = 0; i < ERROR_COUNT; ++i)
		error[i] = 0;

	// 預處理數據
	DNode head = pre_data[0]->next;	// 獲取數據鏈表
	int time_period = 1;				// 記錄關閉起始點到當前時間

	DNode start_point;					// 尋找開始關閉時刻
	while((head->next != NULL) && (head->num == 1))	head = head->next;
	start_point = head;
	DNode pre_point;					// 尋找上一時刻
	while(head->next != NULL) {head = head->next; ++time_period;}
	pre_point = head;

	double globalK; 					// 關閉速率過快﹣參考數值
	globalK = fabs((start_point->num - data[0])/((double)(time_period)/PreSIZE));
	double localK;						// 導葉卡頓與突變﹣參考數值
	localK = fabs((pre_point->num - data[0])/(double)(1.0/PreSIZE));

	// 分析數據
	if (data[1] == 1){
		// 拐点变化、关机时间整定值发生变化,导叶接力器关闭过程特性曲线陡峭
		if ((globalK > TIME_THRE) && (localK > TIME_THRE) && time_period > 10)
			error[0] = 1;
		// 接力器至导叶的传动系统有卡阻,导叶接力器关闭过程有突变点
		if (fabs(globalK - localK) > CHAN_THRE)
			error[1] = 1;
	}
	
	

	// 更新歷史數據鏈表
	for (int i = 0; i < ParCOUNT; ++i){
		pre_data[i]->next = pre_data[i]->next->next;	// 移動頭指針，拋棄最悠久歷史數據

		DNode tail = pre_data[i];						// 添加最新數據
		DNode newDatum = (DNode)malloc(sizeof(Node));
		while(tail->next != NULL)	tail = tail->next;
		newDatum->num = data[i];
		newDatum->next = NULL;
		tail->next = newDatum;
	}

	/////////////
	// 測試部份 //
	/////////////

	// 檢查關閉起始
	// if (start_point == pre_point)
	// 	printf("%p\n", start_point);

	// 檢查歷史數據情況
	// DNode check = pre_data[4]->next;
	// while(check->next != NULL){
	// 	printf("%f\t", check->num);
	// 	check = check->next;
	// }
	// printf("\n");

	// 觀測故障情況
	// printf("%d\t%d\t%d\n", error[0],error[1],error[2]);
	
	return error;
}




int main(int argc, char const *argv[])
{
	constructPreData();
	//數據分析
	for (int i = 601; i < 701; ++i){
		Prediction(i,PreDataStream);
	}
	
	return 0;
}