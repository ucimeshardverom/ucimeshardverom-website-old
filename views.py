#!/usr/bin/python
# -*- coding: utf8 -*-

import codecs
import os
from time import sleep

import pdfkit
import yaml
from flask import Flask, request, render_template, redirect, url_for, send_from_directory
from markdown_to_html import markdown_to_html, markdown_meta
from collections import OrderedDict
from utils import get_tutorial_settings

from selenium import webdriver
import json

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


@app.route('/test/')
def test():
    return render_template('test.html', **_get_template_variables(li_index='active'))


@app.route('/press_kit/')
def press_kit():
    template_variables = _get_template_variables()
    return render_template('press_kit.html', **template_variables)

@app.route('/materialy/<string:metodika>/print/')
@app.route('/materialy/<string:metodika>/print/<string:html_template>')
@app.route('/materialy/<string:metodika>/<string:kapitola>/print/')
@app.route('/materialy/<string:metodika>/<string:kapitola>/print/<string:html_template>')
def materialy_detail_print(metodika, kapitola=None, html_template='materialy_print.html'):
    return materialy_detail(metodika, chapter_name=kapitola, html_template=html_template)


@app.route('/materialy/<string:metodika>/print/teacher/')
@app.route('/materialy/<string:metodika>/print/<string:html_template>/teacher/')
@app.route('/materialy/<string:metodika>/<string:kapitola>/print/teacher/')
@app.route('/materialy/<string:metodika>/<string:kapitola>/print/<string:html_template>/teacher/')
def materialy_detail_print_teacher(metodika, kapitola=None, html_template='materialy_print.html'):
    return materialy_detail(metodika, chapter_name=kapitola, html_template=html_template, print_teacher_pdf=True)


# @app.route('/materialy/<string:metodika>/telekom/')
# @app.route('/materialy/<string:metodika>/<string:kapitola>/telekom/')
# def materialy_detail_print_telekom(metodika, kapitola=None, html_template='materialy_print_telekom.html'):
    
#     return materialy_detail(metodika, chapter_name=kapitola, html_template=html_template)


@app.route('/zacni/')
@app.route('/zacni/<string:kapitola>/')
def zacni(kapitola=None):
    return materialy_detail("zacni", chapter_name=kapitola, material_base_url="", html_template="materialy_detail_zacni.html")


@app.route('/materialy/<string:tutorial_name>/')
@app.route('/materialy/<string:tutorial_name>/<string:chapter_name>/')
def materialy_detail(tutorial_name, chapter_name=None, html_template='materialy_detail.html', material_base_url="materialy/", print_teacher_pdf=False):
    
    material_settings = get_tutorial_settings(tutorial_name, chapter_name)

    if not chapter_name:
        chapter_name = material_settings.get('chapter_name')

    material_content = material_settings.get('content')

    md_file_path = os.path.split(str(material_content.get(chapter_name).get("path")))

    content_path = os.path.join('materialy', tutorial_name, *md_file_path)

    with codecs.open(content_path, mode="r", encoding="utf-8") as file:
        content_raw = file.read()

    for _chapter in material_settings.get('content'):
        _md_file_path = str(material_content.get(_chapter).get("path")).split("/")
        _content_path = os.path.join('materialy', tutorial_name, *_md_file_path)
        with codecs.open(_content_path, mode="r", encoding="utf-8") as file:
            _content_raw = file.read()

        meta_title = markdown_meta(_content_raw).get('title')
        if meta_title:
            material_settings.get('content').get(_chapter)['title'] = meta_title[0]

        meta_sub_title = markdown_meta(_content_raw).get('subtitle')
        if meta_sub_title:
            material_settings.get('content').get(_chapter)['subtitle'] = meta_sub_title[0]

    content_html = markdown_to_html(content_raw, img_url=f"/materialy/{tutorial_name}/{chapter_name}/", html_template=html_template)

    # Retrieve chapter title
    chapter_title = material_settings.get('content').get(chapter_name).get('title')
    chapter_subtitle = material_settings.get('content').get(chapter_name).get('subtitle')

    # Retrieve Teacher Guite
    teacher_content_html = None
    teacher_guide = markdown_meta(content_raw).get('teacher')
    if teacher_guide:
        content_path = os.path.join('materialy', tutorial_name, md_file_path[0], md_file_path[1].split('.')[0] + "_teacher.md")
        with codecs.open(content_path, mode="r", encoding="utf-8") as file:
            teacher_content_raw = file.read()
            teacher_content_html = markdown_to_html(teacher_content_raw, img_url=f"/materialy/{tutorial_name}/", html_template=html_template)

    if print_teacher_pdf:
        if not teacher_guide:
            return ""
        content_html = teacher_content_html


    material_settings['downloads'] = {}
    
    ## Donwloads Tab
    pdf_to_download = os.path.join(os.getcwd(), 'static', 'pdfs', f"{tutorial_name}-{chapter_name}.pdf")
    if os.path.exists(pdf_to_download):
        material_settings['downloads']["Stiahnuť Návod ako PDF"] = url_for('static', filename=os.path.join('pdfs', f"{tutorial_name}-{chapter_name}.pdf"))

    pdf_teacher_to_download = os.path.join(os.getcwd(), 'static', 'pdfs', f"{tutorial_name}-{chapter_name}-teacher.pdf")
    if os.path.exists(pdf_to_download):
        material_settings['downloads']["Stiahnuť Meodiku pre učiteľa ako PDF"] = url_for('static', filename=os.path.join('pdfs', f"{tutorial_name}-{chapter_name}-teacher.pdf"))


    template_variables = _get_template_variables(chapter_title=chapter_title,
                                                 chapter_subtitle=chapter_subtitle,
                                                 material_slug=tutorial_name, chapter_slug=chapter_name,
                                                 settings=material_settings, content_html=content_html,
                                                 material_settings=material_settings,
                                                 material_base_url=material_base_url,
                                                 teacher_content_html=teacher_content_html,
                                                 chapter_id=material_settings['chapter_id'])

    return render_template(html_template, **template_variables)


