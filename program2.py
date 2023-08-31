rank = []
girlnames = []
boynames = []
employees = {"beck":"teacher","tommy":"idiot","jeff":"person","joe":"web-admin"}


for key,value in employees.items():
    print("-------------")
    print("Name: " + key)
    print("Job: " + value)

with open("/home/student/program2/girl_boy_names_2004.csv","r") as names_csv:
    lines = names_csv.readlines()

    for i in lines:
        new_list = i.split(",")
        rank.append(new_list[0])
        girlnames.append(new_list[1])
        boynames.append(new_list[2])
    
    for i in range(len(girlnames)):
        print ("-------------")
        print ("Rank: " + rank[i])
        print ("Girl name: " + girlnames[i])
        print ("Boy name: " + boynames[i])