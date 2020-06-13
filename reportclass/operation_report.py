class OperationRevenue:

	def __init__(self,date_time):
		self.date_time = date_time
		self.output_delivered = None
		self.output_received = None
		self.running_time = None
		self.price_boundary = None
		self.can_price = None
		self.expected_revenue = None
		self.operation_problem = None
		self.unusual_event = ''
		self.head_shift = ''


class OperationRevenueData:
	
	def __init__(self,number_of_sets,plm,pmin,e,contract_price):
		self.number_of_sets=number_of_sets
		self.plm=plm
		self.pmin=pmin
		self.e=e
		self.contract_price = contract_price


