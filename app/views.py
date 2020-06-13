from django.shortcuts import render
import pandas as pd
from reportclass.factory_revenue import *
from reportclass.operation_report import *
from reportclass.hydro_report import *
from reportclass.summary_report import *
import datetime 
from . models import RptOperators,RptMonthlyPlan
import numpy as np
import re

#Factory Revenue View
def factory_revenue_view(request):

	#list to hold month wise data
	month_data=[]
	#list to hold month wise data after converting object into dictionary
	month_data_dict=[]
	
	#read excel
	df3=pd.read_excel('VC_2020.xlsx',header=None,skiprows=range(0,15),skipfooter=1)
	k=0
	#iterate over each row
	for i in df3.values:
		#set attribute values
		mon=factory_revenue_by_month(i[0])
		mon.mn_dk=i[1]
		mon.q_tb=i[2]
		mon.product_delivered_plan=i[3]
		mon.product_delivered_made=i[4]
		mon.product_delivered_rate=mon.get_product_delivered_rate
		mon.revenue_plan = i[6]
		mon.revenue_made = i[7]
		mon.revenue_rate=mon.get_revenue_rate
		mon.product_received = i[9]
		mon.working_time = i[10]

		#add the object inside month data list and object converted to dictionary using vars to month_data_dict
		month_data.append(mon)
		month_data_dict.append(vars(mon))

	#create factory revenue object
	factory=factory_revenue('company', 'factory', 'short', '5/30/2020')
	#set its attribute
	factory.list_of_data_by_month=month_data
	factory.mn_tl= 0
	factory.q_tb = 0
	factory.product_delivered = 0
	factory.product_received = 0
	factory.revenue = 0
	factory.working_time = 0
	factory.cs_tb = 90
	#create complete summary total
	factory.create_summary()

	return render(request,'factory_report.html',{'summary_row':vars(factory.summary_row),'factory':factory,'month_data':month_data_dict})


def operation_view(request):
	df=pd.read_excel('VC_2020.xlsx',header=None,skiprows=range(0,12),sheet_name='VC_Operation',nrows=24,na_filter=False)#6
	operation_data_list=[]
	operation_data_dict=[]

	for i in df.values:
		
			obj=OperationRevenue(i[0])
			obj.output_delivered = i[1]
			obj.output_received = i[2]
			obj.running_time = i[3]
			obj.price_boundary = i[4]
			obj.can_price = i[5]
			obj.expected_revenue = i[6]
			obj.operation_problem = i[7]
			obj.unusual_event = i[8]
			obj.head_shift = i[9]
			operation_data_list.append(obj)
			operation_data_dict.append(vars(obj))


	operation=OperationRevenueData(3,57.0,11.09,245.9,1069.000)
	
	return render(request,'operation_report.html',{'operation':operation,'operation_data':operation_data_dict})

def hydro_view(request):
	df=pd.read_excel('VC_2020.xlsx',header=None,skiprows=range(0,15),sheet_name='VC_Flow',nrows=24,na_filter=False)
	hydro_data_dict=[]
	
	for i in df.values:

		obj=HydroDayReport(i[0])
		obj.upstream = i[1]
		obj.downstream = i[2]
		obj.back_to_lake = i[3]
		obj.rinse_unit = i[4]
		obj.discharge_overflow = i[5]
		obj.minimum_discharge = i[6]
		obj.whi = i[7]
		
		hydro_data_dict.append(vars(obj))


	hydro_general = HydroReportData('CÔNG TY CỔ PHẦN THỦY ĐIỆN VĂN CHẤN ','NHÀ MÁY THỦY ĐIỆN VĂN CHẤN',230,227,45.7,4000,5.09,0.99,4.1)
	
	return render(request,'hydro_report.html',{'day_data' : hydro_data_dict,'hydro_general':hydro_general})

def summary_view(request):
	df=pd.read_excel('summaryreport.xlsx',skiprows=range(0,5),na_filter=False,skipfooter=21)
	
	power_plant_list=[]
	summary_dict=[]
	
	for data in df.values:
		obj=SummaryPowerPlant(data[1],'A','CỤM NHÀ MÁY TRÊN 30MW / IN-MARKET PLANTS (≥30MW)')#data[1],data[2],data[3],data[4],data[5],data[6])
		obj.set_daily_data(data[2],data[3],data[4],data[5],data[6])
		
		i=1
		for col in range(7,72+7,6):
			obj.add_month(data[col],data[col+1],data[col+3],data[col+4])
		
			i+=1
			
		obj.set_year()
		
		power_plant_list.append(obj)

	
	df2=pd.read_excel('summaryreport.xlsx',skiprows=range(0,18),na_filter=False,skipfooter=14)
	for data in df2.values:
		obj=SummaryPowerPlant(data[1],'B','CỤM NHÀ MÁY TRÊN 30MW / IN-MARKET PLANTS (≥30MW)')#data[1],data[2],data[3],data[4],data[5],data[6])
		obj.set_daily_data(data[2],data[3],data[4],data[5],data[6])
		i=1
		for col in range(7,72+7,6):
			obj.add_month(data[col],data[col+1],data[col+3],data[col+4])
			
			i+=1
		obj.set_year()
		
		power_plant_list.append(obj)

		group_A=SummaryByGroup()
		group_B=SummaryByGroup()
		for  plants in power_plant_list:
			if plants.group_id == 'A':
				group_A.add_plant(plants)
			else:
				group_B.add_plant(plants)
	
		group_A.set_plant_total()
		group_B.set_plant_total()

		complete_summary=SummaryTotalPlants()
		complete_summary.add_group_summary(group_B)
		complete_summary.add_group_summary(group_A)
		complete_summary.set_plant_total()
		

	return render(request,'summary_report.html',{'report_date':'06/06/2020','complete_summary':complete_summary})

