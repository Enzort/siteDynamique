import pymysql
import csv
from datetime import datetime


conn = None

def connectivité():
    global conn
    conn = pymysql.connect(host="localhost", user="admin", password="admin", db="footus")




    

def visualiserJoueur() :
    connectivité()
    cur = conn.cursor()
    cur.execute("SELECT nJoueur, nomJoueurs, prenomJoueurs, DATE_FORMAT(dateNaiss,'%Y-%m-%d'), nationalite, poste, nClub, salaire, taille, poids, sprint40y FROM joueurs ORDER BY nJoueur;")
    return cur.fetchall()
    conn.commit()
    cur.close()
    conn.close


def visualiserClub() :
    connectivité()
    cur = conn.cursor()
    cur.execute("SELECT nClub,nomClub,nomVille,budget,nomStade,DATE_FORMAT(dateCrea,'%Y-%m-%d') FROM clubs;")
    return cur.fetchall()
    conn.commit()
    cur.close()
    conn.close

def visualiserJoueurAge() :
    connectivité()
    cur = conn.cursor()
    cur.execute("SELECT nJoueur, nomJoueurs, prenomJoueurs, DATE_FORMAT(dateNaiss,'%Y-%m-%d'), nationalite, poste, nClub, salaire, taille, poids, sprint40y FROM joueurs ORDER BY dateNaiss DESC;")
    return cur.fetchall()
    conn.commit()
    cur.close()
    conn.close

