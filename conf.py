
import sys
import os
sys.path.insert(0, os.path.abspath('.'))
sys.path.append('dsa_algorithms')

project = 'Algorithms'
copyright = '2024, Viathorr'
author = 'Viathorr'
release = '1.0.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.githubpages',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
    'sphinx.ext.ifconfig',
    'sphinx.ext.napoleon'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'tests/*']


html_theme = 'scrolls'
html_static_path = ['_static']
