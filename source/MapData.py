import numpy as np
import shapefile as sf
import pyproj as proj
import os
import re

class MapData:

    def __init__(self):

        self.projection = self.ProjectionFormat()

    class ProjectionFormat:

        def __init__(self):

            # Scaling factor
            self.k = 1

            # Latitude of origin
            self.lat_0 = 0

            # Central Meridian
            self.lon_0 = 0

            # Prime meridian
            self.pm = 'Greenwich'

            self.units = 'Meter'

            # False easting
            self.x_0 = 500000

            # False northing
            self.y_0 = 0

            self.proj = 'utm'

        def read_prj_file(self, dir, name):

            """Reads in the projection format file from the shapefile dataset.

            Args:
                loc: main directory for location of all shapefile information

            Returns:


            :param loc:
            :return:
            """

            projections = {'Transverse_Mercator': 'utm',
                           'Extended_Transverse_Mercator': 'etmerc',
                           'Mercator': 'merc'
                           }

            re_proj = re.compile(r'PROJECTION\["(.*)"\]')
            re_param = re.compile(r'PARAMETER\["(.*),(.*)"\]')
            with open(os.path.join(dir, name + "." + "prj"), 'r') as f:
                text = f.read()

            for key in re_param.findall(text):
                n = float(key[1])
                v = key[0]
                if v == 'False_Easting':
                    self.x_0 = n
                elif v == 'False_Northing':
                    self.y_0 = n
                elif v == 'Central_Meridian':
                    self.lon_0 = n
                elif v == 'Scale_Factor':
                    self.k = n
                elif v == 'Latitude_Of_Origin':
                    self.lat_0 = n
                else:
                    print('Key undefined in read_prj_file')

            self.proj = projections[re_proj.search(text).groups()[0]]

            return self
