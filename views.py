#!/usr/bin/python
# -*- coding: utf8 -*-

import codecs
import os

import pdfkit
import yaml
from flask import Flask, request, render_template, redirect, url_for, send_from_directory
from markdown_to_html import markdown_to_html

app = Flask(__name__, static_url_path='/static')
app.config['FREEZER_DESTINATION'] = 'docs'
app.jinja_options = {'extensions': ['jinja2.ext.with_', 'jinja2.ext.i18n']}

CNAME = 'www.ucimeshardverom.sk'
SRC_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__)))
LOGO_PYCON = 'logo/pycon.svg'


def _get_template_variables(**kwargs):
    variables = {
        'title': 'Učíme s Hardvérom',
        'logo': LOGO_PYCON,
        'CNAME': CNAME,
    }
    variables.update(kwargs)

    return variables


# Github Pages required file
@app.route('/CNAME')
def gh_cname():
    return CNAME


# 404 website
@app.errorhandler(404)
def page_not_found(e):
    # set the 404 status explicitly
    template_variables = _get_template_variables()
    return render_template('404.html', **template_variables), 404


@app.route('/')
def index():
    return render_template('index.html', **_get_template_variables(li_index='active'))


@app.route('/skolenia/')
def skolenia():
    return render_template('skolenia.html', **_get_template_variables(li_index='active'))


@app.route('/ciele/')
def ciele():
    return render_template('ciele_projektu.html', **_get_template_variables(li_index='active'))


@app.route('/ciele_projektu/')
def ciele_projektu():
    return redirect(url_for('ciele'))


@app.route('/o_nas/')
def o_nas():
    return render_template('o_nas.html', **_get_template_variables(li_index='active'))


@app.route('/materialy/')
def materialy():
    return render_template('materialy.html', **_get_template_variables(li_index='active'))


@app.route('/zapojsa/')
def zapojsa():
    return render_template('zapojsa.html', **_get_template_variables(li_index='active'))


@app.route('/sutaz/')
def sutaz():
    return render_template('sutaz.html', **_get_template_variables(li_index='active'))


@app.route('/gdpr/')
def gdpr():
    return render_template('gdpr.html', **_get_template_variables(li_index='active'))


@app.route('/partneri/')
def partneri():
    return render_template('partneri.html', **_get_template_variables(li_index='active'))


@app.route('/hardver/')
def hardver():
    return render_template('hardver.html', **_get_template_variables(li_index='active'))


@app.route('/press_kit/')
def press_kit():
    template_variables = _get_template_variables()
    return render_template('press_kit.html', **template_variables)


# @app.route('/materialy/microbit_makecode/')
# def microbit_makecode():
#     template_variables = _get_template_variables()
#     return render_template('microbit_makecode.html', **template_variables)


@app.route('/materialy/<string:metodika>/print/')
@app.route('/materialy/<string:metodika>/<string:kapitola>/print/')
def materialy_detail_print(metodika, kapitola=None, html_template='materialy_print.html'):
    return materialy_detail(metodika, chapter_name=kapitola, html_template=html_template)


@app.route('/zacni/')
@app.route('/zacni/<string:kapitola>/')
def zacni(kapitola=None):
    return materialy_detail("zacni", chapter_name=kapitola, material_base_url="")


@app.route('/materialy/<string:tutorial_name>/')
@app.route('/materialy/<string:tutorial_name>/<string:chapter_name>/')
def materialy_detail(tutorial_name, chapter_name=None, html_template='materialy_detail.html', material_base_url="materialy/"):
    with open(os.path.join('materialy', tutorial_name, 'SETTINGS.yaml')) as file:
        material_settings = yaml.full_load(file)

    if not chapter_name:
        first_chapter_name = list(material_settings.get('content'))[0]
        chapter_name = first_chapter_name

    # if chapter_name not in [x['slug'] for x in material_settings['content']]:
    #     return "not_found"

    content_path = os.path.join('materialy', tutorial_name, chapter_name + '.md')

    with codecs.open(content_path, mode="r", encoding="utf-8") as file:
        content_raw = file.read()

    content_html = markdown_to_html(content_raw, img_url=f"/materialy/{tutorial_name}/")

    # Retrieve chapter title
    chapter_title = material_settings.get('content').get(chapter_name).get('title')

    # Retrieve Teacher Guite
    teacher_content_html = None
    teacher_guide = material_settings.get('content').get(chapter_name).get('teacher')
    if teacher_guide:
        content_path = os.path.join('materialy', tutorial_name, teacher_guide + '.md')
        with codecs.open(content_path, mode="r", encoding="utf-8") as file:
            teacher_content_raw = file.read()
            teacher_content_html = markdown_to_html(teacher_content_raw, img_url=f"/materialy/{tutorial_name}/")

    template_variables = _get_template_variables(chapter_title=chapter_title,
                                                 material_slug=tutorial_name, chapter_slug=chapter_name,
                                                 settings=material_settings, content_html=content_html,
                                                 material_settings=material_settings,
                                                 material_base_url=material_base_url,
                                                 teacher_content_html=teacher_content_html)

    return render_template(html_template, **template_variables)


