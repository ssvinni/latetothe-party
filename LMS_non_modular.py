#loan management system
 #customer details
#cust_name = "abc"
#cust_cs = 190
#cust_loan_amt = 12345
#qualified = 0

#set 2 for a failure case
#cust_name = "cba"
#cust_cs = 90
#cust_loan_amt = 14345

cust_data = [
{"cust_name":"abc", "cust_cs":190, "cust_loan_amt":12345}
,{"cust_name":"cba","cust_cs":90, "cust_loan_amt":14345 }
]

for c in cust_data:
    print(c)
    qualified = 0
    master_data = [
    {"cs_start":100, "cs_end":199, "loan_amt_start":10000, "loan_amt_end":19999,"interest":4.5, "duration_in_mons":72}
    ,{"cs_start":200, "cs_end":299, "loan_amt_start":10000, "loan_amt_end":19999,"interest":4, "duration_in_mons":72}
    ,{"cs_start":300, "cs_end":399, "loan_amt_start":10000, "loan_amt_end":19999,"interest":3.5, "duration_in_mons":72}
    ,{"cs_start":400, "cs_end":499, "loan_amt_start":10000, "loan_amt_end":19999,"interest":3, "duration_in_mons":72}
    ]
    #application_decision = {}
    for c1 in master_data:
        print(c1)
        if c["cust_cs"] >= c1["cs_start"] and c["cust_cs"] <= c1["cs_end"] and c["cust_loan_amt"] >= c1["loan_amt_start"] and c["cust_loan_amt"] <= c1["loan_amt_end"]:
            qualified = 1
            print(c1["interest"])
            print(c1["duration_in_mons"])
            #application_decision["cust_name"] = cust_name
            #application_decision["cust_cs"] = cust_cs
            #print(application_decision)
    print ('qualified is: ')
    print (qualified)
    #print (qualified = qualified)"""
    print ("applicant name is " + c["cust_name"])
    if qualified == 0:
        print("not qualified")
    else:
        print("qualified")