
# LMS engine

def LMS_engine(p_loans_master_data, p_cust_name, p_cust_cs, p_cust_req_loan_amt):
    # variables

    application_decision = {}

    # core Algorithm

    for c1 in p_loans_master_data:
       # print(c1)
        if p_cust_cs >= c1["cs_start"] and p_cust_cs<= c1["cs_end"] and p_cust_req_loan_amt >= c1["loan_amt_start"] and p_cust_req_loan_amt<= c1["loan_amt_end"]:
            application_decision["interest"] = c1["interest"]
            application_decision["duration_in_mons"] = c1["duration_in_mons"]
            application_decision["p_cust_name"] = p_cust_name

    return application_decision