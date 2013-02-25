import sys, os

source_suffix = '.rst'
master_doc = 'index'
project = u'sphinx 1.2.0 preview'
copyright = u'2013, Takayuki SHIMIZUKAWA'
version = release = '1.2.0'
language = 'ja'
exclude_patterns = ['_build']
pygments_style = 'sphinx'
html_theme = 's6'
extensions = ['sphinxjp.themecore']
html_logo = 'sphinx-logo.png'
html_static_path = ['_static']

def setup(app):
    app.add_stylesheet('custom.css')

