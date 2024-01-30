# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1685360665.5814137
_enable_loop = True
_template_filename = 'res/templates/ajoutJoueur.html'
_template_uri = 'ajoutJoueur.html'
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
        __M_writer('\r\n\r\n<h2>Ajouter un joueur</h2>\r\n\r\n\r\n<div class="container">\r\n    <div class="ajoutJ">\r\n        <form action="insertJoueur" method="POST">\r\n            \r\n            ')
        __M_writer(str(message))
        __M_writer('\r\n\r\n        <br>    \r\n        <br>\r\n        <br>    \r\n        <br>\r\n\r\n            <label for="nomJoueurs">Nom :</label>\r\n        <br>    \r\n        <br>\r\n            <input type="text" id="nom" placeholder="Nom du Joueur" name="nom" required>\r\n        <br>\r\n        <br>\r\n            <label for="prenomJoueurs">Prénom :</label>\r\n        <br>\r\n        <br>\r\n            <input type="text" id="prenom" placeholder="Prénom du joueur" name="prenom" required>\r\n        <br>\r\n        <br>\r\n            <label for="dateNaiss">Date de naissance :</label>\r\n        <br>\r\n        <br>    \r\n            <input type="date" id="naiss" placeholder="Format AAAA-MM-JJ" name="naiss" required>\r\n        <br>\r\n        <br>\r\n            <label for="nationalite">Nationalité :</label>\r\n        <br>\r\n        <br>    \r\n            <input type="text" id="nationalite" placeholder="Nationalité du joueur" name="nationalite" required>\r\n        <br>\r\n        <br>\r\n            <label for="poste">Poste :</label>\r\n        <br>\r\n        <br>\r\n            <label for="poste">QB</label>\r\n            <input type="radio" id="poste" name="poste" value="QB" required>\r\n\r\n            <label for="poste">WR</label>\r\n            <input type="radio" id="poste" name="poste" value="WR" required>\r\n\r\n            <label for="poste">OL</label>\r\n            <input type="radio" id="poste" name="poste" value="OL" required>\r\n        \r\n            <label for="poste">DL</label>\r\n            <input type="radio" id="poste" name="poste" value="DL" required>\r\n\r\n            <label for="poste">RB</label>\r\n            <input type="radio" id="poste" name="poste" value="RB" required>\r\n\r\n            <label for="poste">FB</label>\r\n            <input type="radio" id="poste" name="poste" value="FB" required>\r\n\r\n            <label for="poste">TE</label>\r\n            <input type="radio" id="poste" name="poste" value="TE" required>\r\n\r\n            <label for="poste">LB</label>\r\n            <input type="radio" id="poste" name="poste" value="LB" required>\r\n\r\n            <label for="poste">CB</label>\r\n            <input type="radio" id="poste" name="poste" value="CB" required>\r\n\r\n            <label for="poste">S</label>\r\n            <input type="radio" id="poste" name="poste" value="S" required>\r\n\r\n            <label for="poste">K</label>\r\n            <input type="radio" id="poste" name="poste" value="K" required>\r\n\r\n            <label for="poste">P</label>\r\n            <input type="radio" id="poste" name="poste" value="P" required>\r\n\r\n            <label for="poste">KR</label>\r\n            <input type="radio" id="poste" name="poste" value="KR" required>\r\n\r\n            <label for="poste">PR</label>\r\n            <input type="radio" id="poste" name="poste" value="PR" required>\r\n\r\n            <label for="poste">SP</label>\r\n            <input type="radio" id="poste" name="poste" value="SP" required>\r\n        <br>\r\n        <br>\r\n            <label for="nClub">Numéro du club :</label>\r\n        <br>\r\n        <br>\r\n            <input type="number" id="club" placeholder="" name="club" required>\r\n        <br>\r\n        <br>\r\n            <label for="salaire">Salaire annuel :</label>\r\n        <br>\r\n        <br>    \r\n            <input type="number" id="salaire" placeholder="" name="salaire" required>\r\n        <br>\r\n        <br>\r\n            <label for="taille">Taille :</label>\r\n        <br>\r\n        <br>\r\n            <input type="number" id="taille" placeholder="En centimètres" name="taille" step="any" inputmode="decimal" required>\r\n        <br>\r\n        <br>\r\n            <label for="poids">Poids :</label>\r\n        <br>\r\n        <br>\r\n            <input type="number" id="poids" placeholder="En kilogrammes" name="poids" step="any" inputmode="decimal" required>\r\n        <br>\r\n        <br>\r\n            <label for="sprint40y">Sprint sur 40 yards :</label>\r\n        <br>\r\n        <br>\r\n            <input type="number" id="sprint" placeholder="En secondes" name="sprint" step="any" inputmode="decimal" required>\r\n        <br>\r\n        <br>\r\n            <input type="submit" value="Insérer" class="btn-insérer">\r\n    </form>\r\n    </div>\r\n</div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "res/templates/ajoutJoueur.html", "uri": "ajoutJoueur.html", "source_encoding": "utf-8", "line_map": {"27": 0, "33": 1, "34": 10, "35": 10, "41": 35}}
__M_END_METADATA
"""
