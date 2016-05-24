# in this file we will generate a new KML for use, given a list of ID's

# ID's in a list in a text file
# return a KML with folders for all ID's and a boundary
# option to run with a list of push pin locations

from kml_components import KMLCreator as kml
from email_attach import email_myself

new_kml_file = "new_kml_doc.kml"
outf = open(new_kml_file, 'w')
info_file = open('ids_for_new_file.txt', 'r')

new_kml = kml.header("Somnoi") + kml.boundary_style() + kml.overall_folder_start("Somnoi")

# info comes id,longitude,latitude in the file
info = [tuple(line.split(',')) for line in info_file]

for id, lon, lat, in info:
    new_kml += kml.folder_with_pin(lon, lat.strip(), id)
new_kml += kml.overall_folder_close()


outf.write(new_kml)
outf.close()
email_myself(new_kml_file)