def AjouterJoueur(nom,prenom,naiss,nationalite,poste,club,salaire,taille,poids,sprint) :
    connectivité()
    cur = conn.cursor()
    cur.execute("INSERT INTO joueurs (nomJoueurs,prenomJoueurs,dateNaiss,nationalite,poste,nClub,salaire,taille,poids,sprint40y) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (nom,prenom,naiss,nationalite,poste,club,salaire,taille,poids,sprint))
    conn.commit()
    cur.close()
    conn.close()



def supprimerJoueur(nJoueur) :
    connectivité()
    cur = conn.cursor()
    cur.execute("DELETE FROM joueurs WHERE nJoueur = %s", (nJoueur,))
    conn.commit()
    cur.close()
    conn.close()



def visualiserClubBudget():
    connectivité()
    cur = conn.cursor()
    cur.execute("SELECT nClub,nomClub,nomVille,budget,nomStade,DATE_FORMAT(dateCrea,'%Y-%m-%d') FROM clubs ORDER BY budget;")
    return cur.fetchall()
    conn.commit()
    cur.close()
    conn.close


def visualiserClubCreation():
    connectivité()
    cur = conn.cursor()
    cur.execute("SELECT nClub,nomClub,nomVille,budget,nomStade,DATE_FORMAT(dateCrea,'%Y-%m-%d') FROM clubs ORDER BY dateCrea;")
    return cur.fetchall()
    conn.commit()
    cur.close()
    conn.close




def insertTransf(nJou, Mont, date, Achet) :
    connectivité()
    cur = conn.cursor()
    cur.execute("INSERT INTO transferts (nJoueur, Montant, Date, Acheteur) VALUES (%s,%s,%s,%s)", (nJou, Mont, date, Achet))
    conn.commit()
    cur.close()
    cur.close()

def visualiserTransfert() :
    connectivité()
    cur = conn.cursor()
    cur.execute("SELECT joueurs.nomJoueurs,joueurs.prenomJoueurs,joueurs.nJoueur,transferts.Montant,transferts.Acheteur,transferts.Date FROM joueurs JOIN transferts ON transferts.nJoueur = joueurs.nJoueur ORDER BY joueurs.nJoueur;")
    return cur.fetchall()
    conn.commit()
    cur.close()
    conn.close

def ModifierJoueur(num,nom,prenom,naiss,nationalite,poste,club,salaire,taille,poids,sprint):
    connectivité()
    cur = conn.cursor()
    cur.execute("UPDATE joueurs SET nomJoueurs = %s, prenomJoueurs = %s, dateNaiss = %s , nationalite = %s, poste = %s, nClub = %s, salaire = %s, taille = %s, poids = %s, sprint40y = %s WHERE nJoueur = %s", (nom,prenom,naiss,nationalite,poste,club,salaire,taille,poids,sprint,num))
    conn.commit()
    cur.close()
    conn.close()


def createBaseMySQL() :

    conn = pymysql.connect(host="localhost", user="admin", password="admin", db="")
    cur = conn.cursor()
    
    cur.execute("DROP DATABASE IF EXISTS footus")
    cur.execute("CREATE DATABASE footus")
    cur.execute("USE footus")




# Table clubs
    cur.execute('''CREATE TABLE clubs ( nClub int NOT NULL AUTO_INCREMENT,
            nomClub varchar(50) NOT NULL,
            nomVille varchar(30) NOT NULL,
            budget int NOT NULL,
            nomStade varchar(40) NOT NULL,
            dateCrea date NOT NULL,
            PRIMARY KEY (nClub))
            ENGINE=InnoDB DEFAULT CHARSET=latin1;''')




# Table joueurs
    cur.execute('''CREATE TABLE joueurs (nJoueur int NOT NULL AUTO_INCREMENT,
            nomJoueurs varchar(30) NOT NULL,
            prenomJoueurs varchar(30) NOT NULL,
            dateNaiss date NOT NULL,
            nationalite varchar(35) NOT NULL,
            poste enum('QB','WR','OL','DL','RB','FB','TE','LB','CB','S','K','P','KR','PR','SP') NOT NULL,
            nClub int NOT NULL,
            salaire int NOT NULL,
            taille float NOT NULL,
            poids float NOT NULL,
            sprint40y float NOT NULL,
            PRIMARY KEY (nJoueur),
            FOREIGN KEY (nClub) REFERENCES clubs(nClub) ON DELETE CASCADE)
            ENGINE=InnoDB DEFAULT CHARSET=latin1;''')



# Table transferts
    cur.execute('''CREATE TABLE IF NOT EXISTS transferts (
          nTransfert int NOT NULL AUTO_INCREMENT,
          nJoueur int NOT NULL,
          Montant int NOT NULL,
          Date date NOT NULL,
          Acheteur varchar(30) NOT NULL,
          PRIMARY KEY (nTransfert),
          FOREIGN KEY (nJoueur) REFERENCES joueurs(nJoueur) ON DELETE CASCADE)
          ENGINE=InnoDB DEFAULT CHARSET=latin1;''')


# csv clubs
    with open('CLUBS.csv', mode='r', encoding='utf-8') as fichier_csv:
        lecteur_csv = csv.reader(fichier_csv, delimiter=';') 
        for ligne in lecteur_csv:
            club, ville, budget, stade, creation = ligne
            creation = datetime.strptime(creation, '%d/%m/%Y').date()
            s2 = f"INSERT INTO clubs (nomClub,nomVille,budget,nomStade,dateCrea) VALUES ('{club}','{ville}','{budget}','{stade}','{creation}')"
            cur.execute(s2)


# csv joueurs
    with open('JOUEUR.csv', mode='r', encoding='utf-8') as fichier_csv:
        lecteur_csv = csv.reader(fichier_csv, delimiter=';')
        for ligne in lecteur_csv:
            nom, prenom, dateNaiss, nationalite, poste, nClub, salaire, taille, poids, sprint = ligne
            dateNaiss = datetime.strptime(dateNaiss, '%d/%m/%Y').date()
            s = f"INSERT INTO joueurs (nomJoueurs,prenomJoueurs,dateNaiss,nationalite,poste,nClub,salaire,taille,poids,sprint40y) VALUES ('{nom}','{prenom}','{dateNaiss}','{nationalite}','{poste}','{nClub}','{salaire}','{taille}','{poids}','{sprint}')"
            cur.execute(s)


    conn.commit()
    cur.close()
    conn.close()
