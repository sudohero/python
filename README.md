# python

Just some random code to practice python

File Descriptions:
------------------

+ GoogleDirectionsAPI.py - Uses directions API from Google Maps to get a start point and end point from a user, then display the route data back to the user with total distance and duration of the route and distance and duration of each step in the route.

+ reverse.py - Creates a "shell" for the user to enter 6 commands; 3 normal and 3 reverse. This was just to practice creating lists from strings, using for loops, and manipulating lists and data.

+ ip_geolocator.py - Queries the ip-api.com api for geolocation data of a given IP address or a file containing a list of IP addresses. This is a public api that does not require an api key. More info at https://ip-api.com/docs/api:json#test

### ip_geolocator usage

To query for a single IP
```
$ python3 ip_geolocator.py -i x.x.x.x
```

To query a list of IP's (one IP per line)
```
$ python3 ip_geolocator.py -f <filename>
```

The IP list file would look like:
```
x.x.x.x
y.y.y.y
z.z.z.z
```

### Screenshots

Single IP address query

![single-ip](https://user-images.githubusercontent.com/45858613/112901016-36a08500-90b2-11eb-83c4-e7babbab772a.PNG)


Multiple IP addresses from a list

![ip-list](https://user-images.githubusercontent.com/45858613/112901108-559f1700-90b2-11eb-8ed0-33331089bd96.PNG)
