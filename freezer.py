import os

from flask_frozen import Freezer
from views import app

from utils import get_tutorial_settings

app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True
app.config['development_environment'] = False
freezer = Freezer(app)


@freezer.register_generator
def zacni():
    material = "zacni"

    material_settings = get_tutorial_settings(material, None)

    for chapter_name in material_settings['content']:
        yield {'kapitola': chapter_name}


@freezer.register_generator
def materialy_detail():
    material_dirs = os.listdir('materialy')
    for material in material_dirs:
        print(material)
        yield {'tutorial_name': material}

        material_settings = get_tutorial_settings(material, None)

        for chapter_name in material_settings['content']:
            yield {'tutorial_name': material, 'chapter_name': chapter_name, 'html_template': 'materialy_detail.html'}


@freezer.register_generator
def materialy_images():
    material_dirs = os.listdir('materialy')
    for material in material_dirs:
        material_settings = get_tutorial_settings(material, None)

        for _chapter_name in material_settings['content']:
            _chapter_folder = material_settings['content'][_chapter_name]['path'].split("/")[0]
            _img_folder_path = os.path.join('materialy', material, _chapter_folder, 'images')

            # print(_chapter_name)

            if os.path.exists(_img_folder_path):
                _images = os.listdir(_img_folder_path)
                for _image in _images:
                    yield {"tutorial_name": material, "image": _image, 'chapter_name': _chapter_name}
                    # print({"tutorial_name": material, "image": _image, 'chapter_name': _chapter_name})


if __name__ == '__main__':
    freezer.run()
