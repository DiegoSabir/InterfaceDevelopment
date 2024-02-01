# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys

sys.path.insert(0, os.path.abspath('/'))

project = 'a18diegorg2324'
copyright = '2024, Diego'
author = 'Diego'
release = 'v1.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc'
              'sphinx.ext.intersphinx'
              'sphinx.ext.ifconfig'
              'sphinx.ext.viewcode'
              'sphinx.ext.githubpages']

templates_path = ['_templates']
exclude_patterns = []

language = 'es'
source_patterns = '.rst'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'classic'
#html_static_path = ['_static']
