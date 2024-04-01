print("FIRST COME FIRST SERVE SCHEDULLING")
n= int(input("Enter number of processes : "))
d = dict()
 
for i in range(n):
    key = "P"+str(i+1)
    a = int(input("Enter arrival time of process"+str(i+1)+": "))
    b = int(input("Enter burst time of process"+str(i+1)+": "))
    l = []
    l.append(a)
    l.append(b)
    d[key] = l
 
d = sorted(d.items(), key=lambda item: item[1][0])
 
# Exist time / completion time
ET = []
for i in range(len(d)):
    if(i==0):
        ET.append(d[i][1][1])
    else:
        ET.append(ET[i-1] + d[i][1][1])

# Turn around time
TAT = []
for i in range(len(d)):
    TAT.append(ET[i] - d[i][1][0])
 
# Waiting time
WT = []
for i in range(len(d)):
    WT.append(TAT[i] - d[i][1][1])
 
# Average waiting time
avg_WT = 0
for i in WT:
    avg_WT +=i
avg_WT = (avg_WT/n)

print("Process | Arrival | Burst | Turn Around Time | Waiting Time |")
for i in range(n):
    print(f"   {d[i][0]:<7} {d[i][1][0]:<9} {d[i][1][1]:<6} {TAT[i]:<16} {WT[i]:<12}")
print("")
print(f"Average Waiting Time: {avg_WT}")

 
# print("Process | Arrival | Burst | Turn Around Time |   Waiting Time   |")
# for i in range(n):
#       print("   ",d[i][0],"      ",d[i][1][0],"   ",d[i][1][1],"   ",TAT[i],"      ",WT[i],"   ")
# print("Average Waiting Time: ",avg_WT)