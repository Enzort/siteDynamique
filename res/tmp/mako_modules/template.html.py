# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1685981311.0430343
_enable_loop = True
_template_filename = 'res/templates/template.html'
_template_uri = 'template.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html lang="fr">\r\n    <head>\r\n        <title>Football Américain</title>\r\n        <meta charset="utf-8">\r\n        <meta http-equiv="X-UA-Compatible" content="IE=edge"    >\r\n        <meta name="viewport" content="width=device-width,initial-scale=1.0">\r\n        <link rel="stylesheet" href="../css/sae.css">\r\n    </head>\r\n    <body>\r\n        <nav class="navbar">\r\n            <a>Football Américain</a>\r\n            <div class="nav-links">\r\n                <ul>\r\n                    <li class="active"><a href="index">Accueil</a></li>\r\n                    <li class="dropdown">\r\n                        <a href="#" class="dropbtn">Joueurs</a>\r\n                        <div class="dropdown-content">\r\n                            <a href="affJou">Liste des joueurs</a>\r\n                            <a href="affJouAge">Liste des joueurs par âge</a>\r\n                        </div>\r\n                    </li>\r\n                    <li class="dropdown">\r\n                        <a href="#" class="dropbtn">Clubs</a>\r\n                        <div class="dropdown-content">\r\n                            <a href="affClub">Liste des clubs</a>\r\n                            <a href="affClubBudget">Liste des clubs par budget</a>\r\n                            <a href="affClubCrea">Liste des clubs par date de création</a>\r\n                        </div>\r\n                    </li>\r\n                    <li class="dropdown">\r\n                        <a href="#" class="dropbtn">Transferts</a>\r\n                        <div class="dropdown-content">\r\n                            <a href="insertTransfert">Proposer un transferts</a>\r\n                            <a href="affTransf">Voir les transferts</a>\r\n                        </div>\r\n                    </li>\r\n                    <li class="dropdown">\r\n                        <a href="#" class="dropbtn">Formulaires</a>\r\n                        <div class="dropdown-content">\r\n                            <a href="insertJoueur">Insérer d\'un joueur</a>\r\n                            <a href="suppressById">Supprimer un joueur</a>\r\n                            <a href="ModifierJoueur">Modifier un joueur</a>\r\n                        </div>\r\n                    </li>\r\n                </ul>       \r\n            </div>\r\n            <img class="menuH" src="../media/menuH.jpg" alt="">       \r\n        </nav>\r\n\r\n        ')
        __M_writer(str( self.body() ))
        __M_writer('\r\n\r\n        <script>\r\n\r\n            const menuHamburger = document.querySelector(".menuH")\r\n            const navLinks = document.querySelector(".nav-links")\r\n         \r\n            menuHamburger.addEventListener(\'click\',()=>{\r\n            navLinks.classList.toggle(\'mobile-menu\')\r\n            })\r\n        \r\n        </script>\r\n\r\n    </body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "res/templates/template.html", "uri": "template.html", "source_encoding": "utf-8", "line_map": {"16": 0, "22": 1, "23": 51, "24": 51, "30": 24}}
__M_END_METADATA
"""
