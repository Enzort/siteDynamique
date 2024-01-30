# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1685960135.2170153
_enable_loop = True
_template_filename = 'res/templates/modiJou.html'
_template_uri = 'modiJou.html'
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
        __M_writer('\n\n<h2>Modifier un joueur</h2>\n\n\n<div class="container">\n    <div class="ajoutT1">\n        <form action="ModifierJoueur" method="POST">\n            \n            ')
        __M_writer(str(message))
        __M_writer('\n\n        <br>    \n        <br>\n        <br>    \n        <br>\n            <label for="num">Numéro du joueur :</label>\n        <br>\n        <br>\n            <input type="number" id="num" placeholder="" name="num" required>\n        <br>\n        <br>\n\n            <label for="nomJoueurs">Nom :</label>\n        <br>    \n        <br>\n            <input type="text" id="nom" placeholder="Nom du Joueur" name="nom" required>\n        <br>\n        <br>\n            <label for="prenomJoueurs">Prénom :</label>\n        <br>\n        <br>\n            <input type="text" id="prenom" placeholder="Prénom du joueur" name="prenom" required>\n        <br>\n        <br>\n            <label for="dateNaiss">Date de naissance :</label>\n        <br>\n        <br>    \n            <input type="date" id="naiss" placeholder="Format AAAA-MM-JJ" name="naiss" required>\n        <br>\n        <br>\n            <label for="nationalite">Nationalité :</label>\n        <br>\n        <br>    \n            <input type="text" id="nationalite" placeholder="Nationalité du joueur" name="nationalite" required>\n        <br>\n        <br>\n            <label for="poste">Poste :</label>\n        <br>\n        <br>\n            <label for="poste">QB</label>\n            <input type="radio" id="poste" name="poste" value="QB" required>\n\n            <label for="poste">WR</label>\n            <input type="radio" id="poste" name="poste" value="WR" required>\n\n            <label for="poste">OL</label>\n            <input type="radio" id="poste" name="poste" value="OL" required>\n        \n            <label for="poste">DL</label>\n            <input type="radio" id="poste" name="poste" value="DL" required>\n\n            <label for="poste">RB</label>\n            <input type="radio" id="poste" name="poste" value="RB" required>\n\n            <label for="poste">FB</label>\n            <input type="radio" id="poste" name="poste" value="FB" required>\n\n            <label for="poste">TE</label>\n            <input type="radio" id="poste" name="poste" value="TE" required>\n\n            <label for="poste">LB</label>\n            <input type="radio" id="poste" name="poste" value="LB" required>\n\n            <label for="poste">CB</label>\n            <input type="radio" id="poste" name="poste" value="CB" required>\n\n            <label for="poste">S</label>\n            <input type="radio" id="poste" name="poste" value="S" required>\n\n            <label for="poste">K</label>\n            <input type="radio" id="poste" name="poste" value="K" required>\n\n            <label for="poste">P</label>\n            <input type="radio" id="poste" name="poste" value="P" required>\n\n            <label for="poste">KR</label>\n            <input type="radio" id="poste" name="poste" value="KR" required>\n\n            <label for="poste">PR</label>\n            <input type="radio" id="poste" name="poste" value="PR" required>\n\n            <label for="poste">SP</label>\n            <input type="radio" id="poste" name="poste" value="SP" required>\n        <br>\n        <br>\n            <label for="nClub">Numéro du club :</label>\n        <br>\n        <br>\n            <input type="number" id="club" placeholder="" name="club" required>\n        <br>\n        <br>\n            <label for="salaire">Salaire annuel :</label>\n        <br>\n        <br>    \n            <input type="number" id="salaire" placeholder="" name="salaire" required>\n        <br>\n        <br>\n            <label for="taille">Taille :</label>\n        <br>\n        <br>\n            <input type="number" id="taille" placeholder="En centimètres" name="taille" step="any" inputmode="decimal" required>\n        <br>\n        <br>\n            <label for="poids">Poids :</label>\n        <br>\n        <br>\n            <input type="number" id="poids" placeholder="En kilogrammes" name="poids" step="any" inputmode="decimal" required>\n        <br>\n        <br>\n            <label for="sprint40y">Sprint sur 40 yards :</label>\n        <br>\n        <br>\n            <input type="number" id="sprint" placeholder="En secondes" name="sprint" step="any" inputmode="decimal" required>\n        <br>\n        <br>\n            <input type="submit" value="Insérer" class="btn-insérer">\n    </form>\n    </div>\n</div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "res/templates/modiJou.html", "uri": "modiJou.html", "source_encoding": "utf-8", "line_map": {"27": 0, "33": 1, "34": 10, "35": 10, "41": 35}}
__M_END_METADATA
"""
