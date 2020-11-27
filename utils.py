import os
import yaml
from collections import OrderedDict

def get_tutorial_settings(tutorial_slug, chapter_slug):
    tutorial_name = tutorial_slug
    chapter_name = chapter_slug

    MATERIALS_IGNORED_FILES = ["SETTINGS.yaml", "images"]

    material_path = os.path.join(os.getcwd(), 'materialy', tutorial_name)

    files_in_dir = os.listdir(material_path)
    folders_in_dir = []

    files_in_dir.sort()
    
    for _ignored_filename in MATERIALS_IGNORED_FILES:
        if _ignored_filename in files_in_dir:
            files_in_dir.remove(_ignored_filename)
    
    for _file in files_in_dir:
        if os.path.isdir(os.path.join(material_path, _file)):
            folders_in_dir.append(_file)

    with open(os.path.join('materialy', tutorial_name, 'SETTINGS.yaml')) as file:
        material_settings = yaml.full_load(file)

    material_settings['content'] = OrderedDict()

    material_settings['chapter_id'] = "0."

    material_settings['prev_chapter'] = None
    material_settings['next_chapter'] = None

    prev_chapter = None
    _next_chapter_flag = False

    for _folder in folders_in_dir:
        _chapter_slug = _folder.split("_")[2:]
        _chapter_slug = "_".join(_chapter_slug)
        material_settings['content'][_chapter_slug] = {}
        material_settings['content'][_chapter_slug]['path'] = f"{os.path.join(_folder, _chapter_slug)}.md"

        if not chapter_name:
            material_settings['chapter_name'] = _chapter_slug
            chapter_name = _chapter_slug
        
        if _folder.split("_")[1] == "00":
            material_settings['content'][_chapter_slug]['chapter'] = True
            material_settings['content'][_chapter_slug]['index'] = f"{int(_folder.split('_')[0])}."
        else:
            material_settings['content'][_chapter_slug]['index'] = f"{int(_folder.split('_')[0])}.{int(_folder.split('_')[1])}."

        if _next_chapter_flag:
            material_settings['next_chapter'] = _chapter_slug
            _next_chapter_flag = False

        if _chapter_slug == chapter_name:
            material_settings['chapter_id'] = material_settings['content'][_chapter_slug]['index']
            material_settings['chapter_folder'] = _folder
            material_settings['prev_chapter'] = prev_chapter
            _next_chapter_flag = True

        prev_chapter = _chapter_slug

    return material_settings