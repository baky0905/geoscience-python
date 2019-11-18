# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
sys.setrecursionlimit(1500)

# -- Project information -----------------------------------------------------

project = 'Geoscience with Python'
copyright = 'Kristijan Bakaric'
author = 'Kristijan Bakaric'

# The short X.Y version
version = '1'
# The full version, including alpha/beta/rc tags
release = '2019'

nbsphinx_allow_errors = True

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'nbsphinx',
    'sphinx.ext.mathjax',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']
#source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.ipynb_checkpoints',
                    "extra.ipynb", "notes.ipynb", "sisallys.ipynb",
                    "testing.ipynb", "todo.ipynb"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'
#html_theme = 'classic'
import sphinx_press_theme
import sphinx_rtd_theme

html_theme = "press" #'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'Geoscience with Python'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'Geoscience with Python.tex', 'Geoscience with Python',
     'Kristijan Bakaric', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'Geoscience with Python', 'Geoscience with Python',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Geoscience with Python', 'Geoscience with Python',
     author, 'Geoscience with Python', 'One line description of project.',
     'Miscellaneous'),
]


# -- Extension configuration -------------------------------------------------


# This is processed by Jinja2 and inserted before each notebook
# nbsphinx_prolog = r"""
# {% set docname = env.doc2path(env.docname, base='source') %}
# {% set docname2 = env.doc2path(env.docname, base='') %}

# .. only:: html

#     .. role:: raw-html(raw)
#         :format: html

#     .. nbinfo::

#         This page was generated from `{{ docname2 }}`__.
#         :raw-html:`<br/><a href='https://colab.research.google.com/github/saskeli/data-analysis-with-python-summer-2019/blob/master/{{ docname2 }}'><img align='left' src='https://colab.research.google.com/assets/colab-badge.svg' alt='Open in Colab' title='Open and Execute in Google Colaboratory' /></a>`
#         :raw-html:`<br/>`

#     __ https://github.com/saskeli/data-analysis-with-python-summer-2019/blob/master/{{ docname2 }}

# """

#        :raw-html:`<br/><a href="https://mybinder.org/v2/gh/geo-python/{{ env.config.release }}/master?urlpath=lab/tree/{{ docname }}"><img alt="Binder badge" src="https://img.shields.io/badge/launch-full%20binder-red.svg" style="vertical-align:text-bottom"></a>`
#        :raw-html:`<a href="https://mybinder.org/v2/gh/geo-python/notebooks/master?urlpath=lab/tree/{{ docname2 }}"><img alt="Binder badge" src="https://img.shields.io/badge/launch-student%20binder-red.svg" style="vertical-align:text-bottom"></a>`
#        :raw-html:`<a href="https://notebooks.csc.fi/#/blueprint/d71cd2d26d924f48820dc22b67a87d8e"><img alt="CSC badge" src="https://img.shields.io/badge/launch-CSC%20notebook-blue.svg" style="vertical-align:text-bottom"></a>`