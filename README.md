# mapbox
A web-based application that implements:
* A login page (Bootstrap themed)
* A map
* Polygon tools
* Measure an area on a map and return the size in square meter

Built with Python, Flask, Bootstrap, ReactJS, Mapbox, Turf.

## Installation
Install Python 3.7.4 and pip. Install flask using pip.
```bash
pip install flask
```

## Usage
```bash
python flaskapp.py
```
Open [localhost:5000/login](localhost:5000/login) in a browser.

Login with  
Username: admin  
Password: password  

Click the square button on the top-right corner of the map to draw polygon  
Calculated area size is shown on bottom-left corner  
Click trashcan button on the top-right corner of the map to delete polygon  

Reference:\n
Flask tutorial: [https://youtu.be/MwZwr5Tvyxo](https://youtu.be/MwZwr5Tvyxo)  
Mapbox + Turf: [https://docs.mapbox.com/mapbox-gl-js/example/mapbox-gl-draw/](https://docs.mapbox.com/mapbox-gl-js/example/mapbox-gl-draw/)  
