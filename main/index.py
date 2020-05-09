from flask import Blueprint, render_template, request, session

main_blue = Blueprint('main_blue', __name__)

@main_blue.route('/index')
def index() :
    data = {'confirmator' : 4212, 'heal' : 31, 'die':22}
    html = render_template('index.html', data = data)
    return html


@main_blue.route('/')
def protection_search() :
    data = {'confirmator' : 900, 'heal' : 22, 'die':8}
    html = render_template('protection_search.html', data = data)
    return html

@main_blue.route('/robots.txt')
def robots() :
    
    html = render_template('robots.txt')
    return html

@main_blue.route('/sitemap.xml')
def sitemap() :
    
    html = render_template('sitemap.xml')
    return html