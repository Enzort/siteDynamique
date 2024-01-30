import cherrypy
import os.path
from mako.lookup import TemplateLookup
from mako.template import Template
from BD2 import createBaseMySQL, visualiserJoueur, visualiserClub, visualiserJoueurAge, AjouterJoueur, supprimerJoueur, \
  visualiserClubBudget, visualiserClubCreation, visualiserTransfert, insertTransf, ModifierJoueur

mylookup = TemplateLookup(directories=['res/templates'], input_encoding='utf-8', module_directory='res/tmp/mako_modules')
chemin_media = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'res' , 'media')
chemin_css = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'res' , 'css')


class InterfaceWebEtudiants(object):    

###### Page d'accueil #############
    
    @cherrypy.expose
    def index(self):
        mytemplate = mylookup.get_template("accueil.html")
        resultatJoueurs = visualiserJoueur()
        return mytemplate.render(mesJou=resultatJoueurs)
    
###### Page de joueurs #############
    
    @cherrypy.expose
    def affJou(self):
        mytemplate = mylookup.get_template("joueurs.html")        
        return mytemplate.render(mesJou=visualiserJoueur())
    
###### Page de joueurs par âge #############
    
    @cherrypy.expose
    def affJouAge(self):
        mytemplate = mylookup.get_template("joueurAge.html")        
        return mytemplate.render(mesJou=visualiserJoueurAge())
    
###### Page de clubs #############
    
    @cherrypy.expose
    def affClub(self):
        mytemplate = mylookup.get_template("clubs.html")        
        return mytemplate.render(mesClu=visualiserClub())
    
###### Page de clubs par budget #############
    
    @cherrypy.expose
    def affClubBudget(self):
        mytemplate = mylookup.get_template("clubsBudget.html")        
        return mytemplate.render(mesClu=visualiserClubBudget())
    
###### Page de clubs par date de création #############
    
    @cherrypy.expose
    def affClubCrea(self):
        mytemplate = mylookup.get_template("clubsCreation.html")        
        return mytemplate.render(mesClu=visualiserClubCreation())
    ###### Page des transferts #############
    
    @cherrypy.expose
    def affTransf(self):
        mytemplate = mylookup.get_template("transferts.html")        
        return mytemplate.render(mesTr=visualiserTransfert())
    
###### Pages des transferts ###########
    
    @cherrypy.expose
    def insertTransfert(self):        
        mytemplate = mylookup.get_template("insertTrasnfert.html")        
        return mytemplate.render(message="", type="info")

    @cherrypy.expose
    def insertTransferts(self, nJou=None, Mont=None, date=None, Achet=None ):
        if nJou and Mont and date and Achet :
            try:
                insertTransf(nJou, Mont, date, Achet )
                message = "Proposition de transfert effectuée !"
                typ = "success"
            except (Exception) as e:
                message = str(e)
                typ = "danger"
        else:
            message = ""
            typ = "warning"
        mytemplate = mylookup.get_template("insertTrasnfert.html")        
        return mytemplate.render(message=message, type=typ)
    
###### Pages d'insertion ###########
    
    @cherrypy.expose
    def insertJoueur(self, nom=None, prenom=None, naiss=None, nationalite=None, poste=None, club=None, salaire=None, taille=None, poids=None, sprint=None):
        if nom and prenom and naiss and nationalite and poste and club and salaire and taille and poids and sprint :
            print(naiss, " -:- ", type(naiss))
            try:
                AjouterJoueur(nom, prenom, naiss, nationalite, poste, club, salaire, taille, poids, sprint)
                message = "Insertion réussie !"
                typ = "success"
            except (Exception) as e:
                message = str(e)
                typ = "danger"
        else:
            message = ""
            typ = "warning"
        mytemplate = mylookup.get_template("ajoutJoueur.html")        
        return mytemplate.render(message=message, type=typ)
    
###### Pages de suppression ###########
    
    @cherrypy.expose
    def suppressById(self, nJoueur=None):
        if nJoueur :
            try:
                supprimerJoueur(int(nJoueur))
                message = "Suppression réussie !"
                typ = "success"
            except ValueError as e:
                message = str(e)
                typ = "danger"
        else:
            message = ""
            typ = "warning"
        mytemplate = mylookup.get_template("suppJoueur.html")        
        return mytemplate.render(message=message, type=typ)

###### Pages de modification ###########


    @cherrypy.expose
    def ModifierJoueur(self, num=None,nom=None,prenom=None,naiss=None,nationalite=None,poste=None,club=None,salaire=None,taille=None,poids=None,sprint=None ):
        if num and nom and prenom and naiss and nationalite and poste and club and salaire and taille and poids and sprint:
            try:
                ModifierJoueur(num,nom,prenom,naiss,nationalite,poste,club,salaire,taille,poids,sprint)
                message = "Modification effectuée !"
                typ = "success"
            except (Exception) as e:
                message = str(e)
                typ = "danger"
        else:
            message = ""
            typ = "warning"
        mytemplate = mylookup.get_template("modiJou.html")        
        return mytemplate.render(message=message, type=typ)





if __name__ == '__main__':
    rootPath = os.path.abspath(os.getcwd())
    print("la racine du site est :\n\t{rootPath}\n\tcontient : {os.listdir()}")
    createBaseMySQL()
    cherrypy.tree.mount(InterfaceWebEtudiants(), '/', {
        '/media' : {
            'tools.staticdir.on' : True,
            'tools.staticdir.dir' : os.path.join(chemin_media)
        },
        '/css' : {
            'tools.staticdir.on' : True,
            'tools.staticdir.dir' : os.path.join(chemin_css)
        }
        })
    cherrypy.engine.start()
    cherrypy.engine.block()
    
            