def set_number(number):
	if pd.isnull(number) or str(number).strip()=='':
		return None

	else:
		res=re.sub('[^0-9.]','',str(number))
		if res!='':
			return float(res)
		else:
			return None
	

def import_excel(excel_file,from_date,to_date,kvgs_id):

		df=pd.read_excel(excel_file,None)
		
		sheet_names = list(df.keys()) #fecth name of the sheets
		if len(sheet_names)<3:
			return "Sheets missing in Uploaded Excel"

		sheet1,sheet2,sheet3=  sheet_names[0],sheet_names[1],sheet_names[2]
		
		
		#read 2nd sheet	
		df1=pd.read_excel(excel_file,sheet_name=sheet2)
		
		index = 0
		start_index = 0
		end_index = 0
		
		#extract rows between from date and to date
		for row in df1.values:
			if isinstance(row[0],(datetime.datetime,)):
				
				if row[0].date()==from_date.date():
					start_index=index

				if row[0].date() == to_date.date():
					end_index=index
					break

			index +=1
	
		#read 3rd sheet
		df2=pd.read_excel(excel_file,sheet_name=sheet3)
		index = 0
		start_index2 = 0
		end_index2 = 0

		#extract rows between from date and to date in 3rd sheet
		for row in df2.values:
			if isinstance(row[0],(datetime.datetime,)):
				if row[0].date()==from_date.date():
					
					start_index2=index

				if row[0].date() == to_date.date():
					end_index2=index
					break

			index +=1
		
		#if details not found
		if start_index == 0 or start_index2 ==0:
			return 'Details Not Found'
		

		months=['Tháng 01','Tháng 02','Tháng 03','Tháng 04','Tháng 05','Tháng 06','Tháng 07']
		months.extend(['Tháng 08','Tháng 09','Tháng 10','Tháng 11','Tháng 12'])
		
		result2 =[] #to store 2nd sheet data
		result = [] #to store 3rd sheet data

		#excluding month data, store remaining in the list
		for row in df1.values[start_index:end_index+25]:
			if row[0] not in months:
				result.append(row)

		#excluding month data, store remaining in the list
		for row in df2.values[start_index2:end_index2+25]:
			if row[0] not in months:
				result2.append(row)
			

		for index in range(0,len(result),25):
			day=result[index][0].day
			month=result[index][0].month
			year=result[index][0].year
			
			check_present=RptOperators.objects.filter(id_kvgs=kvgs_id ,report_datetime__day=day,report_datetime__month=month,report_datetime__year=year)
		 
		 	#if rows are  prsent in the table 
			if (len(check_present)!=0):
				check_present.delete()

			hour=0
			for row_index in range(index+1,index+24+1):
				date=datetime.date(year,month,day)
				print(date,hour)
			
				hour +=1
				RptOperators.objects.create(
					id_kvgs = kvgs_id,
					report_datetime = date,
					sl_giao = set_number(result[row_index][1]),
					sl_nhan = set_number(result[row_index][2]),
					thoigian_chay_may = set_number(result[row_index][3]),
					gia_bien_he_thong = set_number(result[row_index][4]),
					gia_can = set_number(result[row_index][5]),
					doanh_thu_du_kien = set_number(result[row_index][6]),
					su_co_van_hanh = set_number(result[row_index][7]),
					su_kien_bat_thuong = set_number(result[row_index][8]),
					rp_hour = hour,
					mn_tl = set_number(result2[row_index][1]),
					mn_hl = set_number(result2[row_index][2]),
					ll_ve_ho = set_number(result2[row_index][3]),
					ll_tuabin =  set_number(result2[row_index][4]),
					ll_xa_tran = set_number(result2[row_index][5]),
					ll_xa_toi_thieu = set_number(result2[row_index][6]),
					w_hi = set_number(result2[row_index][7])
					)
		
		#first sheet part
		data = []
		df3 = pd.read_excel(excel_file,sheet_name=sheet1)
		year = from_date.year
		for row in df3.values:
			if row[0] in months:
				month = int(row[0].split()[1])
				production_plan = float(str(row[3]).replace(',','')) if row[3]!='Chưa TH' or str(row[3]).strip()!='' else None
				revenue_plan = float(str(row[6]).replace(',','')) if row[6]!='Chưa TH' or str(row[6]).strip()!='' else None

				try: 
					obj = RptMonthlyPlan.objects.get(id_kvgs=kvgs_id,year=year,month=month)
					if production_plan!= None:
						obj.production_plan = production_plan
					if revenue_plan!= None:
						obj.revenue_plan = revenue_plan
					obj.save()
				

				except:
					RptMonthlyPlan.objects.create(
						id_kvgs=kvgs_id,
						year=year,
						month=month,
						production_plan=production_plan,
						revenue_plan=revenue_plan
					)

		return 'Details Uploaded'	

def operation_import_view(request):
	if request.method == 'POST' and request.FILES['excel']:
		from_date = datetime.datetime.strptime(request.POST.get('from_date'),'%Y-%m-%d')
		to_date =datetime.datetime.strptime(request.POST.get('to_date'),'%Y-%m-%d')
		excel_file = request.FILES['excel']
		#kvgs_id = request.POST.get('kvgs_id')
		kvgs_id = 6
		res = import_excel(excel_file,from_date,to_date,kvgs_id)

		return render(request,'operation_import.html',{'message':res})
	else:
		return render(request,'operation_import.html')