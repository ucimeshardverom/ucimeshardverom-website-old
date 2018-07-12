#!/usr/bin/python
# -*- coding: utf8 -*-
import os
from datetime import datetime
from flask import Flask, g, request, render_template, abort, make_response, redirect, url_for
from flask_babel import Babel, gettext

app = Flask(__name__, static_url_path='/static')
app.config['BABEL_DEFAULT_LOCALE'] = 'sk'
app.config['FREEZER_DESTINATION'] = 'docs'
app.jinja_options = {'extensions': ['jinja2.ext.with_', 'jinja2.ext.i18n']}
babel = Babel(app)

CNAME = 'www.ucimeshardverom.sk'
SRC_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__)))
LOGO_PYCON = 'logo/pycon.svg'

# LANGS = ('sk', 'en', 'de', 'hu', 'cs', 'ru')
LANGS = ('sk', 'en')

TIME_FORMAT = '%Y-%m-%dT%H:%M:%S+00:00'
NOW = datetime.utcnow().strftime(TIME_FORMAT)


def get_mtime(filename):
    mtime = datetime.fromtimestamp(os.path.getmtime(filename))
    return mtime.strftime(TIME_FORMAT)


SITEMAP_DEFAULT = {'prio': '0.1', 'freq': 'weekly'}
SITEMAP = {
    'sitemap.xml': {'prio': '0.9', 'freq': 'daily', 'lastmod': get_mtime(__file__)},
    'index.html': {'prio': '1', 'freq': 'daily'},
}
LDJSON = {
    "@context": "http://schema.org",
    "@type": "Organization",
    "name": "SPy o.z.",
    "url": "https://"+ CNAME,
    "logo": "https://"+ CNAME +"/static/img/logo/python.svg",
    "sameAs": [
        "https://facebook.com/pyconsk",
        "https://twitter.com/pyconsk",
        "https://www.linkedin.com/company/spy-o--z-",
        "https://github.com/pyconsk",
    ]
}


@app.before_request
def before():
    if request.view_args and 'lang_code' in request.view_args:
        g.current_lang = request.view_args['lang_code']
        request.view_args.pop('lang_code')


@babel.localeselector
def get_locale():
    # try to guess the language from the user accept
    # header the browser transmits. The best match wins.
    # return request.accept_languages.best_match(['de', 'sk', 'en'])
    return g.get('current_lang', app.config['BABEL_DEFAULT_LOCALE'])


def _get_template_variables(**kwargs):
    variables = {
        'title': gettext('Učíme s Hardvérom'),
        'logo': LOGO_PYCON,
        'ld_json': LDJSON,
        'langs': LANGS,
        'CNAME': CNAME,
    }
    variables.update(kwargs)

    if 'current_lang' in g:
        variables['lang_code'] = g.current_lang

        if g.current_lang not in LANGS:
            return abort(404)
    else:
        variables['lang_code'] = app.config['BABEL_DEFAULT_LOCALE']

    return variables


@app.route('/CNAME')
def gh_cname():
    return CNAME


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


@app.route('/zapojsa/skola/')
def zapoj_sa_skola():
    return render_template('zapoj_sa_skola.html', **_get_template_variables(li_index='active'))


@app.route('/zapojsa/rodic/')
def zapoj_sa_rodic():
    return render_template('zapoj_sa_rodic.html', **_get_template_variables(li_index='active'))


@app.route('/zapojsa/dobrovolnik/')
def zapoj_sa_dobrovolnik():
    return render_template('zapoj_sa_dobrovolnik.html', **_get_template_variables(li_index='active'))


@app.route('/zapojsa/sponzor/')
def zapoj_sa_sponzor():
    return render_template('zapoj_sa_sponzor.html', **_get_template_variables(li_index='active'))


@app.route('/blog/')
def blog():
    return render_template('blog.html', **_get_template_variables(li_index='active'))


@app.route('/mapa/')
def mapa():
    return render_template('zapojene_skoly.html', **_get_template_variables(li_index='active'))

@app.route('/zapojene_skoly/')
def zapojene_skoly():
    return redirect(url_for('mapa'))


@app.route('/sutaz/')
def sutaz():
    return render_template('sutaz.html', **_get_template_variables(li_index='active'))


@app.route('/partneri/')
def partneri():
    return render_template('partneri.html', **_get_template_variables(li_index='active'))


@app.route('/hardver/')
def hardver_ako_pomocka():
    return render_template('hardver_ako_pomocka.html', **_get_template_variables(li_index='active'))


@app.route('/microbit/')
def microbit():
    return render_template('microbit.html', **_get_template_variables(li_index='active'))


@app.route('/nodemcu/')
def nodemcu():
    return render_template('nodemcu.html', **_get_template_variables(li_index='active'))


@app.route('/projekty/')
def projekty():
    return render_template('hw_projekty.html', **_get_template_variables(li_index='active'))


@app.route('/hw_projekty/')
def hw_projekty():
    return redirect(url_for('ciele'))


@app.route('/kde_kupit/')
def kde_kupit():
    return render_template('kde_kupit.html', **_get_template_variables(li_index='active'))


def get_lastmod(route, sitemap_entry):
    """Used by sitemap() below"""
    if 'lastmod' in sitemap_entry:
        return sitemap_entry['lastmod']

    template = route.rule.split('/')[-1]
    template_file = os.path.join(SRC_DIR, 'templates', template)

    if os.path.exists(template_file):
        return get_mtime(template_file)

    return NOW


@app.route('/sitemap.xml', methods=['GET'])
def sitemap():
    """Generate sitemap.xml. Makes a list of urls and date modified."""
    domain = 'https://'+ CNAME
    pages = []

    # static pages
    for rule in app.url_map.iter_rules():

        if "GET" not in rule.methods:
            raise Exception

        if 'lang_code' in rule.arguments:
            indx = rule.rule.replace('/<lang_code>/', '')

            for lang in LANGS:
                alternate = []

                for alt_lang in LANGS:
                    if alt_lang != lang:
                        alternate.append({
                            'lang': alt_lang,
                            'url': domain + rule.rule.replace('<lang_code>', alt_lang).replace('index.html', '')
                        })

                sitemap_data = SITEMAP.get(indx, SITEMAP_DEFAULT)
                pages.append({
                    'loc': domain + rule.rule.replace('<lang_code>', lang).replace('index.html', ''),
                    'alternate': alternate,
                    'lastmod': get_lastmod(rule, sitemap_data),
                    'freq': sitemap_data['freq'],
                    'prio': sitemap_data['prio'],
                })
        elif rule.rule == '/sitemap.xml':
            indx = rule.rule.replace('/', '')
            sitemap_data = SITEMAP.get(indx, SITEMAP_DEFAULT)
            pages.append({
                'loc': domain + rule.rule,
                'lastmod': get_lastmod(rule, sitemap_data),
                'freq': sitemap_data['freq'],
                'prio': sitemap_data['prio'],
            })

    sitemap_xml = render_template('sitemap_template.xml', pages=pages)
    response = make_response(sitemap_xml)
    response.headers["Content-Type"] = "text/xml"

    return response


if __name__ == "__main__":
    app.run(debug=True, host=os.environ.get('FLASK_HOST', '127.0.0.1'), port=int(os.environ.get('FLASK_PORT', 5000)))
