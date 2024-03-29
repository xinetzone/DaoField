# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
import sys
from pathlib import Path

ROOT = Path('__file__').resolve().parents[1]
sys.path.extend([str(ROOT/'src')])
import dao_field

if sys.platform == 'win32':
    import asyncio
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

project = 'dao_field'
copyright = '2022, xinetzone'
author = 'xinetzone'

# The full version, including alpha/beta/rc tags
release = dao_field.__version__


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "xyzstyle",
    'myst_nb',
    'sphinx.ext.intersphinx',
    'sphinx_copybutton',
    "sphinx_comments",
    'sphinx.ext.autosummary',
    "sphinx.ext.viewcode",
    "sphinxcontrib.bibtex",
    'sphinx.ext.autosectionlabel',
    "sphinx.ext.graphviz",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    # "sphinx_thebe",
    "sphinx_sitemap",
    "sphinx_design",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'zh_CN'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'xyzstyle'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = [
    'custom.css',
]

# MyST-NB 设置
# 如果你希望stderr和stdout中的每个输出都被合并成一个流，请使用以下配置。
# 避免将 jupter 执行报错的信息输出到 cmd
nb_merge_streams = True
nb_execution_allow_errors = True
nb_execution_mode = 'off'

nb_mime_priority_overrides = [
    ('html', 'text/plain', 0),  # 最高级别
    ('latex', 'image/jpeg', None),  # 禁用
    # ('*', 'customtype', 20)
]

# -- 国际化输出 ----------------------------------------------------------------
gettext_compact = False
locale_dirs = ['locales/']

# Napoleon 设置
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = True
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = True
napoleon_use_ivar = True
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = True
napoleon_type_aliases = None
napoleon_attr_annotations = True

html_logo = '_static/images/logo.jpg'
# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = '_static/images/favicon.jpg'

html_last_updated_fmt = '%Y-%m-%d, %H:%M:%S'



extlinks = {
    # 'duref': ('https://docutils.sourceforge.io/docs/ref/rst/'
    #           'restructuredtext.html#%s', ''),
    # 'durole': ('https://docutils.sourceforge.io/docs/ref/rst/'
    #            'roles.html#%s', ''),
    # 'dudir': ('https://docutils.sourceforge.io/docs/ref/rst/'
    #           'directives.html#%s', ''),
    'py-doc': ('https://daobook.github.io/cpython/%s', ''),
    'daobook': ('https://daobook.github.io/%s', ''),
}

intersphinx_mapping = {
    'python': ('https://daobook.github.io/cpython/', None),
    'tvm': ('https://daobook.github.io/tvm/', None),
    "mxnet": ("https://mxnet.incubator.apache.org/versions/1.9.0/api/python/docs", None)
}

# ``pydata-sphinx-theme`` 配置
# Define the json_url for our version switcher.
json_url = 'https://xinetzone.github.io/dao_field/_static/switcher.json'

version = release

switcher_version = f'v{version}'
if "dev" in version:
    switcher_version = "dev"
elif "rc" in version:
    switcher_version = version.split("rc")[0] + " (rc)"
html_baseurl = "https://xinetzone.github.io/dao_field"
autosummary_generate = True
html_theme_options = {
    "switcher": {
        "json_url": json_url,
        "version_match": switcher_version
    },
    "github_url": "https://github.com/xinetzone/dao_field",
    "use_edit_page_button": True,
    "show_nav_level": 0,
    "show_toc_level": 0,
    "navigation_with_keys": True,
    "collapse_navigation": False,
    "navbar_align": "content", # "right", "left", "content"
    "navbar_start": "navbar-logo.html",
    "navbar_center": "navbar-nav.html",
    "navbar_end": ["theme-switcher", "version-switcher", "navbar-icon-links"],
    # "page_sidebar_items": [], # 删除右侧边栏
    "footer_start": ["copyright", "sphinx-version"],
    "footer_end": ["last-updated", ],
    # 图标可以参考 https://fontawesome.com/icons
    "icon_links": [
        # {
        #     "name": "GitHub",
        #     "url": "https://github.com/xinetzone/tvm-book",
        #     "icon": "fa-brands fa-square-github",
        #     "type": "fontawesome",
        # },
        {
            "name": "知乎",
            "url": "https://www.zhihu.com/people/xinetzone",
            "icon": "fa-brands fa-zhihu",
            "type": "fontawesome",
        },
        {
            "name": "简书",
            "url": "https://www.jianshu.com/u/4302480a3e8e",
            "icon": "fa-solid fa-book",
            "type": "fontawesome",
        },
        {
            "name": "B站",
            "url": "https://space.bilibili.com/252192181",
            "icon": "fa-brands fa-bilibili",
            "type": "fontawesome",
        },
        {
            "name": "博客园",
            "url": "https://www.cnblogs.com/q735613050/",
            "icon": "https://xinetzone.github.io/xinetzone/media/xinetzone.jpg",
            "type": "url",
        },
        {
            "name": "领英",
            "url": "https://www.linkedin.com/in/xinet",
            "icon": "fa-brands fa-linkedin",
            "type": "fontawesome",
        },
        # {
        #     "name": "GitLab",
        #     "url": "https://gitlab.com/<your-org>/<your-repo>",
        #     "icon": "fa-brands fa-square-gitlab",
        #     "type": "fontawesome",
        # },
        # {
        #     "name": "Twitter",
        #     "url": "https://twitter.com/<your-handle>",
        #     "icon": "fa-brands fa-square-twitter",
        #     # The default for `type` is `fontawesome` so it is not actually required in any of the above examples as it is shown here
        # },
        # {
        #     "name": "Mastodon",
        #     "url": "https://<your-host>@<your-handle>",
        #     "icon": "fa-brands fa-mastodon",
        # },
    ],
    # "use_download_button": True,
    # "toc_title": "导航",
    # "single_page": True,
}

html_sidebars = {
    "contribute/index": [
        "search-field",
        "sidebar-nav-bs",
        "custom-template",
    ],  # This ensures we test for custom sidebars
    "demo/no-sidebar": [],  # Test what page looks like with no sidebar items
}

html_context = {
    "github_user": "xinetzone",
    "github_repo": "dao_field",
    "github_version": "main",
    "doc_path": "doc",
}

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_image",
]


bibtex_bibfiles = ["note.bib"]
# To test that style looks good with common bibtex config
bibtex_reference_style = "author_year"
graphviz_output_format = 'svg'

comments_config = {
    "hypothesis": True,
    "dokieli": False,
    "utterances": {
        "repo": "xinetzone/dao_field",
        "optional": "config",
    }
}
