import pymysql
import csv

def mysqlconnect():
    # Connect to database
    try:
        cur.execute("CREATE DATABASE msBE")
        print("Database created. Creating new table 'coor'")
    except:
        print("Database exists. Attempting to connect using table 'coor'.")
    #prepare database/data for insertion
    cur.execute("USE msBE") #establish database, print results for validity 
    cur.execute("CREATE TABLE IF NOT EXISTS coor(timestamp_A VARCHAR(15) NULL,timestamp_B VARCHAR(15) NULL,MAC_A VARCHAR(50) NOT NULL,MAC_B VARCHAR(50) NOT NULL,coordinates_A VARCHAR(50) NOT NULL,coordinates_B VARCHAR(50) NOT NULL)")
    print("Finding table 'coor'...")
   
#insertions into table
def upload(timeA,timeB,macA,macB,coorA,coorB):
    cur.execute("INSERT INTO coor VALUES ("+"\'"+timeA+"\'"+","+"\'"+timeB+"\'"+","+"\'"+macA+"\'"+","+"\'"+macB+"\'"+","+"\'"+coorA+"\'"+","+"\'"+coorB+"\'"+")")


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
    with open("map_coordinates.txt", newline='') as csvfile:
        ll = []
        read = csv.reader(csvfile, delimiter=' ')
        for x in read:
            ll.append(x)
    #insert data
        i=0
        while i<len(ll):
            timestampA = ll[i][2]
            timestampB = ll[i][6]
            macA = ll[i][3]
            macB = ll[i][7]
            coorA = ll[i][0]+", "+ll[i][1]
            coorB = ll[i][4]+", "+ll[i][5]

            upload(timestampA,timestampB,macA,macB,coorA,coorB)
            
                
            i+=1
    
    conn.commit() 
    conn.close()
    print("Values successfully uploaded!")


    
 