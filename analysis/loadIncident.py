import os
from django.contrib.gis.utils import LayerMapping
from .models import Incidents

incidents_mapping = {
    'list_of_at' : 'list_of_at',
    'f2' : 'F2',
    'x' : 'X',
    'y' : 'Y',
    'casulties' : 'Casulties',
    'geom' : 'MULTIPOINT',
}

incidents_shp = os.path.abspath(
	#parcel_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/LandParcels.shp'))
    os.path.join(os.path.dirname(__file__), 'data', 'ATTACK_INCIDENTS[1].shp'),

)

def run(verbose=True):
    lm = LayerMapping(
        Incidents, incidents_shp, incidents_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)