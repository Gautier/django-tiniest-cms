Django tiniest cms
==================

![logo](/gecko.png)

django-tiniest-cms is the simplest CMS I could come up with. There is no
workflow, no WYSIWYG, no content hiearchy, no fancy admin and no security.

Installation
------------

1. The recommended way to install django-tiniest-cms package is with pip.

    $ pip install django-tiniest-cms

2. Then add 'django-tiniest-cms' to `INSTALLED_APPS`.

Usage
-----

Assuming this would be the frontpage template of a website :

    {% load tiniest_cms %}<html>
    <head>
        <title>{% content "website/frontpage/title" %}NO TITLE{% endcontent %}</title>
    </head>
    <body>
        {% content "website/frontpage/main_content"%}

        This is the website of ACME corporation

        {% endcontent %}
    </body>
    </html>

Then in the administration you can add the content snippet matching the name
given to the `content` tags. The content will be rendered as markdown instead
of the default given to the `content` tags.
