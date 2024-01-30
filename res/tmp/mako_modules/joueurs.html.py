# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1685020476.117461
_enable_loop = True
_template_filename = 'res/templates/joueurs.html'
_template_uri = 'joueurs.html'
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
        mesJou = context.get('mesJou', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<h2>Affichage des joueurs :</h2>\r\n<div class="Affichage">\r\n    <table>\r\n        <tr>\r\n            <th>Numéro du Joueur</th>\r\n            <th>Nom</th>\r\n            <th>Prénom</th>\r\n            <th>Date de naissance</th>\r\n            <th>Nationalité</th>\r\n            <th>Poste</th>\r\n            <th>Numéro de club</th>\r\n            <th>Salaire annuel</th>\r\n            <th>Taille en cm</th>\r\n            <th>Poids en kg</th>\r\n            <th>Sprint sur 40 yards en s</th>\r\n        </tr>\r\n')
        for joueur in mesJou:
            __M_writer('        <tr>\r\n            <td style="padding: 10px;">')
            __M_writer(str(joueur[0]))
            __M_writer('</td>\r\n            <td style="padding: 10px;">')
            __M_writer(str(joueur[1]))
            __M_writer('</td>\r\n            <td style="padding: 10px;">')
            __M_writer(str(joueur[2]))
            __M_writer('</td>\r\n            <td style="padding: 10px;">')
            __M_writer(str(joueur[3]))
            __M_writer('</td>\r\n            <td style="padding: 10px;">')
            __M_writer(str(joueur[4]))
            __M_writer('</td>\r\n            <td style="padding: 10px;">')
            __M_writer(str(joueur[5]))
            __M_writer('</td>\r\n            <td style="padding: 10px;">')
            __M_writer(str(joueur[6]))
            __M_writer('</td>\r\n            <td style="padding: 10px;">')
            __M_writer(str(joueur[7]))
            __M_writer('</td>\r\n            <td style="padding: 10px;">')
            __M_writer(str(joueur[8]))
            __M_writer('</td>\r\n            <td style="padding: 10px;">')
            __M_writer(str(joueur[9]))
            __M_writer('</td>\r\n            <td style="padding: 10px;">')
            __M_writer(str(joueur[10]))
            __M_writer('</td>\r\n        </tr>\r\n')
        __M_writer('    </table>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "res/templates/joueurs.html", "uri": "joueurs.html", "source_encoding": "utf-8", "line_map": {"27": 0, "33": 1, "34": 19, "35": 20, "36": 21, "37": 21, "38": 22, "39": 22, "40": 23, "41": 23, "42": 24, "43": 24, "44": 25, "45": 25, "46": 26, "47": 26, "48": 27, "49": 27, "50": 28, "51": 28, "52": 29, "53": 29, "54": 30, "55": 30, "56": 31, "57": 31, "58": 34, "64": 58}}
__M_END_METADATA
"""
