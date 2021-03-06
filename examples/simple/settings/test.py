# Use in `tox`.

from .base import *

INSTALLED_APPS = list(INSTALLED_APPS)

from nine import versions


if versions.DJANGO_1_5:

    try:
        INSTALLED_APPS.append(
            'south') if 'south' not in INSTALLED_APPS else None
    except Exception as e:
        pass

elif versions.DJANGO_1_6:

    try:
        INSTALLED_APPS.append(
            'south') if 'south' not in INSTALLED_APPS else None
    except Exception as e:
        pass


elif versions.DJANGO_1_7:

    try:
        INSTALLED_APPS.remove('south') if 'south' in INSTALLED_APPS else None
        INSTALLED_APPS.remove(
            'tinymce') if 'tinymce' in INSTALLED_APPS else None
    except Exception as e:
        pass

elif versions.DJANGO_1_8:

    try:
        INSTALLED_APPS.remove('south') if 'south' in INSTALLED_APPS else None
        INSTALLED_APPS.remove(
            'tinymce') if 'tinymce' in INSTALLED_APPS else None
    except Exception as e:
        pass

    try:
        INSTALLED_APPS.remove('admin_tools') \
            if 'admin_tools' in INSTALLED_APPS else None
        INSTALLED_APPS.remove('admin_tools.menu') \
            if 'admin_tools.menu' in INSTALLED_APPS else None
        INSTALLED_APPS.remove('admin_tools.dashboard') \
            if 'admin_tools.dashboard' in INSTALLED_APPS else None
    except Exception as e:
        pass

elif versions.DJANGO_1_9:

    try:
        INSTALLED_APPS.remove('south') if 'south' in INSTALLED_APPS else None
        INSTALLED_APPS.remove(
            'tinymce') if 'tinymce' in INSTALLED_APPS else None
        INSTALLED_APPS.remove(
            'localeurl') if 'localeurl' in INSTALLED_APPS else None
    except Exception as e:
        pass

    try:
        INSTALLED_APPS.remove('admin_tools') \
            if 'admin_tools' in INSTALLED_APPS else None
        INSTALLED_APPS.remove('admin_tools.menu') \
            if 'admin_tools.menu' in INSTALLED_APPS else None
        INSTALLED_APPS.remove('admin_tools.dashboard') \
            if 'admin_tools.dashboard' in INSTALLED_APPS else None
    except Exception as e:
        pass

elif versions.DJANGO_1_10:

    try:
        INSTALLED_APPS.remove('south') if 'south' in INSTALLED_APPS else None
        INSTALLED_APPS.remove(
            'tinymce') if 'tinymce' in INSTALLED_APPS else None
        INSTALLED_APPS.remove(
            'localeurl') if 'localeurl' in INSTALLED_APPS else None
    except Exception as e:
        pass

    try:
        INSTALLED_APPS.remove('admin_tools') \
            if 'admin_tools' in INSTALLED_APPS else None
        INSTALLED_APPS.remove('admin_tools.menu') \
            if 'admin_tools.menu' in INSTALLED_APPS else None
        INSTALLED_APPS.remove('admin_tools.dashboard') \
            if 'admin_tools.dashboard' in INSTALLED_APPS else None
    except Exception as e:
        pass
