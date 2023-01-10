emp=[ {"CusID":1, "Cusname":"A", "Cusscore":100, "":[1,2,3,4]}
     ,{"CusID":2, "Cusname":"B", "Cusscore":200, "projects":[1,3,5,6]}
	 ,{"CusID":3, "Cusname":"C", "Cusscorew":200, "projects":[3,7,8,9]}]
	 
for e in emp:
    print(e)
    print(e["projects"])
    for p in (e["projects"]):
        if p==1:
            print(e["Empname"])
































