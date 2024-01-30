# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1685964739.6853437
_enable_loop = True
_template_filename = 'res/templates/transferts.html'
_template_uri = 'transferts.html'
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
        mesTr = context.get('mesTr', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<h2>Affichage des transferts :</h2>\r\n\r\n<div class="Affichage">\r\n    <table>\r\n        <tr>\r\n            <th>Nom du Joueur</th>\r\n            <th>Prénom du Joueur</th>\r\n            <th>Numéro du Joueur</th>\r\n            <th>Montant du transfert</th>\r\n            <th>Acheteur</th>\r\n            <th>Date</th>\r\n            \r\n        </tr>\r\n')
        for transfert in mesTr:
            __M_writer('        <tr>\r\n            <td style="padding: 10px;">')
            __M_writer(str(transfert[0]))
            __M_writer('</td>\r\n            <td style="padding: 10px;">')
            __M_writer(str(transfert[1]))
            __M_writer('</td>\r\n            <td style="padding: 10px;">')
            __M_writer(str(transfert[2]))
            __M_writer('</td>\r\n            <td style="padding: 10px;">')
            __M_writer(str(transfert[3]))
            __M_writer('</td>\r\n            <td style="padding: 10px;">')
            __M_writer(str(transfert[4]))
            __M_writer('</td>\r\n            <td style="padding: 10px;">')
            __M_writer(str(transfert[5]))
            __M_writer('</td>\r\n        </tr>\r\n')
        __M_writer('    </table>\r\n</div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "res/templates/transferts.html", "uri": "transferts.html", "source_encoding": "utf-8", "line_map": {"27": 0, "33": 1, "34": 16, "35": 17, "36": 18, "37": 18, "38": 19, "39": 19, "40": 20, "41": 20, "42": 21, "43": 21, "44": 22, "45": 22, "46": 23, "47": 23, "48": 26, "54": 48}}
__M_END_METADATA
"""
