# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1685360812.4576447
_enable_loop = True
_template_filename = 'res/templates/suppJoueur.html'
_template_uri = 'suppJoueur.html'
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
        message = context.get('message', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<h2>Supprimer un joueur :</h2>\r\n\r\n\r\n<div class="container1">\r\n    <div class="suppJou">\r\n        <form action="suppressById" method="POST">\r\n\r\n            \r\n            ')
        __M_writer(str(message))
        __M_writer('\r\n\r\n        <br>    \r\n        <br>\r\n        <br>    \r\n        <br>\r\n            <label for="nJoueur">Numéro du joueur :</label>\r\n        <br>\r\n        <br>\r\n            <input type="number" id="nJoueur" placeholder="" name="nJoueur" required>\r\n        <br>\r\n        <br>\r\n            <input type="submit" value="Supprimer" class="btn-supp">\r\n        </form>\r\n    </div>\r\n</div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "res/templates/suppJoueur.html", "uri": "suppJoueur.html", "source_encoding": "utf-8", "line_map": {"27": 0, "33": 1, "34": 11, "35": 11, "41": 35}}
__M_END_METADATA
"""
