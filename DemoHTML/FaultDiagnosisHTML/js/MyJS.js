$(function () {
    // convert JQuery date to MySql datetime
    Date.prototype.toMysqlFormat = function() {
    var day = this.getDate();
    var month = this.getMonth()+1;
    return this.getFullYear()+"-"+( month >9 ? month: '0'+month )+"-"+( day >9 ? day: '0'+day );
    };


    //All: global variable for each section
    var urlPrefix = "http://127.0.0.1:8000",
        url,
        TIMENOW;

    //Dynamic: $(".liLeft").click
    var chartDynamicPrediction,
        chartDynamicSensor,
        intervalFunctionPrediction,
        intervalFUnctionSensor,
        startID_prediction = 91,
        startID_sensor = 91,
        intialDataNum = 90;

    //Search: $(".btn-primary").click
    var chartSearchPrediction,
        chartSearchSensor;

    //History record: $("#log").click
    var tableForRecord;

    //搜索相应时段信息
    $(".btn-primary").click(function(){
        //Lock the button
        $(this).attr('disabled', true);
        $("#container_search_l").removeClass("divInvisible");
        $("#container_search_r").removeClass("divInvisible");

        //initialize
        var chartTitle,
            chartSubTitle = "历史记录",
            multipleChartTitle = "相关参数反馈",
            seriesOptions_Prediction = [],
            seriesOptions_Sensor = [],
            name_Prediction = [],
            name_en_Prediction = [],
            names_Sensor = [],
            names_en_Sensor = [],
            url = urlPrefix + "/HealthPrediction/Search";

        //Clear previous chart
        if (chartSearchPrediction) {
            chartSearchPrediction.destroy();
        };
        if (chartSearchSensor) {
            chartSearchSensor.destroy();
        };

        //Settings for each search
        if ($(this).attr("id") == "SearchForHistory-item01") {
            //Prediction --- Parameters setting
            chartTitle = "分段关闭装置反馈";
            name_Prediction = "分段关闭装置反馈";
            name_en_Prediction = "FenDuanGuanBiZhuangZhi_1";

            //Sensor --- Parameters setting
            names_Sensor = ['并网工况','主配唯一反馈','导叶接力器关闭过程特性曲线'];
            names_en_Sensor = ['ElectroHydraulicFeedback_3','ParallelWorkingCondition_26','LeafServomotorFeedback_27'];
        }

        else if ($(this).attr("id") == "SearchForHistory-item02") {
            //Prediction --- Parameters setting
            chartTitle = "接力器反馈";
            name_Prediction = "接力器反馈";
            name_en_Prediction = "JieLiQiFanKui_2";

            //Sensor --- Parameters setting
            names_Sensor = ['接力器反馈'];
            names_en_Sensor = ['ServomotorFeedback_1'];
        }

        else if ($(this).attr("id") == "SearchForHistory-item03") {
            //Prediction --- Parameters setting
            chartTitle = "事故配压阀反馈";
            name_Prediction = "事故配压阀反馈";
            name_en_Prediction = "ShiGuPeiYaFa_3";

            //Sensor --- Parameters setting
            names_Sensor = ['导叶接力器反馈','事故信号（事故配压阀）'];
            names_en_Sensor = ['LeafServomotorFeedback_27','EmergencySignal_28'];
        }

        else if ($(this).attr("id") == "SearchForHistory-item04") {
            //Prediction --- Parameters setting
            chartTitle = "油泵电机健康状态";
            name_Prediction = "油泵电机健康状态";
            name_en_Prediction = "YouBengDianJi_4";

            //Sensor --- Parameters setting
            names_Sensor = ['软启动器工作状态','三相电流','三相电压'];
            names_en_Sensor = ['SoftLauncherStatus_23','OilPump3current_24','OilPump3Voltage_25'];
        }

        else if ($(this).attr("id") == "SearchForHistory-item05") {
            //Prediction --- Parameters setting
            chartTitle = "主配压阀健康状态";
            name_Prediction = "主配压阀健康状态";
            name_en_Prediction = "ZhuPeiYaFa_5";

            //Sensor --- Parameters setting
            names_Sensor = ['接力器反馈（接力器位移）','调节器输出信号','电液转换器反馈传感器','主配漏油量','导叶关闭时间','负荷---并网','平衡表（偏差）'];
            names_en_Sensor = ['ServomotorFeedback_1','RegulatorOutput_2','ElectroHydraulicFeedback_3','Leakage_4','ServomotorCloseTime_6','ParallelLoad_15','BalancedDashboard_17'];
        }

        else if ($(this).attr("id") == "SearchForHistory-item07") {
            //Prediction --- Parameters setting
            chartTitle = "油质污染状态";
            name_Prediction = "油质污染状态";
            name_en_Prediction = "YouZhiWuRan_7";

            //Sensor --- Parameters setting
            names_Sensor = ['油混水监测信号','杂质颗粒监测信号'];
            names_en_Sensor = ['TurbidWaterSignal_29','ImpurityParticlesSignal_30'];
        }

        else if ($(this).attr("id") == "SearchForHistory-item09") {
            //Prediction --- Parameters setting
            chartTitle = "引导阀健康状态";
            name_Prediction = "引导阀健康状态";
            name_en_Prediction = "YinDaoFa_9";

            //Sensor --- Parameters setting
            names_Sensor = ['调节器输出信号','电液转换器反馈传感器','油泵电机电流（电液转换器驱动器电流）','主配拒动开关'];
            names_en_Sensor = ['RegulatorOutput_2','ElectroHydraulicFeedback_3','OilPumpCurrent_7','MainRefuseOperation_32'];
        }



        //Get the Sensor and Prediction data for the initialization
        $.getJSON(url,{"type":"single","startTime":$("#query_start").val(),"endTime":$("#query_end").val(),"name":name_en_Prediction},function (data) {
            seriesOptions_Prediction[0] = {
                name: name_Prediction,
                data: data
            };
        });
        for (var i = 0; i <= names_en_Sensor.length - 1; i++) {
            $.ajaxSettings.async = false;
            $.getJSON(url,{"type":"multiple","startTime":$("#query_start").val(),"endTime":$("#query_end").val(),"name":names_en_Sensor[i]},function (data) {
                seriesOptions_Sensor[i] = {
                    name: names_Sensor[i],
                    data: data
                };
            });
        };


        chartSearchPrediction = new Highcharts.StockChart({
            chart: {
                renderTo: 'container_search_l',
                type: 'spline'
            },
            rangeSelector: {
                buttons: [{
                    type: 'all',
                    text: 'All'
                }],
                inputEnabled: false,
                selected: 0
            },
            title : {
                text : chartTitle
            },
            subtitle: {
                text : chartSubTitle
            },
            tooltip: {
                pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b><br/>',
                valueDecimals: 2
            },
            series: seriesOptions_Prediction
        });

        chartSearchSensor = new Highcharts.StockChart({
            chart: {
                renderTo: 'container_search_r',
                type: 'spline'
            },
            rangeSelector: {
                buttons: [{
                    type: 'all',
                    text: 'All'
                }],
                inputEnabled: false,
                selected: 0
            },
            title : {
                text : multipleChartTitle
            },
            subtitle: {
                text : chartSubTitle
            },
            tooltip: {
                pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b><br/>',
                valueDecimals: 2
            },
            series: seriesOptions_Sensor
        });

        //Unlock the button
        $(this).attr('disabled', false);

    });


    $(".liLeft").click(function(){
        // initialize
        var chartTitle,
            chartSubTitle = "实时数据",
            multipleChartTitle = "相关参数反馈",
            seriesOptions = [],
            seriesCounter = 0,
            itemNO,                    //The selection of prediction datum for the display
            names = [],
            names_en = [],
            url = urlPrefix + "/HealthPrediction/Dynamic";

        $(".liLeft").each(function(){
            $(this).removeClass("active");
        });
        $("#log").removeClass("active");
        $(this).addClass("active");
        $(".btn-primary").attr("id","SearchForHistory-"+$(this).attr("id"));
        $(".btn-primary").attr('disabled', false);

        //Clear previous chart
        $("#container_search_l").addClass("divInvisible");
        $("#container_search_r").addClass("divInvisible");
        $("#container_dynamic_l").removeClass("divInvisible");
        $("#container_dynamic_r").removeClass("divInvisible");
        $("#searchArea").removeClass("divInvisible");

        //remove
        if (chartDynamicPrediction) {
            clearInterval(intervalFunctionPrediction);
            chartDynamicPrediction.destroy();
        };
        if (chartDynamicSensor) {
            clearInterval(intervalFunctionSensor);
            chartDynamicSensor.destroy();
        };
        $("#historicRecord_wrapper").remove();


        // Settings for each click
        if ($(this).attr("id") == "item01") {
            //Prediction --- Parameters setting
            $("#DetailTitle").text("分段关闭装置");
            chartTitle = "分段关闭装置反馈";
            itemNO = 1;

            //Sensor --- Parameters setting
            names = ['并网工况','主配位移反馈','导叶接力器关闭过程特性曲线'];
            names_en = ['ElectroHydraulicFeedback_3','ParallelWorkingCondition_26','LeafServomotorFeedback_27'];
        }

        else if ($(this).attr("id") == "item02") {
            //Prediction --- Parameters setting
            $("#DetailTitle").text("接力器反馈");
            chartTitle = "接力器反馈";
            itemNO = 2;

            //Sensor --- Parameters setting
            names = ['接力器反馈'];
            names_en = ['ServomotorFeedback_1'];
        }

        else if ($(this).attr("id") == "item03") {
            //Prediction --- Parameters setting
            $("#DetailTitle").text("事故配压阀");
            chartTitle = "事故配压阀反馈";
            itemNO = 3;

            //Sensor --- Parameters setting
            names = ['导叶接力器反馈','事故信号（事故配压阀）'];
            names_en = ['LeafServomotorFeedback_27','EmergencySignal_28'];
        }

        else if ($(this).attr("id") == "item04") {
            //Prediction --- Parameters setting
            $("#DetailTitle").text("油泵电机");
            chartTitle = "油泵电机健康状态";
            itemNO = 4;

            //Sensor --- Parameters setting
            names = ['软启动器工作状态','三相电流','三相电压'];
            names_en = ['SoftLauncherStatus_23','OilPump3current_24','OilPump3Voltage_25'];
        }

        else if ($(this).attr("id") == "item05") {
            //Prediction --- Parameters setting
            $("#DetailTitle").text("主配压阀");
            chartTitle = "主配压阀健康状态";
            itemNO = 5;

            //Sensor --- Parameters setting
            names = ['接力器反馈（接力器位移）','调节器输出信号','电液转换器反馈传感器','主配漏油量','导叶关闭时间','负荷---并网','平衡表（偏差）'];
            names_en = ['ServomotorFeedback_1','RegulatorOutput_2','ElectroHydraulicFeedback_3','Leakage_4','ServomotorCloseTime_6','ParallelLoad_15','BalancedDashboard_17'];
        }

        else if ($(this).attr("id") == "item07") {
            //Prediction --- Parameters setting
            $("#DetailTitle").text("油质污染");
            chartTitle = "油质污染状态";
            itemNO = 7;

            //Sensor --- Parameters setting
            names = ['油混水监测信号','杂质颗粒监测信号'];
            names_en = ['TurbidWaterSignal_29','ImpurityParticlesSignal_30'];
        }

        else if ($(this).attr("id") == "item09") {
            //Prediction --- Parameters setting
            $("#DetailTitle").text("引导阀");
            chartTitle = "引导阀健康状态";
            itemNO = 9;

            //Sensor --- Parameters setting
            names = ['调节器输出信号','电液转换器反馈传感器','油泵电机电流（电液转换器驱动器电流）','主配拒动开关'];
            names_en = ['RegulatorOutput_2','ElectroHydraulicFeedback_3','OilPumpCurrent_7','MainRefuseOperation_32'];
        }





        //Get the Sensor data for the initialization
        seriesCounter = names_en.length;
        for (var i = 0; i <= seriesCounter - 1; i++) {
            $.ajaxSettings.async = false;
            $.getJSON(url,{"type":"multiple","id":startID_sensor-intialDataNum,"data":intialDataNum,"field":names_en[i]},function (data) {
                seriesOptions[i] = {
                    name: names[i],
                    data: data
                };
            });
        };
        startID_sensor = startID_sensor + 1;


        //Prediction chart options
        chartDynamicPrediction = new Highcharts.StockChart({
            chart : {
                renderTo: 'container_dynamic_l',
                type: 'spline',
                // animation: Highcharts.svg,
                events : {
                    load : function () {
                        // set up the updating of the chart each second
                        var series = this.series[0];
                        var point;
                        intervalFunctionPrediction = setInterval(function () {
                            $.ajaxSettings.async = false;
                            $.getJSON(url,{"type":"single","id":startID_prediction,"data":0},function(data){
                                $(".aLeft").each(function(index){
                                    if (data[index][1]==1) {
                                        $(this).removeClass("li-pos");
                                        $(this).removeClass("li-unknown");
                                        $(this).addClass("li-neg");
                                    }
                                    else if (data[index][1]==0){
                                        $(this).removeClass("li-neg");
                                        $(this).removeClass("li-unknown");
                                        $(this).addClass("li-pos");
                                    }
                                    else{
                                        $(this).removeClass("li-neg");
                                        $(this).removeClass("li-pos");
                                        $(this).addClass("li-unknown");
                                    }
                                point = data[itemNO-1];
                                TIMENOW = point[0];
                                });
                            })

                            series.addPoint(point, true, true);
                            startID_prediction = startID_prediction + 1;
                        }, 1000);
                    }
                }
            },

            rangeSelector: {
                buttons: [{
                    count: 1,
                    type: 'minute',
                    text: '1M'
                },{
                    type: 'all',
                    text: 'All'
                }],
                inputEnabled: false,
                selected: 0
            },

            title : {
                text : chartTitle
            },
            subtitle: {
                text : chartSubTitle
            },

            exporting: {
                enabled: false
            },

            tooltip: {
                pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b><br/>',
                valueDecimals: 2
            },

            series : [{
                name : chartTitle,
                data : (function () {
                    var data = [];
                    // $.ajaxSettings.async = false;
                    $.getJSON(url,{"type":"single","id":startID_prediction-intialDataNum,"data":intialDataNum},function(dataSeries){
                        for (var i = 1; i <= dataSeries.length; i++) {
                            if ((i%11)==itemNO) {
                                data.push(dataSeries[i-1]);
                            };
                        };
                    });
                    startID_prediction = startID_prediction + 1;
                    return data;
                }())
            }]
        });
        
        //Sensor chart options
        chartDynamicSensor = new Highcharts.StockChart({
            chart : {
                renderTo: 'container_dynamic_r',
                type: 'spline',
                // animation: Highcharts.svg,
                events : {
                    load : function () {
                        intervalFunctionSensor = setInterval(function () {
                            for (var i = 0; i <= seriesCounter - 1; i++) {
                                // set up the updating of the chart each second
                                var series = chartDynamicSensor.series[i];
                                $.ajaxSettings.async = false;
                                $.getJSON(url,{"type":"multiple","id":startID_sensor,"data":0,"field":names_en[i]},function(data){
                                    point = data[0];
                                })
                                series.addPoint(point, true, true);
                            };
                            startID_sensor = startID_sensor + 1;
                        }, 1000);
                    }
                }
            },

            rangeSelector: {
                buttons: [{
                    count: 1,
                    type: 'minute',
                    text: '1M'
                },{
                    type: 'all',
                    text: 'All'
                }],
                inputEnabled: false,
                selected: 0
            },

            title : {
                text : multipleChartTitle
            },
            subtitle: {
                text : chartSubTitle
            },

            exporting: {
                enabled: false
            },
            tooltip: {
                pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b><br/>',
                valueDecimals: 2
            },
            series: seriesOptions
        });

    });





    $("#log").click(function(){
        //initialize
        $(".liLeft").each(function(){
            $(this).removeClass("active");
        });
        $("#log").addClass("active");
        $(".btn-primary").attr("id","SearchForHistory-"+$(this).attr("id"));
        $(".btn-primary").attr('disabled', false);
        //Clear previous chart
        $("#container_search_l").addClass("divInvisible");
        $("#container_search_r").addClass("divInvisible");
        $("#container_dynamic_l").addClass("divInvisible");
        $("#container_dynamic_r").addClass("divInvisible");
        $("#searchArea").addClass("divInvisible");

        $("#historicRecord_wrapper").remove();

        //update page information
        $("#DetailTitle").text("历史记录查询");


        //create record
        url = urlPrefix + "/HealthPrediction/HistoryRecord";

        var table = $("<table>",{id:"historicRecord",class:"display",cellspacing:"0",width:"100%"});
        var field = $("<tr></tr>").append("<th>发生时间</th><th>健康状态异常预测</th><th>备注</th>");
        var tableHead = $("<thead></thead>").append(field);
        var record = $("<tbody></tbody>");
        table.append(tableHead);
        $.ajaxSettings.async = false;
        $.getJSON(url,{"currentTime":TIMENOW},function(data){
            for (var i = 0; i < data.length; i++) {
                var time = new Date(data[i][0]*1000);
                time.setHours(time.getHours()+12);
                time = time.getFullYear()+"-"+
                        ((time.getMonth()+1)>9?(time.getMonth()+1):"0"+(time.getMonth()+1))+"-"+
                        (time.getDate()>9?time.getDate():"0"+time.getDate())+" "+
                        (time.getHours()>9?time.getHours():"0"+time.getHours())+":"+
                        (time.getMinutes()>9?time.getMinutes():"0"+time.getMinutes())+":"+
                        (time.getSeconds()>9?time.getSeconds():"0"+time.getSeconds());
                var datum = $("<tr></tr>").append("<th>" + time + "</th><th>" + data[i][1] + "</th><th>无</th>");
                record.append(datum);
            };
            table.append(record);
        });
        $('#displayArea').append(table);
        $('#historicRecord').DataTable({
            "order": [[ 0, "desc" ]]
        });




    });

    
        
    
    
});