@app.route('/materialy/<string:tutorial_name>/<string:chapter_name>/pdf')
@app.route('/materialy/<string:tutorial_name>/<string:chapter_name>/<string:html_template>/pdf')
def materialy_detail_pdf(tutorial_name, chapter_name=None, html_template='materialy_print.html'):

    material_settings = get_tutorial_settings(tutorial_name, chapter_name)

    if not chapter_name:
        first_chapter_name = list(material_settings.get('content'))[0]
        chapter_name = first_chapter_name

    material_content = material_settings.get('content')

    md_file_path = str(material_content.get(chapter_name).get("path")).split("/")
    md_folder_name = str(md_file_path[0])
    md_folder_number = "_".join(md_folder_name.split("_")[0:2])

    appState = {
        "recentDestinations": [
            {
                "id": "Save as PDF",
                "origin": "local",
                "account": "",
            }
        ],
        "selectedDestinationId": "Save as PDF",
        "version": 2,
        "isHeaderFooterEnabled": False,
        "isCssBackgroundEnabled": True,
    }

    save_directory = os.path.join(os.getcwd(), 'static', 'pdfs')
    filename = f"{md_folder_number}-{tutorial_name}-{chapter_name}.pdf"
    filename_teacher = f"{md_folder_number}-{tutorial_name}-{chapter_name}-teacher.pdf"

    if os.path.exists(os.path.join(save_directory, filename)):
        os.remove(os.path.join(save_directory, filename))

    if os.path.exists(os.path.join(save_directory, filename_teacher)):
        os.remove(os.path.join(save_directory, filename_teacher))

    profile = {
        'printing.print_preview_sticky_settings.appState': json.dumps(appState),
        'savefile.default_directory': save_directory
        }

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('prefs', profile)
    chrome_options.add_argument('--kiosk-printing')
    # chrome_options.add_argument("--headless")

    if os.path.exists("chromedriver.exe"):
        chromedriver_path = os.path.abspath("chromedriver.exe")
    elif os.path.exists("chromedriver"):
        chromedriver_path = os.path.abspath("chromedriver")
    else:
        return "Please put 'chromedriver' or 'chromedriver.exe' into the project directory."

    driver = webdriver.Chrome(options=chrome_options, executable_path=chromedriver_path)
    driver.get(url_for('materialy_detail_print', metodika=tutorial_name, kapitola=chapter_name, html_template=html_template, _external=True))
    driver.execute_script(f"var tempTitle = document.title;document.title = '{filename}';window.print();document.title = tempTitle;")
    while not os.path.exists(os.path.join(save_directory, filename)):
        sleep(1)
    driver.quit()



    return send_from_directory(save_directory, filename, mimetype='application/pdf',
                               as_attachment=False, attachment_filename=filename)

@app.route('/materialy/<string:tutorial_name>/all_pdfs')
@app.route('/materialy/<string:tutorial_name>/<string:html_template>/all_pdfs')
def materialy_detail_all_pdfs(tutorial_name, html_template='materialy_print.html'):

    material_settings = get_tutorial_settings(tutorial_name, None)

    for _chapter in material_settings.get('content'):
        materialy_detail_pdf(tutorial_name, chapter_name=_chapter, html_template=html_template)

    # return str(material_settings.get('content'))

@app.route('/materialy/<string:tutorial_name>/<string:chapter_name>/images/<string:image>')
def materialy_images(tutorial_name, image, chapter_name=None):
    
    material_settings = get_tutorial_settings(tutorial_name, chapter_name)

    return send_from_directory(os.path.join('materialy', tutorial_name, material_settings['chapter_folder'], 'images'), image, mimetype='image/gif')


@app.route('/materialy/save_makecode_image/<string:id>', methods=['GET', 'POST'])
def save_makecode_image(id):
    if request.method == 'POST':
        with open(os.path.join('static', 'makecode_cached_images', id), "w") as file:
            file.write(f"<img class='img-fluid' src='{request.data.decode()}'/>")

    return "OK"


if __name__ == "__main__":
    app.run(debug=True, host=os.environ.get('FLASK_HOST', '127.0.0.1'),
            port=int(os.environ.get('FLASK_PORT', 5000)))
