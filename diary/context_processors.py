from diary.settings import *


def customisation(request):
    request.session['theme'] =  request.COOKIES.get('theme','cyborg')
    custom = {
            'THEME' : request.session.get('theme','cyborg'),
            'INSTALLED_THEMES' : INSTALLED_THEMES,
            'APP_NAME' : APP_NAME,
            }

    return custom
