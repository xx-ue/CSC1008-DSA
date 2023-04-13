from flask import Flask, render_template, request, url_for, flash, redirect
from csv import reader
import folium
from folium.features import DivIcon


app = Flask(__name__)
@app.route('/')
def home():
  return render_template('MainPageSelections.html')
@app.route('/redirect')
def options():
    Route = request.args.get("Route")

    if Route == "1":
        return redirect("/Dijkstra")
    elif Route == "2":
        return redirect("/AStar")
    elif Route == "3":
        return redirect("/Matching")
    elif Route =='5':
        return redirect("/Ridesharing2")
    else:
        return redirect("/Ridesharing")

@app.route('/Dijkstra')
def Dijkstra():
    f = folium.Map(location=[1.3507, 103.8488],
                   zoom_start=14.8
                   )
    distance=0
    coords = []
    coords2=[]
    with open('Dijkstra.csv') as csv_file:
        csv_reader = reader(csv_file)
        header = next(csv_reader)
    # Iterate over each row in the csv using reader object
        for row in csv_reader:# row variable is a list that represents a row in csv
            if row[0] != '':#contains the distance
                distance+=float(row[0])
            if row[1] != '' and row[2] != '':#contains the lat and long for the path from driver to user
                coords.append([float(row[1]), float(row[2])])
            if row[3] != '' and row[4] != '':#contains the lat and long for the path from user to dest
                coords2.append([float(row[3]), float(row[4])])
    folium.PolyLine(coords, color='red', weight=5,opacity=0.4).add_to(f)
    folium.PolyLine(coords2, color='purple', weight=5,opacity=0.5).add_to(f)
    folium.Marker([coords[0][0], coords[0][1]], popup = ('Driver assigned: Peter'), icon = folium.Icon(color='navy', icon='car', prefix='fa')).add_to(f)
    folium.Marker([coords2[0][0], coords2[0][1]], popup = ('User'), icon = folium.Icon(color='black', icon='home', prefix='fa')).add_to(f)
    folium.Marker([coords2[-1][0], coords2[-1][1]], popup = ('Destination\n\nTotal distance: '+str(distance)+'km'+"\nCost:$11.04"), icon = folium.Icon(color='red', icon='info-sign')).add_to(f)
    folium.TileLayer('cartodbpositron').add_to(f)
    f.save('templates/Dijkstra_map.html')
    return render_template('indexForDijkstra.html')
@app.route('/Dijkstra_map')
def Dijkstra_map():
    return render_template('Dijkstra_map.html')

@app.route('/AStar')
def AStar():
    f = folium.Map(location=[1.3496033678588581, 103.84455425144989],
                   zoom_start=14.8
                   )
    distance = 0
    coords = []
    coords2 = []
    with open('Astar.csv') as csv_file:
        csv_reader = reader(csv_file)
        header = next(csv_reader)
        # Iterate over each row in the csv using reader object
        for row in csv_reader:# row variable is a list that represents a row in csv
            if row[0] != '':#contains the distance
                distance += float(row[0])
            if row[1] != '' and row[2] != '':#contains the lat and long for the path from driver to user
                coords.append([float(row[1]), float(row[2])])
            if row[3] != '' and row[4] != '':#contains the lat and long for the path from user to dest
                coords2.append([float(row[3]), float(row[4])])
    folium.PolyLine(coords, color='#905284', weight=5).add_to(f)
    folium.PolyLine(coords2, color='#E3242B', weight=5).add_to(f)
    folium.Marker([coords[0][0], coords[0][1]], popup=('Driver: Ryan'),
                  icon=folium.Icon(color='cadetblue', icon='car', prefix='fa')).add_to(f)
    folium.Marker([coords2[0][0], coords2[0][1]], popup=('User'),
                  icon=folium.Icon(color='black', icon='home', prefix='fa')).add_to(f)
    folium.Marker([coords2[-1][0], coords2[-1][1]], popup=('Destination\n\nTotal distance: ' + str(distance) + 'km'+"\nCost:$8.43"),
                  icon=folium.Icon(color='red', icon='info-sign')).add_to(f)
    folium.TileLayer('cartodbpositron').add_to(f)
    f.save('templates/AStar_map.html')
    return render_template('indexForAStar.html')
