import os

from flask_frozen import Freezer
from views import app
import yaml

FREEZER_DESTINATION_IGNORE = ['navody']
LANGUAGES = (
    {'lang_code': 'sk'},
    {'lang_code': 'en'}
)
app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True
freezer = Freezer(app)


@freezer.register_generator
def index():
    for lang in LANGUAGES:
        yield lang


@freezer.register_generator
def materialy_detail():
    material_dirs = os.listdir('materialy')
    for material in material_dirs:
        yield {'metodika': material}
       
        with open(os.path.join('materialy', material, 'SETTINGS.yaml')) as file:
            material_settings = yaml.full_load(file)
        
        for chapter_name in material_settings['content']:
            yield {'metodika': material, 'kapitola':chapter_name['slug']}

@freezer.register_generator
def materialy_images():
    material_dirs = os.listdir('materialy')
    for material in material_dirs:
        path = os.path.join('materialy', material, 'images')
        images = next(os.walk(path))[2]

        with open(os.path.join('materialy', material, 'SETTINGS.yaml')) as file:
            material_settings = yaml.full_load(file)

        for image in images:
            yield {"image": image, "metodika":material}
            for chapter_name in material_settings['content']:
                yield {"image": image, 'metodika': material, 'kapitola':chapter_name['slug']}

@freezer.register_generator
def materialy_print():
    material_dirs = os.listdir('materialy')
    for material in material_dirs:
        path = os.path.join('materialy', material, 'images')
        images = next(os.walk(path))[2]

        with open(os.path.join('materialy', material, 'SETTINGS.yaml')) as file:
            material_settings = yaml.full_load(file)

        for image in images:
            yield {"image": image, "metodika":material}
            for chapter_name in material_settings['content']:
                yield {"image": image, 'metodika': material, 'kapitola':chapter_name['slug']}

if __name__ == '__main__':
    freezer.freeze()
