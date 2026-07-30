import csv
from gmplot import gmplot

gmap = gmplot.GoogleMapPlotter(23.256749, 72.892409,25)                             
gmap.coloricon = "http://www.googlemapsmarkers.com/v1/%s/"                                  

with open('routes.csv', 'r') as f:
    reader = csv.reader(f)
    
    k=0 
    
    for row in reader:
        if not row:   # <-- skip empty lines
            continue
        lat = float(row[0])
        lon = float(row[1])
        if k==0:
            gmap.marker(lat, lon, 'yellow')
            k=1
        else:
            gmap.marker(lat, lon, 'blue')

gmap.marker(lat, lon, 'red')
gmap.draw("jaimin_map.html")
