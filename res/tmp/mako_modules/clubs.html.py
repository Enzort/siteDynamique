# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1685020057.9778378
_enable_loop = True
_template_filename = 'res/templates/clubs.html'
_template_uri = 'clubs.html'
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
        mesClu = context.get('mesClu', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<h2>Affichage des clubs :</h2>\r\n\r\n<div class="Affichage">\r\n    <table>\r\n        <tr>\r\n            <th>Numéro du club</th>\r\n            <th>Nom du club</th>\r\n            <th>Ville</th>\r\n            <th>Budget</th>\r\n            <th>Stade</th>\r\n            <th>Date de création</th>\r\n        </tr>\r\n')
        for club in mesClu:
            __M_writer('        <tr>\r\n            <td style="padding: 10px;">')
            __M_writer(str(club[0]))
            __M_writer('</td>\r\n            <td style="padding: 10px;">')
            __M_writer(str(club[1]))
            __M_writer('</td>\r\n            <td style="padding: 10px;">')
            __M_writer(str(club[2]))
            __M_writer('</td>\r\n            <td style="padding: 10px;">')
            __M_writer(str(club[3]))
            __M_writer('</td>\r\n            <td style="padding: 10px;">')
            __M_writer(str(club[4]))
            __M_writer('</td>\r\n            <td style="padding: 10px;">')
            __M_writer(str(club[5]))
            __M_writer('</td>\r\n        </tr>\r\n')
        __M_writer('    </table>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "res/templates/clubs.html", "uri": "clubs.html", "source_encoding": "utf-8", "line_map": {"27": 0, "33": 1, "34": 15, "35": 16, "36": 17, "37": 17, "38": 18, "39": 18, "40": 19, "41": 19, "42": 20, "43": 20, "44": 21, "45": 21, "46": 22, "47": 22, "48": 25, "54": 48}}
__M_END_METADATA
"""
