import csv

#class for fun colors 
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

with open("thiccboi.txt", newline='') as csvfile: 
    ll = []  
    thiccboi = csv.reader(csvfile, delimiter=' ')
    for mac in thiccboi:
        ll.append(mac)
    #now we have ll[0][0] as a list. [0-x][3] will be all mac addresses. ll[x] will provide full value. 
    i=0
    j=0
    while i<len(ll):
        j=i+1 
        while j<len(ll):
            if((ll[i][3]) == (ll[j][3])) and (((ll[i][0] != ll[j][0]) or (ll[i][1] != ll[i][1]))): 
                write = open('temp.txt', 'a')
                write.write(ll[i][0]+", "+ll[i][1]+":"+ll[j][0]+", "+ll[j][1]+"\n") 
                print(bcolors.FAIL + "Match found for --"+ll[i][3]+"--" + bcolors.ENDC) 
                #write.write("("+ll[i][0]+", "+ll[i][1]+", "+ll[i][2]+", "+ll[i][3]+")"+","+"("+ll[j][0]+", "+ll[j][1]+", "+ll[j][2]+", "+ll[j][3]+")\n")
                write.close()
                write = open('maps_output.txt', 'a')  
                write.write("("+ll[i][0]+", "+ll[i][1]+", "+ll[i][2]+", "+ll[i][3]+")"+","+"("+ll[j][0]+", "+ll[j][1]+", "+ll[j][2]+", "+ll[j][3]+")\n")
                write.close() 
            else: print(bcolors.OKGREEN + "No match for --"+ll[i][3]+"--" + bcolors.ENDC)
            j+=1 
        i+=1 