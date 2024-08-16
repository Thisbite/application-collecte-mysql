import pandas as pd
import mysql.connector as mysql
import config as cf

conn = cf.create_connection()
cursor = conn.cursor()




"""



# Niveau secondaire premier cycle
df = pd.read_excel('second_1er_cycle.xlsx')
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Niveau_Secondaire_1er_cycle(niv_secondaire_1er_cycle_id, nom_secondaire_1er_cycle) VALUES (%s, %s)",
                           (row['id'], row['nom']))
conn.commit()
# Cycle
df = pd.read_excel('cycle.xlsx')
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Cycle(id_cycle, nom_cycle) VALUES (%s, %s)",
                           (row['id'], row['Cycle']))
conn.commit()

# Niveau préscolaire
df = pd.read_excel('prescolaire.xlsx')
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Niveau_Prescolaire(niv_prescolaire_id, nom_prescolaire) VALUES (%s, %s)",
                           (row['id'], row['Niveau_Prescolaire']))
conn.commit()

# Region
df = pd.read_excel('region.xlsx')
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Region(region_id, f_direction_stat_id, nom_region) VALUES (%s, %s, %s)",
                         (row['code_region'], row['direction_id'], row['region']))
conn.commit()

# Departement
df = pd.read_excel('departement.xlsx')
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Departement(departement_id, f_region_id, nom_departement) VALUES (%s, %s, %s)",
                           (row['code_departement'], row['region_id'], row['departement']))
conn.commit()

# Sous-préfecture
df = pd.read_excel('sous_prefecture.xlsx')
for index, row in df.iterrows():
    cursor.execute("INSERT INTO SousPrefectures(sousprefect_id, f_departement_id, nom_sousprefecture) VALUES (%s, %s, %s)",
                           (row['code_sous_prefecture'], row['departement_id'], row['sous_prefecture']))
conn.commit()





 # Domaine
df = pd.read_excel('domaine.xlsx')
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Domaine(domaine_id, nom_domaine) VALUES (%s, %s)",
    (row['code_domaine'], row['domaine']))

conn.commit()
df = pd.read_excel('primaire_ds')

for index, row in df.iterrows():
    cursor.execute("INSERT INTO Niveau_Primaire(niv_primaire_id, nom_primaire) VALUES (%s, %s)",
                           (row['id'], row['primaire']))
conn.commit()

# Niveau technique
df = pd.read_excel('niveau_technique.xlsx')
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Niveau_Technique(niv_technique_id, nom_technique) VALUES (%s, %s)",
                           (row['id'], row['niveau_technique']))
conn.commit()


 # Supérieur cycle
df = pd.read_excel('superieur_cycle.xlsx')
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Niveau_Superieur(niv_superieur_id, nom_superieur) VALUES (%s, %s)",
                           (row['id'], row['nom']))
conn.commit()


# Niveau secondaire 2ème cycle
df = pd.read_excel('niveau_secon_2nd_cycle.xlsx')
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Niveau_Secondaire_2nd_cycle(niv_secondaire_2nd_cycle_id, nom_secondaire_2nd_cycle) VALUES (%s, %s)",
                           (row['id'], row['nom']))
conn.commit()

#Proffessionnelle cycle
df = pd.read_excel('professionnelle_cycle.xlsx')
# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Niveau_Professionnel( niv_professionnel_id, nom_professionnel) VALUES ( ?, ?)",
                  (row['id'], row['nom']))

# Valider les modifications
conn.commit()

# Fermer la connexion
conn.close()



#type examen
df = pd.read_excel('examen_scolaire.xlsx')
# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Type_examen( id_type_examen, nom_type_examen) VALUES ( ?, ?)",
                  (row['id'], row['nom']))

# Valider les modifications
conn.commit()

# Fermer la connexion
conn.close()
"""
#Groupe age
df = pd.read_excel('groupe_age.xlsx')
# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO  GroupeAge ( grp_age_id,  groupe_age ) VALUES ( %s, %s)",
                  (row['id'], row['nom']))

