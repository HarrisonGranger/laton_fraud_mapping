# import gmplot package
import gmplot
#Set different latitude and longitude points
Charminar_top_attraction_lats, Charminar_top_attraction_lons = zip(*[
    ( 42.7371615, -84.3432647), (37.3504139, -79.1794932)])
#declare the center of the map, and how much we want the map zoomed in
gmap3 = gmplot.GoogleMapPlotter(42.3616, -80.4747, 7)
# Scatter map
gmap3.scatter( Charminar_top_attraction_lats, Charminar_top_attraction_lons, '#FF0000',size = 50, marker = False )
# Plot method Draw a line in between given coordinates
gmap3.plot(Charminar_top_attraction_lats, Charminar_top_attraction_lons, 'cornflowerblue', edge_width = 3.0)
#Your Google_API_Key
gmap3.apikey = " AIzaSyD5sAw22lbdNECc4Bi8DFn7jVc_66SbWrY " 
# save it to html
gmap3.draw("Map.html")