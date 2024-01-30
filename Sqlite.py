import sqlite3

conn = sqlite3.connect('footus.db')

conn.execute('''CREATE TABLE IF NOT EXISTS clubs (
                nClub INTEGER PRIMARY KEY AUTOINCREMENT,
                nomClub TEXT NOT NULL,
                nomVille TEXT NOT NULL,
                budget INTEGER NOT NULL,
                nomStade TEXT NOT NULL,
                dateCrea DATE NOT NULL
            )''')

conn.execute('''CREATE TABLE IF NOT EXISTS joueurs (
                nJoueur INTEGER PRIMARY KEY AUTOINCREMENT,
                nomJoueurs TEXT NOT NULL,
                prenomJoueurs TEXT NOT NULL,
                dateNaiss DATE NOT NULL,
                nationalite TEXT NOT NULL,
                poste TEXT NOT NULL,
                nClub INTEGER NOT NULL,
                salaire INTEGER NOT NULL,
                taille FLOAT NOT NULL,
                poids FLOAT NOT NULL,
                sprint40y FLOAT NOT NULL,
                FOREIGN KEY(nClub) REFERENCES clubs(nClub)
            )''')

infos_clubs = [('New England Patriots', 'Foxborough', '230902712', 'Gillette Stadium', '1959-11-16'),
              ('Philadelphia Eagles', 'Philadelphie', '235626564', 'Lincoln Financial Field', '1933-07-08'),
              ('Cleveland Browns', 'Cleveland', '264278386', 'Cleveland Browns Stadium', '1944-06-04'),
              ('Minnesota Vikings', 'Minneapolis', '233453972', 'U.S. Bank Stadium', '1960-01-28'),
              ('Jacksonville Jaguars', 'Jacksonville', '226928830', 'TIAA Bank Field', '1993-11-30'),
              ('Tampa Bay Buccaneers', 'Tampa', '232311415', 'Raymond James Stadium', '1974-04-24'),
              ('Kansas City Chiefs', 'Kansas City',' 227369049', 'GEHA Field at Arrowhead Stadium', '1959-08-14'),
              ('Los Angeles Rams', 'Inglewood',' 214789198', 'SoFi Stadium', '1936-01-01')]

infos_joueurs = [('Bourne','Kendrick','04/08/1995','Americain','WR','1','6416666','185','86','4.55'),
              ('Scott','Boston','27/04/1995','Americain','RB','2','1750000','168','92','4.4'),
              ('Njoku','David','10/07/1996','Americain','TE','3','3328000','193','112','4.64'),
              ('Jefferson','Justin','16/06/1999','Americain','WR','4','3578946','185','88','4.43'),
              ('Lawrence','Trevor','06/10/1999','Americain','QB','5','8362156','198','97','4.78'),
              ('White','Devin','17/02/1998','Americain','LB','6','9527759','183','108','4.42'),
              ('Mahomes','Patrick','17/09/1995','Americain','QB','7','42403506','188','102','4.8'),
              ('Donald','Aaron','23/05/1991','Americain','DL','8','29842645','185','127','4.68')]


for club in infos_clubs:
    conn.execute("INSERT INTO clubs (nomClub,nomVille,budget,nomStade,dateCrea) VALUES (?,?,?,?,?)", club)
for joueur in infos_joueurs :
    conn.execute("INSERT INTO joueurs (nomJoueurs,prenomJoueurs,dateNaiss,nationalite,poste,nClub,salaire,taille,poids,sprint40y) VALUES (?,?,?,?,?,?,?,?,?,?)", joueur)


conn.commit()
conn.close()
