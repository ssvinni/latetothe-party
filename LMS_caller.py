
#Loan Management Syatem - Caller

#imports

import LMS_engine as lms
import LMS_masterdata

#customer details

cust_name = "abc"
cust_cs = 190
cust_loan_amt = 12345

# call the engine

result = lms.LMS_engine( p_loans_master_data = LMS_masterdata.loan_rules_masteer_data
                        ,p_cust_name = cust_name
                        ,p_cust_cs = cust_cs
                        ,p_cust_req_loan_amt = cust_loan_amt)

print(result)