@app.route('/AStar_map')
def AStar_map():
    return render_template('AStar_map.html')

@app.route('/Matching')
def Matching():
    f = folium.Map(location=[1.3496033678588581, 103.84455425144989],
                   zoom_start=14.4
                   )
    distance =[]
    coords1 = []
    coords2 = []
    coords3 = []
    with open('Matching.csv') as csv_file:
        csv_reader = reader(csv_file)
        header = next(csv_reader)
        # Iterate over each row in the csv using reader object
        for row in csv_reader:# row variable is a list that represents a row in csv
            if row[0] != '':#contains the distances of each path
                distance.append(float(row[0]))
            if row[1] != '' and row[2]!= '':#contains the lat and long for the first path
                coords1.append([float(row[1]), float(row[2])])
            if row[3] != '' and row[4] != '':#contains the lat and long for the second path
                coords2.append([float(row[3]), float(row[4])])
            if row[5] != '' and row[6] != '':#contains the lat and long for the third path
                coords3.append([float(row[5]), float(row[6])])
    folium.PolyLine(coords1, color='#FF1493', weight=5).add_to(f)
    folium.PolyLine(coords2, color='blue', weight=5, opacity=0.4).add_to(f)
    folium.PolyLine(coords3, color='orange', weight=5).add_to(f)
    folium.Marker([coords1[0][0], coords1[0][1]], popup = ('Driver'), icon = folium.Icon(color='navy', icon='car', prefix='fa')).add_to(f)
    folium.Marker([coords1[-1][0], coords1[-1][1]], popup=('User'+'Total Distance: '+str(round(distance[0],2))+"km"),icon=folium.Icon(color='black', icon='home', prefix='fa')).add_to(f)
    folium.Marker([coords2[0][0], coords2[0][1]], popup = ('Driver'), icon = folium.Icon(color='navy', icon='car', prefix='fa')).add_to(f)
    folium.Marker([coords2[-1][0], coords2[-1][1]], popup=('User'+'Total Distance: '+str(round(distance[2],2))+"km"),icon=folium.Icon(color='black', icon='home', prefix='fa')).add_to(f)
    folium.Marker([coords3[0][0], coords3[0][1]], popup = ('Driver'), icon = folium.Icon(color='navy', icon='car', prefix='fa')).add_to(f)
    folium.Marker([coords3[-1][0], coords3[-1][1]], popup=('User'+'Total Distance: '+str(round(distance[1],2))+"km"),icon=folium.Icon(color='black', icon='home', prefix='fa')).add_to(f)
    folium.TileLayer('cartodbpositron').add_to(f)
    f.save('templates/Matching_map.html')
    return render_template('indexForMatching.html')
@app.route('/Matching_map')
def Matching_map():
    return render_template('Matching_map.html')

