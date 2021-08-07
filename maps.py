import gmplot
import csv 

random = False

#changing color of lines:  
with open("config.txt", newline='') as data: 
    config = [] 
    for x in data:
        config.append(int(x))
    #print(config)
data.close 

if config[0]==0:
    config_Color = 0 
else: 
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
with open("map_coordinates.txt", newline='') as csvfile:
    ll=[]
    map_coordinates = csv.reader(csvfile, delimiter='\n')
    for plots in map_coordinates:
        ll.append(plots) 
csvfile.close
for x in range(len(ll)):

    split=''.join(ll[x]).split(' ') #breakout items from each matched row. Seperate with commas. 

    a,o = zip(*[ ( int(float(split[0])),int(float(split[1])) ) , ( int(float(split[4])),int(float(split[5])) ) ])
   #DELETE ME? )))
    lati1="latitude: "+split[0]+"\nlongitude: "+split[1]+";"
    lati2="latitude: "+split[4]+"\nlongitude: "+split[5]+";"
    # Scatter map
    gmap3.scatter( a, o, '#FF0000',size = 50)
    
    b1="Latitude: "+str(split[0])+" Longitude: "+str(split[0])
    b2="Latitude: "+str(split[4])+" Longitude: "+str(split[5])
    gmap3.marker( int(float(split[0])), int(float(split[1])), title=b1 ) 
    gmap3.marker( int(float(split[4])), int(float(split[5])), title=b2 )
    # Plot method Draw a line in between given coordinates
    gmap3.plot(a, o, getcolor(colormarker), edge_width = 2.0)
    if colormarker==9:
        colormarker=0 
    colormarker+=1 





#Your Google_API_Key
#gmap3.apikey = " AIzaSyD5sAw22lbdNECc4Bi8DFn7jVc_66SbWrY " 
# save it to html
gmap3.draw("Map.html")