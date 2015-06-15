$(function () {
	// Parameters: HealthPrediction
	// var 

	// Parameters: createHealthFigure
	var nodes = [],
		edges = [],
		network;

	// Parameters: Tables
	var Parameters_table,
		Equipments_table;

	var createHealthFigure = function() {
			// Instantiate our network object.
			var container = document.getElementById('RelationStructure');
			var data = {
				nodes: nodes,
				edges: edges
			};
			var options = {
				// stabilize: false,   // stabilize positions before displaying
				nodes: {
		          radiusMin: 16,
		          radiusMax: 32,
		          fontColor: '#2B1B17'
		        },
				edges: {
					color: '#A0A0A0'
				},
				groups: {
		          equipments: {
		            shape: 'triangle',
		            color: '#FF9900'
		          },
		          parameters: {
		            shape: 'dot',
		          }
		        }
			};
			network = new vis.Network(container, data, options);
		},
		createTables = function() {
			var outerDIV = $("<div>",{id:"tableList"});
			var tableHead = $("<thead></thead>");
			var equ_table = $("<table>",{id:"EquipmentsList",class:"display",cellspacing:"0",width:"300px"});
	        var equ_record = $("<tbody>",{id:"Equ_Record"});
	        var par_table = $("<table>",{id:"ParametersList",class:"display",cellspacing:"0",width:"300px"});
	        var par_record = $("<tbody>",{id:"Par_Record"});
	        equ_table.append(tableHead).append(equ_record);
	        par_table.append(tableHead).append(par_record);
	        outerDIV.append(equ_table).append(par_table);
	        $("#displayArea").append(outerDIV);
		}



	$('#ParametersList tbody').on('click', 'tr', function () {
        var point = $('td', this).eq(0).text();
        var options = {
            // position: {x:positionx,y:positiony}, // this is not relevant when focusing on nodes
            scale: 1.0,
            animation: {
                duration: 2500,
                easingFunction: 'easeOutQuad'
            }
        }
        network.focusOnNode(point, options);
        network.selectNodes([point]);
    });

    $('#Equ_Record').on('click', 'tr', function () {
        var point = parseInt($('td', this).eq(0).text()) + 100;
        var options = {
            // position: {x:positionx,y:positiony}, // this is not relevant when focusing on nodes
            scale: 1.0,
            animation: {
                duration: 2500,
                easingFunction: 'easeOutQuad'
            }
        }
        network.focusOnNode(point, options);
        network.selectNodes([point]);
    });


	$(".liLeft").click(function(){
		// initialize
		var Equipments_count,
			Equipments,
			Equipments_details,
			Parameters_count,
			Parameters,
			Parameters_details,
			Relationship = [];
		nodes = [];
		edges = [];
		$(".liLeft").each(function(){
            $(this).removeClass("active");
        });
        $(this).addClass("active");
        // if (Parameters_table) {Parameters_table.clear();};
        // if (Equipments_table) {Equipments_table.clear();};
        // if ($("#tableList")) {$("#tableList").remove();};
        // createTables();



        if ($(this).attr("id") == "item01") {
        	// initialize
        	$("#DetailTitle").text("健康预测-决策关系结构图");
        	Equipments_count = 11;
        	Equipments = ['分段关闭装置',
        				  '接力器反馈',
        				  '事故配压阀',
        				  '油泵电机',
        				  '主配压阀',
        				  '主接力器',
        				  '油质污染',
        				  '无油电转',
        				  '引导阀',
        				  '组合阀',
        				  '油泵'];
        	Equipments_details = ['分段关闭装置',
		        				  '接力器反馈',
		        				  '事故配压阀',
		        				  '油泵电机',
		        				  '主配压阀',
		        				  '主接力器',
		        				  '油质污染',
		        				  '无油电转',
		        				  '引导阀',
		        				  '组合阀',
		        				  '油泵'];
        	Parameters_count = 32;
        	Parameters = ['接力器反馈',
        				  '调节器输出信号',
        				  '电液转换器反馈传感器',
        				  '主配漏油量',
        				  '接力器端盖',
        				  '导叶关闭时间',
        				  '油泵电机电流',
        				  '回油箱油位正常液位',
        				  '油泵输油量1',
        				  '油泵输油量2',
        				  '油泵电机运行工况',
        				  '油泵电机电流',
        				  '排油阀门',
        				  'PID调节器负荷',
        				  '并网负荷',
        				  '停机状态',
        				  '平衡表',
        				  '油位',
        				  '油泵负载状态',
        				  '油泵停机状态',
        				  '油流量',
        				  '卸载时间',
        				  '软启动器工作状态',
        				  '三相电流',
        				  '三相电压',
        				  '并网工况',
        				  '导叶接力器反馈',
        				  '事故信号',
        				  '油混水监测信号',
        				  '杂质颗粒监测信号',
        				  '漏油箱液位',
        				  '主配拒动开关'];
        	Parameters_details = ['接力器反馈（接力器位移）---接力器',
								  '调节器输出信号---调节器',
								  '电液转换器反馈传感器---电液转换器、伺服电机',
								  '主配漏油量---管路漏油量检测传感器',
								  '接力器端盖---接力器',
								  '导叶关闭时间（主配关闭最大行程）---接力器、伺服电机',
								  '油泵电机电流（电液转换器驱动器电流）---油泵电机',
								  '回油箱油位正常液位',
								  '油泵输油量1',
								  '油泵输油量2',
								  '油泵电机运行工况（起、停机）',
								  '油泵电机电流',
								  '排油阀门',
								  '负荷---PID调节器',
								  '负荷---并网',
								  '停机状态',
								  '平衡表（偏差）--- 调节器输出信号与导叶接力器反馈信号差值',
								  '油位---回油箱',
								  '负载状态---油泵',
								  '停机状态---油泵',
								  '油流量---组合阀至压力油罐的流量传感器',
								  '卸载时间---油泵电机',
								  '软启动器工作状态---软启动器',
								  '三相电流---油泵电机',
								  '三相电压---油泵电机',
								  '并网工况',
								  '导叶接力器反馈',
								  '事故信号（事故配压阀）',
								  '油混水监测信号---混水传感器',
								  '杂质颗粒监测信号---油质检测仪',
								  '漏油箱液位',
								  '主配拒动开关'];
			Relationship = [[3,26,27],
							[1],
							[27,28],
							[24,25],
							[1,2,3,4,6,15,17,106],
							[1,5,13,14,16],
							[29,30],
							[],
							[2,3,7,32],
							[8,9,10,18,19,20,21,22],
							[]];
        }

		else if ($(this).attr("id") == "item02") {
			// initialize
        	$("#DetailTitle").text("故障诊断-决策关系结构图");
		}
        

		// create tables
		for (var i = 1; i <= Equipments_count; i++) {
			var datum = $("<tr></tr>").append("<td>" + i + "</td><td>" + Equipments[i-1] + "</td>");
			$("#Equ_Record").append(datum);
		};
		Equipments_table = $('#EquipmentsList').DataTable({
                            "bDestroy": true,
                            "iDisplayLength" : 10,
                            "ordering": false,
                            "bFilter": false,
                            "scrollY": "250px",
					        "scrollCollapse": true,
					        "paging": false,
					        "aoColumns": [
					            { "sTitle": "设备编号", "sClass": "right"},
					            { "sTitle": "名称", "sClass": "left"}
					        ]
                        });
		for (var i = 1; i <= Parameters_count; i++) {
			var datum = $("<tr></tr>").append("<td>" + i + "</td><td>" + Parameters[i-1] + "</td>");
			$("#Par_Record").append(datum);
		};
		Parameters_table = $('#ParametersList').DataTable({
                            "bDestroy": true,
                            "autoWidth": false,
                            "iDisplayLength" : 10,
                            "ordering": false,
                            "bFilter": false,
                            "scrollY": "250px",
					        "scrollCollapse": true,
					        "paging": false,
					        "aoColumns": [
					            { "sTitle": "参数编号", "sClass": "right"},
					            { "sTitle": "名称", "sClass": "left"}
					        ]
                        });



		// create network structure
		for (var i = 1; i <= Parameters_count; i++) {
			nodes.push({id: i, value: 1, label: Parameters[i-1], title: Parameters_details[i-1], group: 'parameters'});
		};
		for (var i = 1; i <= Equipments_count; i++) {
			nodes.push({id: i+100, value: 1, label: Equipments[i-1], title: Equipments_details[i-1], group: 'equipments'});
		};
		for (var index_e = 0; index_e < Relationship.length; index_e++) {
			for (var index_p = 0; index_p < Relationship[index_e].length; index_p++) {
				edges.push({from: index_e+101, to: Relationship[index_e][index_p], value: 1, title: '相关'});
			};
		};
		createHealthFigure();


	});

})