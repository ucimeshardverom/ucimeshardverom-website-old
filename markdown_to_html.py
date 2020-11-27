import markdown
from bs4 import BeautifulSoup
import os
from markdown.extensions.toc import TocExtension


def markdown_meta(raw_markdown):
    md = markdown.Markdown(extensions = ['meta'])
    html = md.convert(raw_markdown)
    return md.Meta


def markdown_to_html(raw_markdown, img_url="", html_template=None):

    extension_configs = {
        'smarty': {
            'substitutions': {
                'left-double-quote': '&bdquo;',
                'right-double-quote': '&ldquo;'
            }
        }
    }

    content_html = markdown.markdown(raw_markdown, extensions=[
        'meta', 'admonition', 'markdown_captions', 'fenced_code', 'smarty', 'tables', 'footnotes', 'extra', TocExtension(toc_depth="3-6")], extension_configs=extension_configs)

    # Figures and FigCaptions
    content_html = content_html.replace("<figure", "<figure class='mt-2 mb-2'")
    content_html = content_html.replace("<figcaption", "<figcaption class='text-center text-muted font-italic'")

    # Alerts
    content_html = content_html.replace("<div class=\"admonition danger\">", "<div class=\"alert alert-danger\">")
    content_html = content_html.replace("<div class=\"admonition primary\">", "<div class=\"alert alert-primary\">")
    content_html = content_html.replace("<div class=\"admonition secondary\">", "<div class=\"alert alert-secondary\">")
    content_html = content_html.replace("<div class=\"admonition success\">", "<div class=\"alert alert-success\">")
    content_html = content_html.replace("<div class=\"admonition warning\">", "<div class=\"alert alert-warning\">")
    content_html = content_html.replace("<div class=\"admonition info\">", "<div class=\"alert alert-info\">")
    content_html = content_html.replace("<div class=\"admonition light\">", "<div class=\"alert alert-light\">")
    content_html = content_html.replace("<div class=\"admonition dark\">", "<div class=\"alert alert-dark\">")


    if html_template in ["materialy_print_telekom.html", "materialy_print.html"]:
        content_html = content_html.replace("<p>// LEFT</p>", "<div class=\"row text-justify mt-4 mb-4\"><div class=\"col-6\">")
        content_html = content_html.replace("<p>// RIGHT</p>", "</div><div class=\"col-6\">")
    else:
        content_html = content_html.replace("<p>// LEFT</p>", "<div class=\"row text-justify mt-4 mb-4\"><div class=\"col-lg-6\">")
        content_html = content_html.replace("<p>// RIGHT</p>", "</div><div class=\"col-lg-6\">")

    content_html = content_html.replace("<p>// END</p>", "</div></div>")
    content_html = content_html.replace("<p>// NEWPAGE</p>", "<div style=\"page-break-after: always;\"></div>")
    
    content_html = content_html.replace("<div class=\"admonition magenta\">", "<div class=\"alert alert-telekom\">")

    content_html = content_html.replace("<p><img", "<p class=\"mb-0\"><img")

    # Put H1 and H2 titles in <span> tag
    soup = BeautifulSoup(content_html, "html.parser")
    for h1 in soup.find_all('h1'):
        text = h1.getText()
        h1.clear()
        new_tag = soup.new_tag("span")
        new_tag.string = str(text)
        h1.insert(1, new_tag)
    for h2 in soup.find_all('h2'):
        text = h2.getText()
        h2.clear()
        new_tag = soup.new_tag("span")
        new_tag.string = str(text)
        h2.insert(1, new_tag)
    content_html = str(soup)



    # Alert titles
    content_html = content_html.replace(
        "<p class=\"admonition-title\">", "<p class=\"h4\">")

    # Tables
    content_html = content_html.replace(
        "<table>", "<table class=\"table table-striped\">")

    # Blockquotes
    content_html = content_html.replace("<blockquote>", "<blockquote class=\"blockquote\">")

    # Images
    content_html = content_html.replace("<img ", "<img class=\"img-fluid\" ")

    soup = BeautifulSoup(content_html, "html.parser")

    # MakeCode images - render HTML from MakeCode share ID
    for tag in soup.find_all('pre'):
        if not tag.get('data-packageid') and not tag.get('id') and tag.code and tag.code.get('class') and \
                tag.code.get('class')[0] == "makecode":
            code_id = tag.code.string.strip()
            makecode_html = BeautifulSoup(f"""<div class="text-center">"""
                                          f"""<pre id="{code_id}" data-packageid="{code_id}"></pre>"""
                                          f"""<p class="text-muted font-italic">Edituj a stiahni: """
                                          f"""<a target="_blank" href="http://makecode.microbit.org/{code_id}">"""
                                          f"""http://makecode.microbit.org/{code_id}</a></p></div>""", "html.parser")
            tag.replace_with(makecode_html)
        elif not tag.get('data-packageid') and not tag.get('id') and tag.code and tag.code.get('class') and \
                tag.code.get('class')[0] == "makecode-no-link":
            code_id = tag.code.string.strip()
            makecode_html = BeautifulSoup(f"""<div class="text-center">"""
                                          f"""<pre id="{code_id}" data-packageid="{code_id}"></pre>"""
                                          f"""</div>""", "html.parser")
            tag.replace_with(makecode_html)
        elif not tag.get('data-packageid') and not tag.get('id') and tag.code and tag.code.get('class') and \
                tag.code.get('class')[0] == "makecode-link-only":
            code_id = tag.code.string.strip()
            makecode_html = BeautifulSoup(f"""<div class="text-center">"""
                                          f"""<p class="text-muted font-italic">Edituj a stiahni: """
                                          f"""<a target="_blank" href="http://makecode.microbit.org/{code_id}">"""
                                          f"""http://makecode.microbit.org/{code_id}</a></p></div>""", "html.parser")
            tag.replace_with(makecode_html)
        elif not tag.get('data-packageid') and not tag.get('id') and tag.code and tag.code.get('class') and \
                tag.code.get('class')[0] == "makecode-snippet":
            code_id = tag.code.string.strip()
            makecode_html = BeautifulSoup(f"""<div class="text-center">"""
                                          f"""<pre id="{code_id}" data-packageid="{code_id}" class="makecode-snippet"></pre>"""
                                          f"""</div>""", "html.parser")
            tag.replace_with(makecode_html)

    # MakeCode images - load from buffer (if image present)
    for tag in soup.find_all('pre'):
        if tag.get('data-packageid') and tag.get('id') and tag.get('data-packageid') == tag.get('id'):
            cached_img_path = os.path.join(
                'static', 'makecode_cached_images', tag.get('data-packageid'))
            if os.path.isfile(cached_img_path):
                with open(cached_img_path, "r") as f:
                    cached_img_tag = BeautifulSoup(f.read(), "html.parser")
                    tag.replace_with(cached_img_tag)

    # Make IFRAMES (such as Youtube videos) resposive
    for iframe in soup.find_all('iframe'):
        iframe['class'] = "embed-responsive-item"
        iframe.wrap(soup.new_tag("div", attrs={"class": "embed-responsive embed-responsive-16by9"}))
    content_html = soup

    # Change Image urls to the base of the tutorial url
    for image_tag in soup.find_all('img'):
        if image_tag.get('src').startswith('images/'):
            image_tag['src'] = img_url + image_tag['src']
        image_tag['class'] = " ".join(image_tag.get('class', " ")) + " img-fluid pt-2"
        image_tag.wrap(soup.new_tag("div", attrs={"class": "text-center"}))
    content_html = soup

    return content_html
