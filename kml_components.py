class KMLCreator():

    @staticmethod
    def header(name):
        return """<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">
<Document>
    <name>%s.kml</name>
        """ % (name)

    @staticmethod
    def placemark_style():
        return """<Style id="s_ylw-pushpin_hl">
        <IconStyle>
            <scale>1.3</scale>
            <Icon>
                <href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href>
            </Icon>
            <hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>
        </IconStyle>
    </Style>
    <StyleMap id="boundaryPoly1210666825101131200012000010423950104012628108200220023653">
        <Pair>
            <key>normal</key>
            <styleUrl>#boundaryPoly12201701227625140102030021700121013111910600210512110</styleUrl>
        </Pair>
        <Pair>
            <key>highlight</key>
            <styleUrl>#boundaryPoly12331321942161700510000212103521017126125045003121460</styleUrl>
        </Pair>
    </StyleMap>
    <StyleMap id="m_ylw-pushpin">
        <Pair>
            <key>normal</key>
            <styleUrl>#s_ylw-pushpin</styleUrl>
        </Pair>
        <Pair>
            <key>highlight</key>
            <styleUrl>#s_ylw-pushpin_hl</styleUrl>
        </Pair>
    </StyleMap>
    <Style id="s_ylw-pushpin">
        <IconStyle>
            <scale>1.1</scale>
            <Icon>
                <href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href>
            </Icon>
            <hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>
        </IconStyle>
    </Style>
    """

    @staticmethod
    def boundary_style():
        return """<Style id="boundaryPoly12201701227625140102030021700121013111910600210512110">
        <LineStyle>
            <color>ff0000ff</color>
            <width>2</width>
        </LineStyle>
        <PolyStyle>
            <fill>0</fill>
        </PolyStyle>
    </Style>
    <Style id="boundaryPoly12331321942161700510000212103521017126125045003121460">
        <LineStyle>
            <color>ff0000ff</color>
            <width>2</width>
        </LineStyle>
        <PolyStyle>
            <fill>0</fill>
        </PolyStyle>
    </Style>
    <StyleMap id="boundaryPoly1210666825101131200012000010423950104012628108200220023653">
        <Pair>
            <key>normal</key>
            <styleUrl>#boundaryPoly12201701227625140102030021700121013111910600210512110</styleUrl>
        </Pair>
        <Pair>
            <key>highlight</key>
            <styleUrl>#boundaryPoly12331321942161700510000212103521017126125045003121460</styleUrl>
        </Pair>
    </StyleMap>
        """

    @staticmethod
    def overall_folder_start(name):
        return """<Folder>
        <name>%s</name>
        <open>1</open>
    """ % (name)

    @staticmethod
    def folder_no_pin(id):
        return """<Folder>
                <name>%s</name>
                <open>1</open>
                <Placemark>
                    <name>Boundary</name>
                    <styleUrl>#boundaryPoly1210666825101131200012000010423950104012628108200220023653</styleUrl>
                    <Polygon>
                        <tessellate>1</tessellate>
                        <outerBoundaryIs>
                            <LinearRing>
                                <coordinates>
                                </coordinates>
                            </LinearRing>
                        </outerBoundaryIs>
                    </Polygon>
                </Placemark>
            </Folder>
        """ % (id)
    
    @staticmethod
    def folder_with_pin(lon, lat, id):
        return """<Folder>
                <name>%s</name>
                <open>1</open>
                <Placemark>
                    <name>Boundary</name>
                    <styleUrl>#boundaryPoly1210666825101131200012000010423950104012628108200220023653</styleUrl>
                    <Polygon>
                        <tessellate>1</tessellate>
                        <outerBoundaryIs>
                            <LinearRing>
                                <coordinates>
                                </coordinates>
                            </LinearRing>
                        </outerBoundaryIs>
                    </Polygon>
                </Placemark>
                <Placemark>
                    <name>%s</name>
                    <LookAt>
                        <longitude>%s</longitude>
                        <latitude>%s</latitude>
                        <altitude>0</altitude>
                        <heading>0</heading>
                        <tilt>0</tilt>
                        <range>1000</range>
                        <gx:altitudeMode>relativeToSeaFloor</gx:altitudeMode>
                    </LookAt>
                    <styleUrl>#m_ylw-pushpin</styleUrl>
                    <Point>
                        <gx:drawOrder>1</gx:drawOrder>
                        <coordinates>%s,%s,0</coordinates>
                    </Point>
                </Placemark>
            </Folder>
        """ % (id, id, lon, lat, lon, lat)


    @staticmethod
    def overall_folder_close():
        return """</Folder>
</Document>
</kml>
    """
