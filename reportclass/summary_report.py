from math import isnan

class DailySummary:

	def __init__(self,elevation,average_daily_flow,daily_power_generation,daily_revenue_generation,daily_avergate_power):
		self.elevation = elevation
		self.average_daily_flow = average_daily_flow
		self.daily_power_generation = daily_power_generation
		self.daily_revenue_generation = daily_revenue_generation
		self.daily_avergate_power = daily_avergate_power	



class MonthSummary:

	def __init__(self,quantity_plan,quantity_actual,revenue_plan,revenue_actual):
		self.month_wise_quantity_plan= quantity_plan
		self.month_wise_quantity_actual = quantity_actual
		self.month_wise_quantity_rate = 0
		self.month_wise_revenue_plan = revenue_plan
		self.month_wise_revenue_actual = revenue_actual
		self.month_wise_revenue_rate = 0
	
	def set_month_wise_quantity_rate(self):	
		if self.month_wise_quantity_plan == 0 or self.month_wise_quantity_actual == 0:
			self.month_wise_quantity_rate = 0
		
		elif isinstance(self.month_wise_quantity_plan,(int,float)) and isinstance(self.month_wise_quantity_actual,(int,float)) and isnan(self.month_wise_quantity_plan) == False and isnan(self.month_wise_quantity_actual) == False:
			self.month_wise_quantity_rate=(self.month_wise_quantity_actual*100)/self.month_wise_quantity_plan
			
		else:
			self.month_wise_quantity_rate=0


	def set_month_wise_revenue_rate(self):	
		
		if self.month_wise_revenue_plan == 0 or self.month_wise_revenue_actual == 0:
			self.month_wise_revenue_rate = 0
		
		elif isinstance(self.month_wise_revenue_plan,(int,float)) and isinstance(self.month_wise_revenue_actual,(int,float)) and isnan(self.month_wise_revenue_plan) == False and isnan(self.month_wise_revenue_actual) == False:
			self.month_wise_revenue_rate=(self.month_wise_revenue_actual*100)/self.month_wise_revenue_plan
			
		else:
			self.month_wise_revenue_rate=0


class SummaryPowerPlant:

	def __init__(self,powerplant_name,group_id,group_name=''):
		self.powerplant_name = powerplant_name
		self.daily = None
		self.month = []
		self.year = None
		self.group_id = group_id	
		self.group_name = group_name

	def set_daily_data(self,elevation,average_daily_flow,daily_power_generation,daily_revenue_generation,daily_avergate_power):
		self.daily =DailySummary(elevation,average_daily_flow,daily_power_generation,daily_revenue_generation,daily_avergate_power)			

	def add_month(self,quantity_plan,quantity_actual,revenue_plan,revenue_actual):
		month_obj=MonthSummary(quantity_plan,quantity_actual,revenue_plan,revenue_actual)
		month_obj.set_month_wise_quantity_rate()
		month_obj.set_month_wise_revenue_rate()
		self.month.append(month_obj)

	
	def set_year(self):
		quantity_plan = 0
		quantity_actual = 0
		revenue_plan = 0
		revenue_actual = 0
		
		for mon in self.month:

			if isinstance(mon.month_wise_quantity_plan,(int,float)) and isnan(mon.month_wise_quantity_plan) == False:
				quantity_plan += mon.month_wise_quantity_plan

			if isinstance(mon.month_wise_quantity_actual,(int,float)) and isnan(mon.month_wise_quantity_actual) == False:
				quantity_actual += mon.month_wise_quantity_actual
			
			if isinstance(mon.month_wise_revenue_plan,(int,float)) and isnan(mon.month_wise_revenue_plan) == False:
				revenue_plan += mon.month_wise_revenue_plan

			if isinstance(mon.month_wise_revenue_actual,(int,float)) and isnan(mon.month_wise_revenue_actual) == False:
				revenue_actual += mon.month_wise_revenue_actual
			
		self.year = MonthSummary(quantity_plan,quantity_actual,revenue_plan,revenue_actual)
		self.year.set_month_wise_quantity_rate()
		self.year.set_month_wise_revenue_rate()	


