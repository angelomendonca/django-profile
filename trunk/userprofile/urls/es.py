from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib.auth import views
from userprofile.views import *
from django.conf import settings

urlpatterns = patterns('',
    # Private profile
    url(r'^perfil/$', overview, name='profile_overview'),

    url(r'^perfil/de/(?P<username>.+)/$', public, name='profile_public'),

    url(r'^perfil/editar/ubicacion/$', location, name='profile_edit_location'),

    url(r'^perfil/editar/ubicacion/listo/$', direct_to_template,
        {'extra_context': {'section': 'location'},
        'template': 'userprofile/profile/location_done.html'},
        name='profile_edit_location_done'),

    url(r'^perfil/editar/personal/$', personal, name='profile_edit_personal'),

    url(r'^perfil/editar/personal/listo/$', direct_to_template,
        {'extra_context': {'section': 'personal'},
        'template': 'userprofile/profile/personal_done.html'},
        name='profile_edit_personal_done'),

    url(r'^perfil/edit/publico/$', makepublic, name='profile_edit_public'),

    url(r'^perfil/edit/publico/listo/$', direct_to_template,
        {'extra_context': {'section': 'public'},
        'template': 'userprofile/profile/makepublic_done.html'},
        name='profile_edit_public_done'),

    url(r'^perfil/eliminar/$', delete, name='profile_delete'),

    url(r'^perfil/eliminar/listo/$', direct_to_template,
        {'extra_context': {'section': 'delete'},
        'template': 'userprofile/profile/delete_done.html'},
        name='profile_delete_done'),

    url(r'^perfil/obtener_infopais/(?P<lat>[0-9\.\-]+)/(?P<lng>[0-9\.\-]+)/$',
        fetch_geodata,
        name='profile_geocountry_info'),

    # Avatars
    url(r'^perfil/editar/avatar/eliminar/$', avatardelete, name='profile_avatar_delete'),

    url(r'^perfil/editar/avatar/$', avatarchoose, name='profile_edit_avatar'),

    url(r'^perfil/editar/avatar/buscar/$', searchimages, name='profile_avatar_search'),

    url(r'^perfil/editar/avatar/recortar/$', avatarcrop, name='profile_avatar_crop'),

    url(r'^perfil/editar/avatar/recortar/listo/$', direct_to_template,
        { 'extra_context': {'section': 'avatar'},
        'template': 'userprofile/avatar/done.html'},
        name='profile_avatar_crop_done'),

    # Account utilities
    url(r'^password/reestablecer/$', reset_password, name='password_reset'),

    url(r'^password/reestablecer/listo/$', direct_to_template,
        {'template': 'userprofile/account/password_reset_done.html'},
        name='password_reset_done'),

    url(r'^email/validar/$', email_validation, name='email_validation'),

    url(r'^email/validar/procesado/$', direct_to_template,
        {'extra_context': {'section': 'overview'},
         'template': 'userprofile/account/email_validation_processed.html'},
         name='email_validation_processed'),

    url(r'^email/validar/(?P<key>.{70})/$', email_validation_process,
        name='email_validation_process'),

    url(r'^email/validar/reestablecer/$', email_validation_reset,
        name='email_validation_reset'),

    url(r'^email/validar/reestablecer/(?P<action>listo|fallo)/$',
        direct_to_template, {'extra_context': {'section': 'overview'},
        'template' : 'userprofile/account/email_validation_reset_done.html'},
        name='email_validation_reset_done'),

    url(r'^password/cambiar/$', change_password_authenticated, 
        name='password_change'),

    url(r'^password/cambiar/listo/$', direct_to_template,
        {'extra_context': {'section': 'overview'},
         'template': 'userprofile/account/password_change_done.html'},
        name='password_change_done'),

    url(r'^password/cambiar/(?P<key>.{70})/$', change_password_with_key,
        name='password_change_with_key'),

    url(r'^entrar/$', views.login,
        {'template_name': 'userprofile/account/login.html'},
        name='login'),

    url(r'^salir/$', logout,
        {'template': 'userprofile/account/logout.html'},
        name='logout'),


    # Registration

    url(r'^registro/$', register, name='signup'),

    url(r'^registro/validar/$', direct_to_template,
        {'template' : 'userprofile/account/validate.html'},
        name='signup_validate'),

    url(r'^registro/completo/$', direct_to_template,
        {'template': 'userprofile/account/registration_done.html'},
        name='signup_complete'),
)