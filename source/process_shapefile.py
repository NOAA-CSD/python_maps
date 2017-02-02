import shapefile
from pyproj import Proj
import numpy as np

sf = shapefile.Reader("../Utah/Utah.shp")
# Convert lat-lon to
pr = Proj('+proj=tmerc +k=0.9996 +lat_0=0 +lon_0=-111 +x_0=500000 +y_0=0 + pn=greenwich')
x,y = pr(37,-109)
print('x=%12.3f y=%12.3f (meters)' % pr(-114.057222, 51.045))
print('lat=%12.3f lon=%12.3f (degrees)' % pr(285704, 5659276, inverse=True))
shapes = sf.shapes()
print(sf.shapeRecord(1).shape.points[0:5])

print(len(sf.shapeRecord(1).shape.points))

lon_lat = np.empty([len(sf.shapeRecord(1).shape.points), 2])

for i, point in enumerate(sf.shapeRecord(1).shape.points):
    lon_lat[i] = pr(point[0], point[1], inverse=True)

np.savetxt('test_lat_lon.csv', lon_lat, delimiter=',')