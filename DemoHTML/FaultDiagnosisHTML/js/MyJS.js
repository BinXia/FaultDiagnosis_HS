$(function () {

    //All: global variable for each section
    var urlPrefix = "http://127.0.0.1:8000",
        url,
        TIMENOW;

    //Dynamic: $(".liLeft").click
    var chartDynamicSensor,
        intervalFUnctionSensor,
        startID_prediction = 91,
        startID_sensor = 91,
        intialDataNum = 90,
        isPause = false,
        reinitialize,
        reinitialize = $('#dynamicRecords').DataTable({
                            "bDestroy": true,
                            "iDisplayLength" : 5,
                            "order": [[ 0, "desc" ]],
                            "stateSave": true
                        });

    //Search: $(".btn-primary").click
    var chartSearchSensor,
        isSearch = true,
        time_Datetime;

    //History record: $("#log").click
    var tableForRecord;

    //Get all the data from the database
    var sensor_all,
        prediction_all,
        log_all,
        log_all_backup;
    url = urlPrefix + "/HealthPrediction/Dynamic";
    $.ajaxSettings.async = false;
    $.getJSON(url,{"type":"multiple_all","id":1,"data":1800},function(data){
        sensor_all = data;
    });
    $.getJSON(url,{"type":"single_all","id":1,"data":1800},function(data){
        prediction_all = data;
    });
    url = urlPrefix + "/HealthPrediction/HistoryRecord";
    $.getJSON(url,{"currentTime":0},function(data){
        log_all = data;
        log_all_backup = data;
    });


    // Convert timestamp to MySql Datetime
    Date.prototype.toDATETIME = function() {
        this.setHours(this.getHours());
        this.DATETIME = this.getFullYear()+"-"+
                        ((this.getMonth()+1)>9?(this.getMonth()+1):"0"+(this.getMonth()+1))+"-"+
                        (this.getDate()>9?this.getDate():"0"+this.getDate())+" "+
                        (this.getHours()>9?this.getHours():"0"+this.getHours())+":"+
                        (this.getMinutes()>9?this.getMinutes():"0"+this.getMinutes())+":"+
                        (this.getSeconds()>9?this.getSeconds():"0"+this.getSeconds());
    }

    // pause and restart
    $("#StatusSwitch").click(function(){
        isPause = !isPause;
        if (isPause) {
            $(this).text("开始");
        }
        else{
            $(this).text("暂停");
        };
    });

    $('#dynamicRecords tbody').on('click', 'tr', function () {
        time_Datetime = $('td', this).eq(0).text();
        isSearch = false;
        $(".search").click();
    });



    //搜索相应时段信息
    $(".search").click(function(){
        //Lock the button
        $(this).attr('disabled', true);
        $("#container_search_r").removeClass("divInvisible");

        //initialize
        var chartTitle,
            chartSubTitle = "历史记录",
            multipleChartTitle = "相关参数反馈",
            seriesOptions_Sensor = [],
            names_Sensor = [],
            names_en_Sensor = [],
            url = urlPrefix + "/HealthPrediction/Search",
            startTime,
            endTime;

        //Clear previous chart
        if (chartSearchSensor) {
            chartSearchSensor.destroy();
        };

        //Settings for each search
        if ($(this).attr("id") == "SearchForHistory-item01") {
            //Sensor --- Parameters setting
            names_Sensor = ['并网工况','主配唯一反馈','导叶接力器关闭过程特性曲线'];
            names_en_Sensor = ['ElectroHydraulicFeedback_3','ParallelWorkingCondition_26','LeafServomotorFeedback_27'];
        }

        else if ($(this).attr("id") == "SearchForHistory-item02") {
            //Sensor --- Parameters setting
            names_Sensor = ['接力器反馈'];
            names_en_Sensor = ['ServomotorFeedback_1'];
        }

        else if ($(this).attr("id") == "SearchForHistory-item03") {
            //Sensor --- Parameters setting
            names_Sensor = ['导叶接力器反馈','事故信号（事故配压阀）'];
            names_en_Sensor = ['LeafServomotorFeedback_27','EmergencySignal_28'];
        }

        else if ($(this).attr("id") == "SearchForHistory-item04") {
            //Sensor --- Parameters setting
            names_Sensor = ['软启动器工作状态','三相电流','三相电压'];
            names_en_Sensor = ['SoftLauncherStatus_23','OilPump3current_24','OilPump3Voltage_25'];
        }

        else if ($(this).attr("id") == "SearchForHistory-item05") {
            //Sensor --- Parameters setting
            names_Sensor = ['接力器反馈（接力器位移）','调节器输出信号','电液转换器反馈传感器','主配漏油量','导叶关闭时间','负荷---并网','平衡表（偏差）'];
            names_en_Sensor = ['ServomotorFeedback_1','RegulatorOutput_2','ElectroHydraulicFeedback_3','Leakage_4','ServomotorCloseTime_6','ParallelLoad_15','BalancedDashboard_17'];
        }

        else if ($(this).attr("id") == "SearchForHistory-item07") {
            //Sensor --- Parameters setting
            names_Sensor = ['油混水监测信号','杂质颗粒监测信号'];
            names_en_Sensor = ['TurbidWaterSignal_29','ImpurityParticlesSignal_30'];
        }

        else if ($(this).attr("id") == "SearchForHistory-item09") {
            //Sensor --- Parameters setting
            names_Sensor = ['调节器输出信号','电液转换器反馈传感器','油泵电机电流（电液转换器驱动器电流）','主配拒动开关'];
            names_en_Sensor = ['RegulatorOutput_2','ElectroHydraulicFeedback_3','OilPumpCurrent_7','MainRefuseOperation_32'];
        }



        //Get the Sensor data for the search
        if (isSearch) {
            for (var i = 0; i <= names_en_Sensor.length - 1; i++) {
                $.ajaxSettings.async = false;
                $.getJSON(url,{"type":"multiple","startTime":$("#query_start").val(),"endTime":$("#query_end").val(),"name":names_en_Sensor[i]},function (data) {
                    seriesOptions_Sensor[i] = {
                        name: names_Sensor[i],
                        data: data
                    };
                });
            };
        }
        else{
            startTime = new Date(time_Datetime);
            endTime = new Date(time_Datetime);
            startTime.setMinutes(startTime.getMinutes()-1);
            endTime.setMinutes(endTime.getMinutes()+1);
            startTime = Date.parse(startTime);
            endTime = Date.parse(endTime);
            for (var i = 0; i <= names_en_Sensor.length - 1; i++) {
                $.ajaxSettings.async = false;
                $.getJSON(url,{"type":"multiple","startTime":startTime,"endTime":endTime,"name":names_en_Sensor[i]},function (data) {
                    seriesOptions_Sensor[i] = {
                        name: names_Sensor[i],
                        data: data
                    };
                });
            };
        };
        

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

        //Unlock the button and Reset isSearch
        $(this).attr('disabled', false);
        isSearch = true;

    });


    $(".liLeft").click(function(){
        // initialize
        var chartTitle,
            chartSubTitle = "实时数据",
            multipleChartTitle = "相关参数反馈",
            seriesOptions = [],
            seriesCounter = 0,
            itemNO,                    //The selection of prediction datum for the display
            itemName,
            names = [],
            names_en = [],
            names_i = [],
            url = urlPrefix + "/HealthPrediction/Dynamic";

        $(".liLeft").each(function(){
            $(this).removeClass("active");
        });
        $("#log").removeClass("active");
        $(this).addClass("active");
        $(".btn-primary").attr("id","SearchForHistory-"+$(this).attr("id"));
        $(".btn-primary").attr('disabled', false);

        //Clear previous chart
        $("#container_search_r").addClass("divInvisible");
        $("#records_dynamic_l").removeClass("divInvisible");
        $("#container_dynamic_r").removeClass("divInvisible");
        $("#searchArea").removeClass("divInvisible");
        if (chartDynamicSensor) {
            clearInterval(intervalFunctionSensor);
            chartDynamicSensor.destroy();
        };
        $("#historicRecord_wrapper").remove();
        reinitialize.clear();
        log_all = log_all_backup.slice();


        // Settings for each click
        if ($(this).attr("id") == "item01") {
            //Prediction --- Parameters setting
            $("#DetailTitle").text("分段关闭装置");
            itemName = "分段关闭装置";
            itemNO = 1;

            //Sensor --- Parameters setting
            names = ['并网工况','主配位移反馈','导叶接力器关闭过程特性曲线'];
            names_en = ['ElectroHydraulicFeedback_3','ParallelWorkingCondition_26','LeafServomotorFeedback_27'];
            names_i = [3,26,27];
        }

        else if ($(this).attr("id") == "item02") {
            //Prediction --- Parameters setting
            $("#DetailTitle").text("接力器反馈");
            itemName = "接力器反馈";
            itemNO = 2;

            //Sensor --- Parameters setting
            names = ['接力器反馈'];
            names_en = ['ServomotorFeedback_1'];
            names_i = [1];
        }

        else if ($(this).attr("id") == "item03") {
            //Prediction --- Parameters setting
            $("#DetailTitle").text("事故配压阀");
            itemName = "事故配压阀";
            itemNO = 3;

            //Sensor --- Parameters setting
            names = ['导叶接力器反馈','事故信号（事故配压阀）'];
            names_en = ['LeafServomotorFeedback_27','EmergencySignal_28'];
            names_i = [27,28];
        }

        else if ($(this).attr("id") == "item04") {
            //Prediction --- Parameters setting
            $("#DetailTitle").text("油泵电机");
            itemName = "油泵电机";
            itemNO = 4;

            //Sensor --- Parameters setting
            names = ['软启动器工作状态','三相电流','三相电压'];
            names_en = ['SoftLauncherStatus_23','OilPump3current_24','OilPump3Voltage_25'];
            names_i = [24,25];
        }

        else if ($(this).attr("id") == "item05") {
            //Prediction --- Parameters setting
            $("#DetailTitle").text("主配压阀");
            itemName = "主配压阀";
            itemNO = 5;

            //Sensor --- Parameters setting
            names = ['接力器反馈（接力器位移）','调节器输出信号','电液转换器反馈传感器','主配漏油量','导叶关闭时间','负荷---并网','平衡表（偏差）'];
            names_en = ['ServomotorFeedback_1','RegulatorOutput_2','ElectroHydraulicFeedback_3','Leakage_4','ServomotorCloseTime_6','ParallelLoad_15','BalancedDashboard_17'];
            names_i = [1,2,3,4,6,15,17];
        }

        else if ($(this).attr("id") == "item07") {
            //Prediction --- Parameters setting
            $("#DetailTitle").text("油质污染");
            itemName = "油质污染";
            itemNO = 7;

            //Sensor --- Parameters setting
            names = ['油混水监测信号','杂质颗粒监测信号'];
            names_en = ['TurbidWaterSignal_29','ImpurityParticlesSignal_30'];
            names_i = [29,30];
        }

        else if ($(this).attr("id") == "item09") {
            //Prediction --- Parameters setting
            $("#DetailTitle").text("引导阀");
            itemName = "引导阀";
            itemNO = 9;

            //Sensor --- Parameters setting
            names = ['调节器输出信号','电液转换器反馈传感器','油泵电机电流（电液转换器驱动器电流）','主配拒动开关'];
            names_en = ['RegulatorOutput_2','ElectroHydraulicFeedback_3','OilPumpCurrent_7','MainRefuseOperation_32'];
            names_i = [2,3,7,32];
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
        
        //Sensor chart options
        chartDynamicSensor = new Highcharts.StockChart({
            chart : {
                renderTo: 'container_dynamic_r',
                type: 'spline',
                // animation: Highcharts.svg,
                events : {
                    load : function () {
                        intervalFunctionSensor = setInterval(function () {
                            if (!isPause){
                                // update prediction
                                $(".aLeft").each(function(index){
                                    if (prediction_all[startID_prediction-1][index+1]==1) {
                                        $(this).removeClass("li-pos");
                                        $(this).removeClass("li-unknown");
                                        $(this).addClass("li-neg");
                                    }
                                    else if (prediction_all[startID_prediction-1][index+1]==0){
                                        $(this).removeClass("li-neg");
                                        $(this).removeClass("li-unknown");
                                        $(this).addClass("li-pos");
                                    }
                                    else{
                                        $(this).removeClass("li-neg");
                                        $(this).removeClass("li-pos");
                                        $(this).addClass("li-unknown");
                                    }
                                });
                                startID_prediction = startID_prediction + 1;

                                // update related parameters
                                for (var i = 0; i <= seriesCounter - 1; i++) {
                                    // set up the updating of the chart each second
                                    var series = chartDynamicSensor.series[i];
                                    point = [sensor_all[startID_sensor-1][0],sensor_all[startID_sensor-1][names_i[i]]];
                                    series.addPoint(point, true, true);
                                };
                                TIMENOW = point[0];
                                startID_sensor = startID_sensor + 1;

                                // update log
                                reinitialize.destroy();
                                for (var i = log_all.length-1; i >= 0 ; i--) {
                                    if ((log_all[i][0]*1000) < TIMENOW) {
                                        if (log_all[i][1] == itemName) {
                                            var time = new Date(log_all[i][0]*1000);
                                            time.toDATETIME();
                                            var datum = $("<tr></tr>").append("<td>" + time.DATETIME + "</td><td>" + log_all[i][1] + "</td><td>" + log_all[i][2] + "</td><td>" + log_all[i][3] + "</td>");
                                            $("#Record").append(datum);
                                            log_all.splice(i,1);
                                        }
                                        else{
                                            continue;
                                        };
                                    }
                                    else{
                                        break;
                                    };
                                };

                                reinitialize = $('#dynamicRecords').DataTable({
                                    "bDestroy": true,
                                    "iDisplayLength" : 5,
                                    "order": [[ 0, "desc" ]],
                                    "stateSave": true
                                });

                            }
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
        $("#records_dynamic_l").addClass("divInvisible");
        $("#container_search_r").addClass("divInvisible");
        $("#container_dynamic_r").addClass("divInvisible");
        $("#searchArea").addClass("divInvisible");
        $("#historicRecord_wrapper").remove();

        //update page information
        $("#DetailTitle").text("历史记录查询");


        //create record
        url = urlPrefix + "/HealthPrediction/HistoryRecord";

        var table = $("<table>",{id:"historicRecord",class:"display",cellspacing:"0",width:"100%"});
        var field = $("<tr></tr>").append("<th>发生时间</th><th>设备</th><th>健康状态异常预测</th><th>备注</th>");
        var tableHead = $("<thead></thead>").append(field);
        var record = $("<tbody></tbody>");
        table.append(tableHead);
        $.ajaxSettings.async = false;
        $.getJSON(url,{"currentTime":TIMENOW},function(data){
            for (var i = 0; i < data.length; i++) {
                var time = new Date(data[i][0]*1000);
                time.toDATETIME();
                var datum = $("<tr></tr>").append("<td>" + time.DATETIME + "</td><td>" + data[i][1] + "</td><td>" + data[i][2] + "</td><td>" + data[i][3] + "</td>");
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