class SummaryByGroup:

	def __init__(self):
		self.plants_group = []
		self.plant_total = SummaryPowerPlant('Cộng/Total','')
		self.plant_total.month = [MonthSummary('','','','') for i in range(12)]

	def add_plant(self,plant):
		self.plants_group.append(plant)

	def set_plant_total(self):
		

		elevation = ''
		average_daily_flow = ''
		daily_power_generation = ''
		daily_revenue_generation = ''
		daily_avergate_power = ''

		if hasattr(self,'group_summary'):
			
			
			loop = [obj.plant_total for obj in self.group_summary]
			
		else:
			
			loop = self.plants_group
		
		for plant in loop:
			#elevation sum
			if (isinstance(plant.daily.elevation,(float,int)) or isinstance(plant.daily.elevation,(float,int))) and isnan(plant.daily.elevation) == False:
				if elevation == '':
					elevation = plant.daily.elevation
				else:
					elevation += plant.daily.elevation

			#average daily flow sum
			if (isinstance(plant.daily.average_daily_flow,(float,int)) or isinstance(plant.daily.average_daily_flow,(float,int)) and isnan(plant.daily.average_daily_flow) == False):
				if average_daily_flow == '':
					average_daily_flow = plant.daily.average_daily_flow
				else:
					average_daily_flow += plant.daily.average_daily_flow

			#daily power generation sum
			if isinstance(plant.daily.daily_power_generation,(float,int)) or isinstance(plant.daily.daily_power_generation,(float,int)) and isnan(plant.daily.daily_power_generation) == False:
				if daily_power_generation == '':
					daily_power_generation = plant.daily.daily_power_generation
				else:
					daily_power_generation += plant.daily.daily_power_generation

			#daily revenue sum
			if isinstance(plant.daily.daily_revenue_generation,(float,int)) or isinstance(plant.daily.daily_revenue_generation,(float,int)) and isnan(plant.daily.daily_revenue_generation) == False:
				if daily_revenue_generation == '':
					daily_revenue_generation = plant.daily.daily_revenue_generation
				else:
					daily_revenue_generation += plant.daily.daily_revenue_generation

			#avergate power sum
			if isinstance(plant.daily.daily_avergate_power,(float,int)) or isinstance(plant.daily.daily_avergate_power,(float,int)) and isnan(plant.daily.daily_avergate_power) == False:
				if daily_avergate_power == '':
					daily_avergate_power = plant.daily.daily_avergate_power
				else:
					daily_avergate_power += plant.daily.daily_avergate_power

			
			index = 0
			for mon in plant.month:
				
				if isinstance(mon.month_wise_quantity_plan,(int,float)) and isnan(mon.month_wise_quantity_plan) == False:

					if self.plant_total.month[index].month_wise_quantity_plan == '':
						self.plant_total.month[index].month_wise_quantity_plan = mon.month_wise_quantity_plan

					else:

						self.plant_total.month[index].month_wise_quantity_plan += mon.month_wise_quantity_plan

				if isinstance(mon.month_wise_quantity_actual,(int,float)) and isnan(mon.month_wise_quantity_actual) == False:

					if self.plant_total.month[index].month_wise_quantity_actual == '':
						self.plant_total.month[index].month_wise_quantity_actual = mon.month_wise_quantity_actual

					else:

						self.plant_total.month[index].month_wise_quantity_actual += mon.month_wise_quantity_actual

				if isinstance(mon.month_wise_revenue_plan,(int,float)) and isnan(mon.month_wise_revenue_plan) == False:

					if self.plant_total.month[index].month_wise_revenue_plan == '':
						self.plant_total.month[index].month_wise_revenue_plan = mon.month_wise_revenue_plan

					else:

						self.plant_total.month[index].month_wise_revenue_plan += mon.month_wise_revenue_plan

				if isinstance(mon.month_wise_revenue_actual,(int,float)) and isnan(mon.month_wise_revenue_actual) == False:

					if self.plant_total.month[index].month_wise_revenue_actual == '':
						self.plant_total.month[index].month_wise_revenue_actual = mon.month_wise_revenue_actual

					else:

						self.plant_total.month[index].month_wise_revenue_actual += mon.month_wise_revenue_actual


				self.plant_total.month[index].set_month_wise_quantity_rate()
				self.plant_total.month[index].set_month_wise_revenue_rate()
				index += 1
				
		#update daily data
		self.plant_total.set_daily_data(elevation,average_daily_flow,daily_power_generation,daily_revenue_generation,daily_avergate_power)
		#update rate
		

		#set annual data
		self.plant_total.set_year()
		


class SummaryTotalPlants(SummaryByGroup):

	def __init__(self):
		self.group_summary = []
		self.summary = SummaryByGroup()
		self.due_to_incedents = None
		self.due_to_other_jobs = None
		self.volunteer_operation = None
		self.prepared_by  = ''
		self.downstream_high_elevation = None
		self.dispatch_operation = None
		self.legal_procedure = None

		super().__init__()


	def add_group_summary(self,group):
		self.group_summary.append(group)

