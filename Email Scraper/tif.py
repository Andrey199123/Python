from osgeo import gdal
import numpy as np
import os
from collections import OrderedDict
import glob2
from osgeo import osr

script_dir = os.path.dirname(os.path.realpath(__file__))
RESOLUTION = 10
NULL_VALUE = -9999.0


def process(input_file):
    total_lines = 1
    total_columns = 1

    dict_x = OrderedDict()
    dict_y = OrderedDict()

    i = 0

    min_x = 99999999999999
    max_x = -99999999999999
    min_y = 99999999999999
    max_y = -99999999999999

    # First find the number of grid pixels
    with open(input_file) as file:
        for l in file:
            line = l.replace('    ', ' ').replace('  ', ' ').rstrip("\r\n").strip()

            tmps = line.split(" ")
            x = tmps[0]
            y = tmps[1]
            z = float(tmps[2])

            if not dict_x:
                dict_x[x] = 0
            if not dict_y:
                dict_y[y] = 0

            if x not in dict_x:
                total_lines += 1
                dict_x[x] = 0
            if y not in dict_y:
                total_columns += 1
                dict_y[y] = 0

            if min_x > float(x):
                min_x = float(x)
            if max_x < float(x):
                max_x = float(x)

            if min_y > float(y):
                min_y = float(y)
            if max_y < float(y):
                max_y = float(y)

            # print(i)
            i += 1

    matrix = np.tile(NULL_VALUE, (total_columns, total_lines))

    # print(min_x, min_y, max_x, max_y)

    with open(input_file) as file:
        for l in file:
            line = l.replace('    ', ' ').replace('  ', ' ').rstrip("\r\n").strip()

            tmps = line.split(" ")
            x = float(tmps[0])
            y = float(tmps[1])
            z = float(tmps[2])

            i = int((x - min_x) / RESOLUTION)
            j = int((y - max_y) / -RESOLUTION)
            # print(x, min_x, y, min_y, i, j)

            matrix[j][i] = z

    # arr = np.array(matrix)
    # np_matrix = arr.reshape(total_lines, total_columns)

    print(min_x, min_y, max_y, max_y)
    # print(matrix)

    output_file = os.path.splitext(os.path.basename(input_file))[0]

    output_raster = gdal.GetDriverByName('GTiff').Create(script_dir + '/' + output_file + '.tif',
                                                         total_lines, total_columns, 1, gdal.GDT_Float32)

    geotransform = (min_x, RESOLUTION, 0, max_y, 0, -RESOLUTION)

    # writting output raster
    output_raster.GetRasterBand(1).WriteArray(matrix)
    output_raster.SetGeoTransform(geotransform)

    srs = osr.SpatialReference()
    srs.ImportFromEPSG(32632)
    output_raster.SetProjection(srs.ExportToWkt())
    output_raster.GetRasterBand(1).SetNoDataValue(NULL_VALUE)

    output_raster = None

    # file = '/home/rasdaman/tmp/Elevation_DGM10/dgm10_32572_6019_1_sh.xyz'


process("xyzweapon.xyz")