# @app.route('/materialy/generate_header/<string:title>/<string:subtitle>/')
# def generate_header(title, subtitle):
#     return f"<!DOCTYPE html><html><body align='center'><h1>{title}</h1><img height='20px' src='https://upload.wikimedia.org/wikipedia/commons/0/09/Kate-icon.png'/> {subtitle}<hr></body></html>"


# @app.route('/materialy/<string:metodika>/generate_pdf')
# @app.route('/materialy/<string:metodika>/generate_pdf/<int:js_loading_time>')
# @app.route('/materialy/<string:metodika>/<string:kapitola>/generate_pdf')
# @app.route('/materialy/<string:metodika>/<string:kapitola>/generate_pdf/<int:js_loading_time>')
# def tutorial_generate_pdf(metodika, kapitola="uvod", js_loading_time=0):
#     with open(os.path.join('materialy', metodika, 'SETTINGS.yaml')) as file:
#         material_settings = yaml.full_load(file)
#
#     # Retrieve chapter title
#     for i, ch_data in enumerate(material_settings['content']):
#         if kapitola == ch_data['slug']:
#             chapter_title = ch_data['title']
#
#     # Full list of options is at https://wkhtmltopdf.org/usage/wkhtmltopdf.txt
#     options = {
#         'page-size': 'A4',
#         'margin-top': '35mm',
#         'margin-right': '15mm',
#         'margin-bottom': '25mm',
#         'margin-left': '15mm',
#         'encoding': "UTF-8",
#         'no-outline': "",
#         'title': f"Metodika: {chapter_title}",
#
#         'header-spacing': "10",
#         'header-html': f"http://127.0.0.1:5000/materialy/generate_header/BBC micro:bit & MicroPython/{chapter_title}/",
#
#         'footer-line': "",
#         'footer-font-size': "10",
#         'footer-spacing': "10",
#         'footer-center': "Licencia: CC BY SA 4.0",
#         'footer-right': "Strana [page] z [toPage]\nPosledná úprava: XX.X.XXXX",
#         'footer-left': "www.ucimeshardverom.sk\nAutor: Marek Mansell",
#
#         'disable-javascript': "",
#
#         'image-dpi': "2000",
#         'no-pdf-compression': "",
#         # 'grayscale':"",
#     }
#
#     pdfkit.from_url(f'http://127.0.0.1:5000/materialy/{metodika}/{kapitola}/print/',
#                     os.path.join('static', 'pdfs', f"{metodika}-{kapitola}.pdf"), options=options)
#
#     return send_from_directory(os.path.join('static', 'pdfs'), f"{metodika}-{kapitola}.pdf", mimetype='application/pdf',
#                                as_attachment=False, attachment_filename=f"{metodika}-{kapitola}.pdf")


# @app.route('/materialy/generate')
# def generate_all_pdfs():
#     return "s"
#     material_dirs = os.listdir('materialy')
#     for material in material_dirs:
#
#         with open(os.path.join('materialy', material, 'SETTINGS.yaml')) as file:
#             material_settings = yaml.full_load(file)
#
#         for chapter_name in material_settings['content']:
#             tutorial_generate_pdf(material, kapitola=chapter_name['slug'])
#             # print(f"{material}-{chapter_name['slug']}.pdf")
#     return "OK"


# @app.route('/materialy/<string:metodika>/images/print/<string:image>')
# # @app.route('/materialy/<string:metodika>/<string:kapitola>/print/images/<string:image>')
# def materialy_images_print(metodika, image, kapitola=None):
#     return materialy_images(metodika, image)


@app.route('/materialy/<string:metodika>/images/<string:image>')
# @app.route('/materialy/<string:metodika>/<string:kapitola>/images/<string:image>')
def materialy_images(metodika, image, kapitola=None):
    return send_from_directory(os.path.join('materialy', metodika, 'images'), image, mimetype='image/gif')


@app.route('/zacni/images/<string:image>')
# @app.route('/zacni/<string:kapitola>/images/<string:image>')
def materialy_zacni_images(image, metodika="zacni", kapitola=None):
    return materialy_images(metodika, image, kapitola)


@app.route('/materialy/save_makecode_image/<string:id>', methods=['GET', 'POST'])
def save_makecode_image(id):
    if request.method == 'POST':
        with open(os.path.join('static', 'makecode_cached_images', id), "w") as file:
            file.write(f"<img class='img-fluid' src='{request.data.decode()}'/>")

    return "OK"


if __name__ == "__main__":
    app.run(debug=True, host=os.environ.get('FLASK_HOST', '127.0.0.1'),
            port=int(os.environ.get('FLASK_PORT', 5000)))
