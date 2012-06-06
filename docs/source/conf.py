# Sphinx conf file
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../../')))

extensions       = ['sphinx.ext.autodoc']
templates_path   = ['_templates']
source_suffix    = '.rst'
master_doc       = 'index'
project          = 'sagverk'
copyright        = 'Copyright (c) 2012 H359'
version          = '0.1.0'
release          = '0.1.0'
exclude_trees    = ['_build']
pygments_style   = 'sphinx'
html_theme       = 'default'
html_static_path = ['_static']
htmlhelp_basename = 'sagverkdoc'
latex_documents = [
    ('index', 'sagverk.text', 'Sagverk documentation', 'Konstantin Kirillov', 'manual'),
]