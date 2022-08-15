
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
  
roznica = mins+dura 
mins = roznica % 60
hour += roznica // 60
hour %=24

print("End time: ",hour,":",mins,sep="")