# Valider les modifications
conn.commit()
"""
# Fermer la connexion
conn.close()


#Infractructure sanitaire
df = pd.read_excel('infrastructure_sani.xlsx')
# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO  Infrastructures_sanitaires ( id_infrastructures_sanitaires,  nom_infrastructures_sanitaires ) VALUES ( ?, ?)",
                  (row['id'], row['nom']))

# Valider les modifications
conn.commit()

# Fermer la connexion
conn.close()



# Lieu Accouchement
df = pd.read_excel('accouchement.xlsx')
# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO  Lieu_accouchement ( id_lieu_accouchement,  nom_lieu_accouchement ) VALUES ( ?, ?)",
                  (row['id'], row['nom']))

# Valider les modifications
conn.commit()

# Fermer la connexion
conn.close()



# Services médicaux
df = pd.read_excel('service_medicaux.xlsx')
# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Service_Medicaux( id_service_medicaux,  nom_service_medicaux ) VALUES ( ?, ?)",
                  (row['id'], row['nom']))

# Valider les modifications
conn.commit()

# Fermer la connexion
conn.close()




# Etat de vaccination
df = pd.read_excel('etat_vaccination.xlsx')
# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Etat_vaccinal( id_etat_vaccinal,  nom_etat_vaccinal ) VALUES ( ?, ?)",
                  (row['id'], row['nom']))

# Valider les modifications
conn.commit()

# Fermer la connexion
conn.close()

# Type de vaccination 
df = pd.read_excel('type_vaccination.xlsx')
# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Types_de_vaccination( id_types_de_vaccination,  nom_types_de_vaccination ) VALUES ( ?, ?)",
                  (row['id'], row['nom']))

# Valider les modifications
conn.commit()

# Fermer la connexion
conn.close()



# Pathologie
df = pd.read_excel('pathologie.xlsx')
# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Pathologie( id_pathologie,  nom_pathologie ) VALUES ( ?, ?)",
                  (row['id'], row['nom']))

# Valider les modifications
conn.commit()

# Fermer la connexion
conn.close()



# Tranche d'âge
df = pd.read_excel('tranche_age.xlsx')
# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Tranche_age( id_tranche_age,  nom_tranche_age ) VALUES ( ?, ?)",
                  (row['id'], row['nom']))

# Valider les modifications
conn.commit()

# Fermer la connexion
conn.close()



# Maladie PEV
df = pd.read_excel('maladie_pev.xlsx')
# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Maladies_du_PEV( id_maladies_du_pev,  nom_maladies_du_pev ) VALUES ( ?, ?)",
                  (row['id'], row['nom']))

# Valider les modifications
conn.commit()

# Fermer la connexion
conn.close()



# Maladie infectieuse
df = pd.read_excel('maladies_infectieuse.xlsx')
# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Maladies_infectieuses( id_maladies_infectieuses, nom_maladies_infectieuses ) VALUES ( ?, ?)",
                  (row['id'], row['nom']))

# Valider les modifications
conn.commit()

# Fermer la connexion
conn.close()


#Infections respiratoire
df = pd.read_excel('infection_respiratoire.xlsx')
# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Infection_respiratoire( id_infectieuses_respiratoire,nom_infectieuses_respiratoire) VALUES ( ?, ?)",
                  (row['id'], row['nom']))

# Valider les modifications
conn.commit()

# Fermer la connexion
conn.close()



#Maladies IST
df = pd.read_excel('maladie_ist.xlsx')
# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Maladies_IST( id_maladies_ist,nom_maladies_ist) VALUES ( ?, ?)",
                  (row['id'], row['nom']))

# Valider les modifications
conn.commit()

# Fermer la connexion
conn.close()



# Type maladies
df = pd.read_excel('type_maladie.xlsx')
# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Type_de_Maladie( id_type_de_maladie,nom_type_de_maladie) VALUES ( ?, ?)",
                  (row['id'], row['nom']))

# Valider les modifications
conn.commit()

# Fermer la connexion
conn.close()


# Activités IES
df = pd.read_excel('activite_ies.xlsx')
# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Activites_IEC( id_activites_iec,nom_activites_iec) VALUES ( ?, ?)",
                  (row['id'], row['nom']))

# Valider les modifications
conn.commit()

# Fermer la connexion
conn.close()

#Sexe
df = pd.read_excel('ok_sexe.xlsx')
# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Sexe(sexe_id,sexe) VALUES (%s, %s)",
                  (row['id'], row['nom']))
conn.commit()
conn.close()



#Trimestre
df = pd.read_excel('trimestre.xlsx')
# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Trimestre (id_trimestre, nom_trimestre) VALUES (%s, %s)",
                  (row['id'], row['nom']))
conn.commit()
conn.close()

"""







