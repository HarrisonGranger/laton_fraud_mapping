import pymysql
import csv

def mysqlconnect():
    # Connect to database
    try:
        cur.execute("CREATE DATABASE msBE")
        print("No data entered. Creating new table 'coor'")
        print("Please upload data. Yum Yum.")
        quit()
    except:
        print("Database exists. Attempting to connect using table 'coor'.")
    #prepare database/data for insertion
    try:
        cur.execute("USE msBE") #establish database, print results for validity 
        print("Finding table 'coor'...")
    except:
        print("No table found.")
        quit()

def getAll():
    cur.execute("SELECT * FROM coor")

def getTime(timea,timeb):
    cur.execute("SELECT *  FROM coor WHERE timestamp_A AND timestamp_B BETWEEN "+str(timea)+" AND "+str(timeb)+"")


def getMac(mac):
    cur.execute("SELECT * FROM coor WHERE MAC_A OR MAC_B = \'"+str(mac)+"\'")

def getCoordinates(coordinates): 
    cur.execute("SELECT * FROM coor WHERE COORDINATES_A = "+str(coordinates)+" OR COORDiNATES_B = "+str(coordinates)+"")
 

def delete():
    cur.execute("DROP table coor")

if __name__ == "__main__" :
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password="pass",
        )
    cur = conn.cursor() 
    #connect to sql database
    mysqlconnect()
    #read file with coordinates
    with open("order.txt", newline='') as csvfile:
        ll = []
        read = csv.reader(csvfile, delimiter='/')
        for x in read:
            ll.append(x)
    #request data
        if " ".join(ll[0])=='A':
            print("Fetching coornidate specifications...\n")
            getAll()
        elif " ".join(ll[0])=='T':
            a=ll[1][0]
            print("Fetching timestamp specifications...\n")
            #print(a)
            b=ll[2][0]
            #print(b)
            getTime(a,b)
        elif " ".join(ll[0])=='M':
            print("Fetching mac address specifications...\n")
            a=ll[1][0]
            getMac(a)
        elif " ".join(ll[0])=='D':
            answer=input("Would you like to commit changes (y/n) ? : ")
            if answer == 'y':
                delete()
            elif answer == 'n':
                print("Whew! Close one!")
            else: 
                print(str(answer)+" not a valid option.")
        elif " ".join(ll[0])=='C':
            print("Fetching coornidate specifications...\n")
            a=ll[1][0]
            getCoordinates(a)

        a=0
        for x in cur:
            print(x)
            a=a+1
    
        print("\n"+str(a)+" results found")
        quit()        
        

    conn.close()


    

