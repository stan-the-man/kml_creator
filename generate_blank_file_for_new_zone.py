# in this file we will generate a new KML for use, given a list of ID's

# ID's in a list in a text file
# return a KML with folders for all ID's and a boundary
# option to run with a list of push pin locations

import re
from kml_components import KMLCreator as kml
from email_attach import email_myself

new_kml_file = "new_kml_doc.kml"
outf = open(new_kml_file, 'w')
info_file = open('id_lon_lat.txt', 'r')
#info_file = open('ids_for_new_file.txt', 'r')

agency_name = "San Jose Water"
new_kml = kml.header(agency_name) + kml.meter_style() + kml.boundary_style() + kml.overall_folder_start(agency_name)

# info comes id,latitude,longitude in the file
info = [tuple(line.split(',')) for line in info_file]

sites = {}
for id, lat, lon, service_num, service_addr, water_use in info:
    water_use = water_use.strip()
    if sites.get(id) is None:
        sites[id] = []
    sites[id].append((lon, lat, service_num, service_addr, water_use))

for id, meter in sites.iteritems():
    new_kml += kml.folder_in_folder_start(id)
    new_kml += kml.boundary_poly()
    for lon, lat, service_num, service_addr, water_use in meter:
        service_addr = re.sub(r'&','and', service_addr)
        if lon != '#N/A' or lat != '#N/A':
            new_kml += kml.meter_icon(id, lon, lat, service_num, service_addr, water_use)
    new_kml += kml.folder_in_folder_end()
new_kml += kml.overall_folder_close()

outf.write(new_kml)
outf.close()
email_myself(new_kml_file)
