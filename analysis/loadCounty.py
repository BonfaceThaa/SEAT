import os
from django.contrib.gis.utils import LayerMapping
from .models import County

county_mapping = {
    'geom' : 'MULTIPOLYGON',
}

county_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'County[1].shp'),
)

def run(verbose=True):
    lm = LayerMapping(
        County, county_shp, county_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)