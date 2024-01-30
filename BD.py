import BD2
import pymysql



BD2.createBaseMySQL()





# REQUETES CRUD 

def visualiserJoueur() :
    db = BD2.connectivité()
    cursor = db.cursor()
    cursor.execute("SELECT nJoueur, nomJoueurs, prenomJoueurs, DATE_FORMAT(dateNaiss,'%Y-%m-%d'), nationalite, poste, nClub, salaire, taille, poids, sprint40y FROM joueurs ORDER BY nJoueur;")
    return cursor.fetchall()


def visualiserClub() :
    db = BD2.connectivité()
    cursor = db.cursor()
    cursor.execute("SELECT nClub,nomClub,nomVille,budget,nomStade,DATE_FORMAT(dateCrea,'%Y-%m-%d') FROM clubs;")
    return cursor.fetchall()

def visualiserJoueurAge() :
    db = BD2.connectivité()
    cursor = db.cursor()
    cursor.execute("SELECT nJoueur, nomJoueurs, prenomJoueurs, DATE_FORMAT(dateNaiss,'%Y-%m-%d'), nationalite, poste, nClub, salaire, taille, poids, sprint40y FROM joueurs ORDER BY dateNaiss DESC;")
    return cursor.fetchall()

def AjouterJoueur(nom,prenom,naiss,nationalite,poste,club,salaire,taille,poids,sprint) :
    db = BD2.connectivité()
    cursor = db.cursor()
    cursor.execute("INSERT INTO joueurs (nomJoueurs,prenomJoueurs,dateNaiss,nationalite,poste,nClub,salaire,taille,poids,sprint40y) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (nom,prenom,naiss,nationalite,poste,club,salaire,taille,poids,sprint))
    db.commit()
    cursor.close()
    db.close()


def supprimerJoueur(nJoueur) :
    db = BD2.connectivité()
    cursor = db.cursor()
    cursor.execute("DELETE FROM joueurs WHERE nJoueur = %s", (nJoueur,))
    db.commit()
    cursor.close()
    db.close()



def visualiserClubBudget():
    db = BD2.connectivité()
    cursor = db.cursor()
    cursor.execute("SELECT nClub,nomClub,nomVille,budget,nomStade,DATE_FORMAT(dateCrea,'%Y-%m-%d') FROM clubs ORDER BY budget;")
    return cursor.fetchall()


def visualiserClubCreation():
    db = BD2.connectivité()
    cursor = db.cursor()
    cursor.execute("SELECT nClub,nomClub,nomVille,budget,nomStade,DATE_FORMAT(dateCrea,'%Y-%m-%d') FROM clubs ORDER BY dateCrea;")
    return cursor.fetchall()






choix = 0
while choix != 8:
    print("\n--------------------------------------------------------------------------------")
    print("--------------------------------Mode CLI----------------------------------------")
    print("--------------------------------------------------------------------------------\n")
    print("--------------------------------------------------------------------------------")
    print("------------------------------CRUD JOUEURS--------------------------------------")
    print("--------------------------------------------------------------------------------\n")
    print("1 - Visualiser l'ensemble des joueurs")
    print("2 - Visualiser l'ensemble des joueurs par ordre croissant de l'âge")
    print("3 - Ajouter un joueur")
    print("4 - Supprimer un joueur")
    print("\n--------------------------------------------------------------------------------")
    print("-------------------------------CRUD CLUBS---------------------------------------")
    print("--------------------------------------------------------------------------------\n")
    print("5 - Visualiser l'ensemble des clubs")
    print("6 - Visualiser les clubs par budget dans l'ordre croissant")
    print("7 - Visualier les clubs par date de création du plus récent au plus ancien")
    print("\n--------------------------------------------------------------------------------\n")
    print("8 - Sortir du menu CLI")
    print("\n")

    choix = int(input("Entrez votre choix: "))
    print("\n")



    if choix == 1:
        joueurs = visualiserJoueur()
        print("{:<8} | {:<15} | {:<15} | {:<10} | {:<15} | {:<10} | {:<6} | {:<8} | {:<6} | {:<6} | {:<10}".format(
            "n° Joueur", "Nom", "Prenom", "Naissance", "Nationalite", "Poste",
            "n° Club", "Salaire", "Taille", "Poids", "Sprint sur 40 yards"
        ))
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------")
        print()
        for joueur in joueurs:
            print("{:<8} | {:<15} | {:<15} | {:<10} | {:<15} | {:<10} | {:<6} | {:<8} | {:<6} | {:<6} | {:<10}".format(*joueur))

    elif choix == 2:
        joueurs = visualiserJoueurAge()
        print("{:<8} | {:<15} | {:<15} | {:<10} | {:<15} | {:<10} | {:<6} | {:<8} | {:<6} | {:<6} | {:<10}".format(
            "n° Joueur", "Nom", "Prenom", "Naissance", "Nationalite", "Poste",
            "n° Club", "Salaire", "Taille", "Poids", "Sprintsur 40 yards"
        ))
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------")
        print()
        for joueur in joueurs:
            print("{:<8} | {:<15} | {:<15} | {:<10} | {:<15} | {:<10} | {:<6} | {:<8} | {:<6} | {:<6} | {:<10}".format(*joueur))
            
            
    elif choix == 3:
        nomJoueur = input("Entrez le nom du joueur : ")
        prenomJoueur = input("Entrez le prénom du joueur : ")
        dateNaiss = input("Entrez la date de naissance du joueur (AAAA-MM-JJ): ")
        nationalite = input("Entrez la nationalité du joueur : ")
        poste = input("Entrez le poste du joueur ('QB','WR','OL','DL','RB','FB','TE','LB','CB','S','K','P','KR','PR','SP'): ")
        nClub = input("Entrez le numéro du club : ")
        salaire = input("Entrez le salaire du joueur : ")
        taille = input("Entrez la taille du joueur (en cm): ")
        poids = input("Entrez le poids du joueur (en kg): ")
        sprint40y = input("Entrez le temps pour parcourir 40 yards (en s) : ")
        AjouterJoueur(nomJoueur, prenomJoueur, dateNaiss, nationalite, poste, nClub, salaire, taille, poids, sprint40y)

    elif choix == 4:
        nJoueur = input("Entrez le numéro du joueur à supprimer : ")
        supprimerJoueur(nJoueur)
        
    elif choix == 5:
        clubs = visualiserClub()
        print("{:<8} | {:<15} | {:<15} | {:<10} | {:<15} | {:<10} ".format(
            "n° Club","Nom du club","Nom de la ville","Budget en €","Nom du stade","Date de création"
        ))
        print("---------------------------------------------------------------------------------------------------------------")
        print()
        for club in clubs:
            print("{:<8} | {:<15} | {:<15} | {:<10} | {:<15} | {:<10} |".format(*club))
            
    elif choix == 6 :
        clubs = visualiserClubBudget()
        print("{:<8} | {:<15} | {:<15} | {:<10} | {:<15} | {:<10} ".format(
            "n° Club","Nom du club","Nom de la ville","Budget en €","Nom du stade","Date de création"
        ))
        print("---------------------------------------------------------------------------------------------------------------")
        print()
        for club in clubs:
            print("{:<8} | {:<15} | {:<15} | {:<10} | {:<15} | {:<10} |".format(*club))
            
            
    elif choix == 7:
        clubs = visualiserClubCreation()
        print("{:<8} | {:<15} | {:<15} | {:<10} | {:<15} | {:<10} ".format(
            "n° Club","Nom du club","Nom de la ville","Budget en €","Nom du stade","Date de création"
        ))
        print("---------------------------------------------------------------------------------------------------------------")
        print()
        for club in clubs:
            print("{:<8} | {:<15} | {:<15} | {:<10} | {:<15} | {:<10} |".format(*club))
            
            
        
    elif choix == 8:
        print("Merci d'avoir utilisé le menu CLI")

    else:
        print("Choix invalide")
