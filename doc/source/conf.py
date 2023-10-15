import os
import sys
from datetime import date

sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, '../..')
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Demon_Connect'
copyright = f"{date.today().year}, Tanjiro"
author = 'Anupam Maurya'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [ 
    "sphinx.ext.autodoc",
    "sphinx_copybutton",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinxext.opengraph",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosummary",
    "sphinx_togglebutton",
    "sphinx.ext.autosectionlabel"]

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []
pygments_style = "friendly"
html_theme = "sphinx_book_theme"
suppress_warnings = ["image.not_readable"]
html_static_path = ['_static']
html_favicon = "favicon.ico"



# sphinx.ext.autodoc
autodoc_member_order = "bysource"
# autodoc_typehints = "none"  # show type hints in doc signature
# autodoc_typehints = "description"  # show type hints in doc body instead of signature

# sphinx.ext.napoleon
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_use_ivar = True

# sphinx-copybutton
copybutton_prompt_text = r">>> |\.\.\. |> |\$ |\# | In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
copybutton_prompt_is_regexp = True
copybutton_remove_prompts = True

# sphinx_book_theme
html_theme_options = {
    "use_sidenotes": True,
    "repository_url": "https://github.com/anupammaurya6767/Demon_connect",
    "repository_branch": "main",
    "path_to_docs": "docs/source",
    "use_edit_page_button": True,
    "use_repository_button": True,
    "use_issues_button": True,
    "use_source_button": True,
    "logo": {
        "text": "Demon_Connect",
        "link": "https://demon-connect.readthedocs.io/",
        "alt_text": "tanjiro-sama",
        "image_light": "main.png",
        "image_dark": "main.png",
    },
    "icon_links_label": "Quick Links",
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/anupammaurya6767/Demon_connect",
            "icon": "fab fa-github",
        },
        {
            "name": "PyPI",
            "url": "https://github.com/anupammaurya6767/Demon_connect",
            "icon": "fab fa-python",
        },
        {
            "name": "Updates",
            "url": "https://chat.whatsapp.com/FVeZfhzV68iEPAwRTpMdLh",
            "icon": "fa-solid fa-bullhorn",
        },
        {
            "name": "Chat",
            "url": "https://chat.whatsapp.com/FGV7ef4d9tNGtfN8HDvbim",
            "icon": "fa-solid fa-comment-dots",
        },
        {
            "name": "Issues",
            "url": "https://github.com/anupammaurya6767/Demon_connect/issues",
            "icon": "fas fa-bug",
        }
    ],
    "use_download_button": True,
}

# sphinx.ext.intersphinx
intersphinx_mapping = {"python": ("https://docs.python.org/3", None)}

# sphinxext.opengraph
ogp_site_url = "https://demon-connect.readthedocs.io/"
ogp_site_name = "pywa documentation"
ogp_image = "https://demon-connect.readthedocs.io/en/latest/_static/main.png"
ogp_image_alt = "tanjiro-sama"
ogp_description_length = 300
ogp_type = "website"
ogp_custom_meta_tags = [
    '<meta property="og:description" content="Demon Connect • Whatsapp API" /> '
]


# sphinx.ext.todo
todo_include_todos = True
