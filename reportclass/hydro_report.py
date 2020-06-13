class HydroDayReport:

	def __init__(self,target):
		
		self.target = target
		self.upstream = None
		self.downstream = None
		self.back_to_lake = None
		self.rinse_unit = None
		self.discharge_overflow = None
		self.minimum_discharge = None
		self.whi = None	


class  HydroReportData:

	def __init__(self,company_name,factory_name,mn_dbt,mnc,q0,qmax,wtb,whi,wc):
		self.company_name = company_name #text field
		self.factory_name = factory_name 
		self.mn_dbt = mn_dbt
		self.mnc = mnc
		self.q0 = q0
		self.qmax = qmax
		self.wtb = wtb
		self.whi = whi
		self.wc = wc
		