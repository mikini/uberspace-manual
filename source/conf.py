#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Uberspace 7 manual documentation build configuration file, created by
# sphinx-quickstart on Tue Feb 13 12:19:29 2018.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import sphinx_rtd_theme

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = []

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Uberspace 7 manual'
copyright = '2018, uberspace.de'
author = 'uberspace.de'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '7'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

def _read_changelog_files():
    import os
    import os.path

    entries = []

    changelog_dir = os.path.join(
        os.path.dirname(__file__),
        'changelog',
    )

    for name in os.listdir(changelog_dir):
        path = os.path.join(changelog_dir, name)

        if not name.endswith('.rst'):
            continue

        base, _ = os.path.splitext(name)
        date, sep, version = base.partition('_')

        if not sep:
            print("invalid filename: " + path)

        entries.append({
            'date': date,
            'version': version,
            'text': open(path).read().decode('utf-8'),
        })

    entries.sort(key=lambda e: e['date'], reverse=True)
    return entries


changelog_entries = _read_changelog_files()

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
  'display_version': False,
  'navigation_depth': 2,
  'collapse_navigation': True
}
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_last_updated_fmt = '%b %d, %Y'
html_context = {
  'css_files': ['_static/css/custom.css'],
  'changelog_entries': changelog_entries,
  'newest_changelog_entry': changelog_entries[0],
}
html_show_copyright = False
html_favicon = '_static/favicon.ico'


release = changelog_entries[-1]['version']


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
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
    ]
}


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'Uberspace7manualdoc'


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'uberspace7manual', 'Uberspace 7 manual Documentation',
     [author], 1)
]

def rstjinja(app, docname, source):
    """
    Render our pages as jinja templates.
    """
    source[0] = app.builder.templates.render_string(
        source[0], app.config.html_context
    )


def setup(app):
    app.connect("source-read", rstjinja)
