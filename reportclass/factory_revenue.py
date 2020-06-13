class factory_revenue_by_month(object):
    

    def __init__(self, month):
        self.month = month
        self.mn_dk = None
        self.q_tb = None
        self.product_delivered_plan = None
        self.product_delivered_made = None
        self.product_delivered_rate=None
        self.revenue_plan = None
        self.revenue_made = None
        self.revenue_rate = None
        self.product_received = None
        self.working_time = None
    
    @property
    def get_product_delivered_rate(self):
        if self.product_delivered_plan == 'Chưa TH' or  self.product_delivered_made== 'Chưa TH':
            
            return 'Chưa TH'
        
        plan=int(self.product_delivered_plan)
        made=int(self.product_delivered_made)
        value=round(made * 100 /plan,1) 
        return value
    

    

    @property
    def get_revenue_rate(self):
        if self.revenue_plan == 'Chưa TH' or  self.revenue_made== 'Chưa TH':
            
            return 'Chưa TH'
        
        plan=int(self.revenue_plan)
        made=int(self.revenue_made)
        value=round(made * 100 /plan,1) 
        return value


class factory_revenue(object):
    """description of class"""
    def __init__(self, company_name, factory_name, factory_short_name, report_date):
        self.company_name = company_name #text field
        self.factory_name = factory_name #text field
        self.factory_short_name = factory_short_name #text field
        self.report_date = report_date #text field
        self.mn_tl= None #float
        self.q_tb = None #float
        self.product_delivered = None #float
        self.product_received = None #float
        self.revenue = None #float
        self.working_time = None #float
        self.cs_tb = None #float
        self.list_of_data_by_month = None
        self.summary_row = None

    #create sample data, report must be show value with float format number
    def create_summary(self):
        pass
    
        if self.list_of_data_by_month is None:
            self.summary_row = None
            return None

        self.summary_row = factory_revenue_by_month('NĂM 2020')
        
        for row in self.list_of_data_by_month:
            assert isinstance(row, factory_revenue_by_month)
            
            #mn_dk
            if isinstance(row.mn_dk,float) and row.mn_dk is not None and row.mn_dk!='Chưa TH':
                if self.summary_row.mn_dk is None  or self.summary_row.mn_dk =='Chưa TH':
                    self.summary_row.mn_dk = row.mn_dk
   
                else:
                    self.summary_row.mn_dk += row.mn_dk
                  
            #q_tb
            if row.q_tb is not None and row.q_tb!='Chưa TH':
                if self.summary_row.q_tb is None  or self.summary_row.q_tb =='Chưa TH':
                    self.summary_row.q_tb = row.q_tb
   
                else:
                    self.summary_row.q_tb += row.q_tb

            
            #product delievered plan
            if row.product_delivered_plan!='Chưa TH' and row.product_delivered_plan!=None :
                
                if self.summary_row.product_delivered_plan =='Chưa TH' or self.summary_row.product_delivered_plan == None:
                   
                    self.summary_row.product_delivered_plan = row.product_delivered_plan
                
                else:
                
                    self.summary_row.product_delivered_plan += row.product_delivered_plan
            
           #product delivered made  
            
            if row.product_delivered_made is not None and row.product_delivered_made!='Chưa TH':

                if self.summary_row.product_delivered_made is  None  or self.summary_row.product_delivered_made =='Chưa TH' :
                    self.summary_row.product_delivered_made = row.product_delivered_made
                else:
                    self.summary_row.product_delivered_made += row.product_delivered_made
            
            
            #revenue plan
            if row.revenue_plan is not None and row.revenue_plan!='Chưa TH':

                if self.summary_row.revenue_plan is  None or self.summary_row.revenue_plan =='Chưa TH' :
                    self.summary_row.revenue_plan = row.revenue_plan
                else:
                    self.summary_row.revenue_plan += row.revenue_plan
    
            #revenue made
            if row.revenue_made is not None and row.revenue_made!='Chưa TH':
                
                if self.summary_row.revenue_made is  None or self.summary_row.revenue_made =='Chưa TH' :
                    self.summary_row.revenue_made =  row.revenue_made
                else:
                    self.summary_row.revenue_made +=  row.revenue_made

            #product_received
            if row.product_received is not None and row.product_received!='Chưa TH':
                
                if self.summary_row.product_received is  None or self.summary_row.product_received =='Chưa TH' :
                    self.summary_row.product_received = row.product_received
                else:
        
                    self.summary_row.product_received += row.product_received


            #working_time
            if row.working_time is not None and row.working_time!='Chưa TH':
                
                if self.summary_row.working_time is  None or self.summary_row.working_time =='Chưa TH' :
                    self.summary_row.working_time = row.working_time
                else:
                    
                    self.summary_row.working_time += row.working_time
        
        #set rate values
        self.summary_row.product_delivered_rate=self.summary_row.product_delivered_plan/self.summary_row.product_delivered_made
        self.summary_row.revenue_rate=self.summary_row.revenue_plan/self.summary_row.revenue_made        

        


    def generate_sample_data(self):
        self.mn_tl =0
        #set other property like above

        #popupate the list_of_data_by_month
        self.list_of_data_by_month = []
        row = factory_revenue_by_month("Thang 1")
        row.mn_dk = 227.0
        #set all other property
        self.list_of_data_by_month.append(row)
