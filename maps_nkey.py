import gmplot
import csv 

random = False

#first deal wth config file stuff 
with open("config.txt", newline='') as data: 
    config = [] 
    for x in data:
        config.append(int(x))
    #print(config)
data.close 

if config[0]==0:
    print("NO")
    config_Color = 0 
else: 
    print("YES")
    if config[0]==-1:
        random=True
    else:
        if(config[0]>9 or config[0]<-1):
            print("Invalid color selected! Default will be used.")
            config_Color = 0
        else: 
            config_Color = config[0]


def getcolor(colormarker): 
    if random == True:
        return color[colormarker]
    else:
        return color[config_Color] 

gmap3 = gmplot.GoogleMapPlotter(37.3504139, -79.1794932, 2) 
color = ['red','green','cornflowerblue','yellow','purple','black','orange','grey','pink','white']
colormarker = 0 #variable to choose colors  
with open("temp.txt", newline='') as csvfile:
    ll=[]
    temp = csv.reader(csvfile, delimiter='\n')
    for plots in temp:
        ll.append(plots) 
csvfile.close
for x in range(len(ll)):
    split=''.join(ll[x]).split(":")
    lt1 =  split[0].split(",") 
    lt2 =  split[1].split(",") 
    a,o = zip(*[ ( int(float(lt1[0])),int(float(lt1[1])) ) , ( int(float(lt2[0])),int(float(lt2[1])) ) ])
    lati1="latitude: "+lt1[0]+"\nlongitude: "+lt1[1]+";"
    lati2="latitude: "+lt2[0]+"\nlongitude: "+lt2[1]+";"
    # Scatter map
    gmap3.scatter( a, o, '#FF0000',size = 50)
    
    b1="lat: "+str(lt1[0])+" lon: "+str(lt1[0])
    b2="lat: "+str(lt2[0])+" lon: "+str(lt2[0])
    gmap3.marker( int(float(lt1[0])), int(float(lt1[1])), title=b1 ) 
    gmap3.marker( int(float(lt2[0])), int(float(lt2[1])), title=b2 )
    # Plot method Draw a line in between given coordinates
    gmap3.plot(a, o, getcolor(colormarker), edge_width = 2.0)
    if colormarker==9:
        colormarker=0 
    colormarker+=1 





#Your Google_API_Key
#gmap3.apikey = "API_KEY HERE " 
# save it to html
gmap3.draw("Map.html")