@app.route('/Ridesharing')
def Ridesharing():
    f = folium.Map(location=[1.3496033678588581, 103.84455425144989],
                   zoom_start=14
                   )
    coords1 = []
    coords2 = []
    coords3 = []
    coords4 = []

    with open('Ridesharing.csv') as csv_file:
        csv_reader = reader(csv_file)
        header = next(csv_reader)

    # Iterate over each row in the csv using reader object
        for row in csv_reader:# row variable is a list that represents a row in csv
            if row[1] != '' and row[2] != '': #contains the lat and long for the path from driver to main user
                coords1.append([float(row[1]), float(row[2])])
            if row[3] != '' and row[4] != '':#contains the lat and long for the path from main user to rideshare user
                coords2.append([float(row[3]), float(row[4])])
            if row[5] != '' and row[6] != '':#contains the lat and long for the path from rideshare user to first destination
                coords3.append([float(row[5]), float(row[6])])
            if row[7] != '' and row[8] != '':#contains the lat and long for the path from first destination to second destination
                coords4.append([float(row[7]), float(row[8])])

    folium.PolyLine(coords1, color='#FF1493',dash_array='10', weight=10).add_to(f)#plot from driver to main user
    folium.PolyLine(coords2, color='#20B2AA', opacity=0.8,weight=5).add_to(f) #plot from main user to rideshare user
    folium.PolyLine(coords3, color='yellow', weight=5).add_to(f) #plot rideshare user to first destination
    folium.PolyLine(coords4, color='blue',opacity=0.1, weight=10).add_to(f)#plot first destination to second destination
    folium.Marker([coords1[0][0], coords1[0][1]], popup=('Driver: Ben'),
                  icon=folium.Icon(color='navy', icon='car', prefix='fa')).add_to(f)
    folium.Marker([coords2[0][0], coords2[0][1]], popup=('Main User'),
                  icon=folium.Icon(color='black', icon='home', prefix='fa')).add_to(f)
    folium.Marker([coords3[0][0], coords3[0][1]], popup=('Rideshare user'),
                  icon=folium.Icon(color='black', icon='home', prefix='fa')).add_to(f)
    folium.Marker([coords3[-1][0], coords3[-1][1]], icon=DivIcon( #first destination
        icon_size=(150, 36),
        icon_anchor=(7, 20),
        html='<div style="font-size: 18pt; color : black">1</div>',
    )).add_to(f)
    f.add_child(folium.CircleMarker([coords3[-1][0], coords3[-1][1]], radius=10))
    folium.Marker([coords4[-1][0], coords4[-1][1]], icon=DivIcon( #second destination
        icon_size=(150, 36),
        icon_anchor=(7, 20),
        html='<div style="font-size: 18pt; color : black">2</div>',
    )).add_to(f)
    f.add_child(folium.CircleMarker([coords4[-1][0], coords4[-1][1]], radius=10))
    folium.TileLayer('cartodbpositron').add_to(f)
    f.save('templates/Ridesharing_map.html')
    return render_template('indexForRidesharing.html')
@app.route('/Ridesharing_map')
def Ridesharing_map():
    return render_template('Ridesharing_map.html')
@app.route('/Ridesharing2')
def Ridesharing2():
    f = folium.Map(location=[1.3496033678588581, 103.84455425144989],
                   zoom_start=14
                   )
    distance = 0
    coords1 = []
    coords2 = []
    coords3 = []
    with open('Ridesharing2.csv') as csv_file:
        csv_reader = reader(csv_file)
        header = next(csv_reader)

    # Iterate over each row in the csv using reader object
        for row in csv_reader:# row variable is a list that represents a row in csv
            if row[1] != '' and row[2] != '': #contains the lat and long for the path from driver to main user
                coords1.append([float(row[1]), float(row[2])])
            if row[3] != '' and row[4] != '':#contains the lat and long for the path from main user to destination
                coords2.append([float(row[3]), float(row[4])])
            if row[5] != '' and row[6] != '':#contains the lat and long for users that were not picked up
                coords3.append([float(row[5]), float(row[6])])

    folium.PolyLine(coords1, color='#FF1493',dash_array='10', weight=10).add_to(f)#plot driver to user
    folium.PolyLine(coords2, color='#20B2AA', opacity=0.8,weight=5).add_to(f) #plot user to destination

    folium.Marker([coords1[0][0], coords1[0][1]], popup=('Driver: Ben'),
                  icon=folium.Icon(color='navy', icon='car', prefix='fa')).add_to(f)
    folium.Marker([coords2[0][0], coords2[0][1]], popup=('Main User'),
                  icon=folium.Icon(color='black', icon='home', prefix='fa')).add_to(f)
    folium.Marker([coords2[-1][0], coords2[-1][1]], popup=('Destination'),
                  icon=folium.Icon(color='cadetblue', icon='info-sign')).add_to(f)
    ##Users that were not picked up##
    folium.Marker([1.339083,103.852493], popup=('User'),
                      icon=folium.Icon(color='black', icon='home', prefix='fa')).add_to(f)
    folium.Marker([1.343148,103.853641], popup=('User'),
                  icon=folium.Icon(color='black', icon='home', prefix='fa')).add_to(f)
    folium.Marker([1.352936049,103.8520056], popup=('User'),
                  icon=folium.Icon(color='black', icon='home', prefix='fa')).add_to(f)

    folium.TileLayer('cartodbpositron').add_to(f)
    f.save('templates/Ridesharing2_map.html')
    return render_template('indexForRidesharing2.html')
@app.route('/Ridesharing2_map')
def Ridesharing2_map():
    return render_template('Ridesharing2_map.html')

if __name__ == '__main__':
    app.run(debug=True)