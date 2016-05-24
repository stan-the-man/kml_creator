class KMLCreator():

    @staticmethod
    def header(name):
        return """<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">
<Document>
    <name>%s.kml</name>
        """ % (name)

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
    def overall_folder_close():    
        return """</Folder>
</Document>
</kml>
    """
