#!/usr/bin/python
# -*- coding: utf8 -*-

import codecs
import os
from time import sleep

from flask import Flask, request, render_template, redirect, url_for, send_from_directory
from markdown_to_html import markdown_to_html, markdown_meta
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
    global app
    variables = {
        'title': 'Učíme s Hardvérom',
        'logo': LOGO_PYCON,
        'CNAME': CNAME,
        'development_environment': app.config.get("development_environment", True)
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
    return render_template('pdf_template_default.html', **_get_template_variables(li_index='active'))


if __name__ == "__main__":
    app.run(debug=True, host=os.environ.get('FLASK_HOST', '127.0.0.1'),
            port=int(os.environ.get('FLASK_PORT', 5000)))
