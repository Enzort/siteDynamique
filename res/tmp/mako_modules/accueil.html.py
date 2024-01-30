# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1684962691.2193449
_enable_loop = True
_template_filename = 'res/templates/accueil.html'
_template_uri = 'accueil.html'
_source_encoding = 'utf-8'
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'template.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<div class="presentation">\r\n    <img class="catch" src="../media/catch.jpg" alt="">\r\n    <p class="text">\r\n        Le football américain est un sport collectif opposant deux équipes de onze joueurs qui alternent entre la défense et l\'attaque. Le but du jeu est de marquer des points en amenant le ballon dans la zone des buts adverse. Pour conserver la possession, l\'équipe attaquante doit parcourir au moins 10 yards en 4 tentatives (appelées « down »). Dans le même temps, l\'équipe en défense doit empêcher l\'attaque d\'atteindre cet objectif, dans le but de reprendre la possession du ballon. Si l\'équipe attaquante valide 10 yards ou plus lors de sa possession, elle bénéficie de quatre nouvelles tentatives pour continuer à gagner du terrain. Sinon, la possession du ballon change de camp et les rôles, défense/attaque, s\'inversent.\r\n        Les points peuvent être marqués de différentes façons : en franchissant la ligne de but avec le ballon, en lançant le ballon à un autre joueur situé de l\'autre côté de la ligne de but, en plaquant le porteur du ballon de l\'équipe adverse dans sa propre zone d\'en-but (safety) ou en tirant au pied le ballon entre les poteaux du but adverse. Le vainqueur est l\'équipe ayant marqué le plus de points à la fin du match.\r\n        Aux États-Unis et au Canada (y compris au Québec), le football américain (ainsi que son pendant canadien) est simplement appelé football. Par contre, le sport dénommé football au niveau mondial y est appelé soccer. \r\n    </p>\r\n</div>\r\n\r\n\r\n\r\n<div class="classement">\r\n    <p class="texte">\r\n        Classements :\r\n    </p>\r\n    <img class="classA" src="../media/AFC.png" alt="Classement AFC">\r\n    <img class="classN" src="../media/NFC.png" alt="Classement NFC">\r\n</div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "res/templates/accueil.html", "uri": "accueil.html", "source_encoding": "utf-8", "line_map": {"27": 0, "32": 1, "38": 32}}
__M_END_METADATA
"""
