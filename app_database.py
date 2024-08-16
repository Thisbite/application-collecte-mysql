import config as cf
import mysql.connector
from mysql.connector import Error
def table_administration_parametre():
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = cf.create_connection()
    cursor = conn.cursor()
    create_table_commands = [
        """
        CREATE TABLE IF NOT EXISTS DirectionStatistique (
            direction_id INTEGER PRIMARY KEY,
            Description TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Region (
            region_id INTEGER PRIMARY KEY,
            f_direction_stat_id INTEGER,
            nom_region TEXT,
            FOREIGN KEY (f_direction_stat_id) REFERENCES DirectionStatistique(direction_id)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Departement (
            departement_id INTEGER PRIMARY KEY,
            f_region_id INTEGER,
            nom_departement TEXT,
            FOREIGN KEY (f_region_id) REFERENCES Region(region_id)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS SousPrefectures (
            sousprefect_id INTEGER PRIMARY KEY,
            f_departement_id INTEGER,
            nom_sousprefecture TEXT,
            FOREIGN KEY (f_departement_id) REFERENCES Departement(departement_id)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Domaine (
            domaine_id INTEGER PRIMARY KEY,
            nom_domaine TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS SousDomaine (
            sous_domaine_id INTEGER PRIMARY KEY,
            f_domaine_id INTEGER,
            nom_sous_domaine TEXT,
            FOREIGN KEY (f_domaine_id) REFERENCES Domaine(domaine_id)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Indicateur (
            indicateur_id INTEGER PRIMARY KEY,
            f_domaine_id INTEGER,
            nom_indicateur TEXT,
            FOREIGN KEY (f_domaine_id) REFERENCES Domaine(domaine_id)
        );
        """,

        """
        CREATE TABLE IF NOT EXISTS Directeur (
            id INTEGER PRIMARY KEY,
            Nom TEXT,
            Prenom TEXT,
            Email TEXT,
            Numero TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS AgentCollecte (
            id INTEGER PRIMARY KEY,
            Nom TEXT,
            Prenom TEXT,
            Email TEXT,
            Numero TEXT
        );
        """
    ]

    # Execute each create table command
    for command in create_table_commands:
        try:
            cursor.execute(command)
            print(f"Table créée avec succès avec la commande :\n{command}")
        except Error as e:
            print(f"Une erreur est survenue : {e.args[0]}")

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
table_administration_parametre()


"""
Niveau de désagrégation
"""


def table_niveau_desagregation():
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = cf.create_connection()
    cursor = conn.cursor()

    create_table_commands = [
        """
        CREATE TABLE IF NOT EXISTS Cycle (
            id_cycle INTEGER PRIMARY KEY,
            nom_cycle TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Niveau_Prescolaire (
            niv_prescolaire_id INTEGER PRIMARY KEY,
            nom_prescolaire TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Niveau_Primaire (
            niv_primaire_id INTEGER PRIMARY KEY,
            nom_primaire TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Niveau_Secondaire_1er_cycle (
            niv_secondaire_1er_cycle_id INTEGER PRIMARY KEY,
            nom_secondaire_1er_cycle TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Niveau_Secondaire_2nd_cycle (
            niv_secondaire_2nd_cycle_id INTEGER PRIMARY KEY,
            nom_secondaire_2nd_cycle TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Niveau_Technique (
            niv_technique_id INTEGER PRIMARY KEY,
            nom_technique TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Niveau_Superieur (
            niv_superieur_id INTEGER PRIMARY KEY,
            nom_superieur TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Niveau_Professionnel (
            niv_professionnel_id INTEGER PRIMARY KEY,
            nom_professionnel TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Type_examen (
            id_type_examen INTEGER PRIMARY KEY,
            nom_type_examen TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Infrastructures_sanitaires (
            id_infrastructures_sanitaires INTEGER PRIMARY KEY,
            nom_infrastructures_sanitaires TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Lieu_accouchement (
            id_lieu_accouchement INTEGER PRIMARY KEY,
            nom_lieu_accouchement TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Etat_vaccinal (
            id_etat_vaccinal INTEGER PRIMARY KEY,
            nom_etat_vaccinal TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Types_de_vaccination (
            id_types_de_vaccination INTEGER PRIMARY KEY,
            nom_types_de_vaccination TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Pathologie (
            id_pathologie INTEGER PRIMARY KEY,
            nom_pathologie TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Tranche_age (
            id_tranche_age INTEGER PRIMARY KEY,
            nom_tranche_age TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Maladies_du_PEV (
            id_maladies_du_pev INTEGER PRIMARY KEY,
            nom_maladies_du_pev TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Maladies_infectieuses (
            id_maladies_infectieuses INTEGER PRIMARY KEY,
            nom_maladies_infectieuses TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Infection_respiratoire (
                  id_infectieuses_respiratoire INTEGER PRIMARY KEY,
                  nom_infectieuses_respiratoire TEXT
              );
              """,
        """
        CREATE TABLE IF NOT EXISTS Maladies_IST (
            id_maladies_ist INTEGER PRIMARY KEY,
            nom_maladies_ist TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Type_de_Maladie (
            id_type_de_maladie INTEGER PRIMARY KEY,
            nom_type_de_maladie TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Activites_IEC (
            id_activites_iec INTEGER PRIMARY KEY,
            nom_activites_iec TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Service_Medicaux (
            id_service_medicaux INTEGER PRIMARY KEY,
            nom_service_medicaux TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Type_infrastructures_ou_organisations_sportives (
            id_type_infrastructures_sportives INTEGER PRIMARY KEY,
            nom_type_infrastructures_sportives TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Disciplines_sportives (
            id_disciplines_sportives INTEGER PRIMARY KEY,
            nom_disciplines_sportives TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Type_infrastructures_culturelles (
            id_type_infrastructures_culturelles INTEGER PRIMARY KEY,
            nom_type_infrastructures_culturelles TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Type_de_Patrimoines_culturels_immatériels (
            id_type_patrimoines_culturels_immatériels INTEGER PRIMARY KEY,
            nom_type_patrimoines_culturels_immatériels TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Type_actions_culturelles_et_artistiques (
            id_type_actions_culturelles_artistiques INTEGER PRIMARY KEY,
            nom_type_actions_culturelles_artistiques TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Type_operateurs_des_oeuvres_esprit (
            id_type_operateurs_oeuvres_esprit INTEGER PRIMARY KEY,
            nom_type_operateurs_oeuvres_esprit TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Type_de_groupes_culturels (
            id_type_groupes_culturels INTEGER PRIMARY KEY,
            nom_type_groupes_culturels TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Type_de_manifestations_culturelles (
            id_type_manifestations_culturelles INTEGER PRIMARY KEY,
            nom_type_manifestations_culturelles TEXT
        );
        """,

        """
        CREATE TABLE IF NOT EXISTS Trimestre (
        id_trimestre INTEGER PRIMARY KEY,
            nom_trimestre TEXT 
               );
         """,
        """
        CREATE TABLE IF NOT EXISTS Etat_des_ouvrages(
        id_etat_des_ouvrages INTEGER PRIMARY KEY,
        nom_etat_des_ouvrages TEXT 

        );

        """,
        """
        CREATE TABLE IF NOT EXISTS Type_abonnement(
        id_type_abonnnement INTEGER PRIMARY KEY,
        nom_type_abonnnement TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Type_suivi(
        id_type_suivi INTEGER PRIMARY KEY,
        nom_type_suivi TEXT 

        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Type_de_vulnerabilite(
        id_type_de_vulnerabilite INTEGER PRIMARY KEY,
        nom_type_de_vulnerabilite TEXT 
        );

        """,
        """
        CREATE TABLE IF NOT EXISTS Type_de_prise_charge(
        id_type_de_prise_charge INTEGER PRIMARY KEY,
        nom_type_de_prise_charge TEXT
        );

        """,
        """
        CREATE TABLE IF NOT EXISTS Niveau(
        id_niveau INTEGER PRIMARY KEY,
        nom_niveau TEXT
        );
        """
        ,
        """
        CREATE TABLE IF NOT EXISTS Sexe (
            sexe_id INTEGER PRIMARY KEY,
            sexe TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS GroupeAge (
            grp_age_id INTEGER PRIMARY KEY,
            groupe_age TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Age (
            age_id INTEGER PRIMARY KEY,
            age TEXT
        );
        """
    ]

    # Execute each create table command
    for command in create_table_commands:
        try:
            cursor.execute(command)
            print(f"Table créée avec succès avec la commande :\n{command}")
        except Error as e:
            print(f"Une erreur est survenue : {e.args[0]}")

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

#Appel à la fonction
table_niveau_desagregation()

"""
Table de valeurs des indicateurs
"""


def table_valeurs_indicateur():
    """Crée la table ValeursIndicateurs si elle n'existe pas déjà."""
    conn = cf.create_connection()
    if conn is None:
        print("Connexion à la base de données échouée. Table non créée.")
        return

    cursor = conn.cursor()
    create_table_query = """
    CREATE TABLE IF NOT EXISTS ValeursIndicateurs (
        id INT AUTO_INCREMENT PRIMARY KEY,
        Valeur DECIMAL(10,2),
        Annee INT,
        f_sexe_id INT,
        f_grp_age_id INT,
        f_age_id INT,
        f_cycle_id INT,
        f_region_id INT,
        f_departement_id INT,
        f_sous_prefecture_id INT,
        f_indicateur_id INT,
        f_niveau_prescolaire_id INT,
        f_niveau_primaire_id INT,
        f_niveau_secondaire_1er_cycle_id INT,
        f_niveau_secondaire_2nd_cycle_id INT,
        f_niveau_technique_id INT,
        f_niveau_superieur_id INT,
        f_niveau_professionnel_id INT,
        f_type_examen_id INT,
        f_infrastructures_sanitaires_id INT,
        f_lieu_accouchement_id INT,
        f_etat_vaccinal_id INT,
        f_types_de_vaccination_id INT,
        f_pathologie_id INT,
        f_tranche_age_id INT,
        f_maladies_du_pev_id INT,
        f_maladies_infectieuses_id INT,
        f_infectieuses_respiratoire_id INT,
        f_maladies_ist_id INT,
        f_type_de_maladie_id INT,
        f_activites_iec_id INT,
        f_service_medicaux_id INT,
        f_type_infrastructures_ou_organisations_sportives_id INT,
        f_disciplines_sportives_id INT,
        f_type_infrastructures_culturelles_id INT,
        f_type_de_patrimoines_culturels_immat_id INT,
        f_type_actions_culturelles_et_artistiques_id INT,
        f_type_operateurs_des_oeuvres_esprit_id INT,
        f_type_de_groupes_culturels_id INT,
        f_type_de_manifestations_culturelles_id INT,

        f_trimestre_id INT,
        f_etat_des_ouvrages_id INT,
        f_type_abonnement_id INT,
        f_type_suivi_id INT,
        f_type_de_vulnerabilite_id INT,
        f_type_de_prise_charge_id INT,
        f_niveau_id INT,

        FOREIGN KEY (f_trimestre_id) REFERENCES Trimestre(id_trimestre),
        FOREIGN KEY (f_etat_des_ouvrages_id) REFERENCES Etat_des_ouvrages(id_etat_des_ouvrages),
        FOREIGN KEY (f_type_abonnement_id) REFERENCES Type_abonnement(id_type_abonnnement),
        FOREIGN KEY (f_type_suivi_id) REFERENCES Type_suivi(id_type_suivi),
        FOREIGN KEY (f_type_de_vulnerabilite_id) REFERENCES Type_de_vulnerabilite(id_type_de_vulnerabilite),
        FOREIGN KEY (f_type_de_prise_charge_id) REFERENCES Type_de_prise_charge(id_type_de_prise_charge),
        FOREIGN KEY (f_niveau_id) REFERENCES Niveau(id_niveau),

        FOREIGN KEY (f_region_id) REFERENCES Region(region_id),
        FOREIGN KEY (f_departement_id) REFERENCES Departement(departement_id),
        FOREIGN KEY (f_sous_prefecture_id) REFERENCES SousPrefectures(sousprefect_id),
        FOREIGN KEY (f_indicateur_id) REFERENCES Indicateur(indicateur_id),
        FOREIGN KEY (f_sexe_id) REFERENCES Sexe(sexe_id),
        FOREIGN KEY (f_grp_age_id) REFERENCES GroupeAge(grp_age_id),
        FOREIGN KEY (f_age_id) REFERENCES Age(age_id),
        FOREIGN KEY (f_cycle_id) REFERENCES Cycle(id_cycle),
        FOREIGN KEY (f_niveau_prescolaire_id) REFERENCES Niveau_Prescolaire(niv_prescolaire_id),
        FOREIGN KEY (f_niveau_primaire_id) REFERENCES Niveau_Primaire(niv_primaire_id),
        FOREIGN KEY (f_niveau_secondaire_1er_cycle_id) REFERENCES Niveau_Secondaire_1er_cycle(niv_secondaire_1er_cycle_id),
        FOREIGN KEY (f_niveau_secondaire_2nd_cycle_id) REFERENCES Niveau_Secondaire_2nd_cycle(niv_secondaire_2nd_cycle_id),
        FOREIGN KEY (f_niveau_technique_id) REFERENCES Niveau_Technique(niv_technique_id),
        FOREIGN KEY (f_niveau_superieur_id) REFERENCES Niveau_Superieur(niv_superieur_id),
        FOREIGN KEY (f_niveau_professionnel_id) REFERENCES Niveau_Professionnel(niv_professionnel_id),
        FOREIGN KEY (f_type_examen_id) REFERENCES Type_examen(id_type_examen),
        FOREIGN KEY (f_infrastructures_sanitaires_id) REFERENCES Infrastructures_sanitaires(id_infrastructures_sanitaires),
        FOREIGN KEY (f_lieu_accouchement_id) REFERENCES Lieu_accouchement(id_lieu_accouchement),
        FOREIGN KEY (f_etat_vaccinal_id) REFERENCES Etat_vaccinal(id_etat_vaccinal),
        FOREIGN KEY (f_types_de_vaccination_id) REFERENCES Types_de_vaccination(id_types_de_vaccination),
        FOREIGN KEY (f_pathologie_id) REFERENCES Pathologie(id_pathologie),
        FOREIGN KEY (f_tranche_age_id) REFERENCES Tranche_age(id_tranche_age),
        FOREIGN KEY (f_maladies_du_pev_id) REFERENCES Maladies_du_PEV(id_maladies_du_pev),
        FOREIGN KEY (f_maladies_infectieuses_id) REFERENCES Maladies_infectieuses(id_maladies_infectieuses),
        FOREIGN KEY (f_infectieuses_respiratoire_id) REFERENCES Infection_respiratoire(id_infectieuses_respiratoire),
        FOREIGN KEY (f_maladies_ist_id) REFERENCES Maladies_IST(id_maladies_ist),
        FOREIGN KEY (f_type_de_maladie_id) REFERENCES Type_de_Maladie(id_type_de_maladie),
        FOREIGN KEY (f_activites_iec_id) REFERENCES Activites_IEC(id_activites_iec),
        FOREIGN KEY (f_service_medicaux_id) REFERENCES Service_Medicaux(id_service_medicaux),
        FOREIGN KEY (f_type_infrastructures_ou_organisations_sportives_id) REFERENCES Type_infrastructures_ou_organisations_sportives(id_type_infrastructures_sportives),
        FOREIGN KEY (f_disciplines_sportives_id) REFERENCES Disciplines_sportives(id_disciplines_sportives),
        FOREIGN KEY (f_type_infrastructures_culturelles_id) REFERENCES Type_infrastructures_culturelles(id_type_infrastructures_culturelles),
        FOREIGN KEY (f_type_de_patrimoines_culturels_immat_id) REFERENCES Type_de_Patrimoines_culturels_immatériels(id_type_patrimoines_culturels_immatériels),
        FOREIGN KEY (f_type_actions_culturelles_et_artistiques_id) REFERENCES Type_actions_culturelles_et_artistiques(id_type_actions_culturelles_artistiques),
        FOREIGN KEY (f_type_operateurs_des_oeuvres_esprit_id) REFERENCES Type_operateurs_des_oeuvres_esprit(id_type_operateurs_oeuvres_esprit),
        FOREIGN KEY (f_type_de_groupes_culturels_id) REFERENCES Type_de_groupes_culturels(id_type_groupes_culturels),
        FOREIGN KEY (f_type_de_manifestations_culturelles_id) REFERENCES Type_de_manifestations_culturelles(id_type_manifestations_culturelles)
    );
    """

    try:
        cursor.execute(create_table_query)
        print("Table ValeursIndicateurs créée avec succès.")
    except Error as e:
        print(f"Une erreur est survenue lors de la création de la table : {e}")

    conn.commit()
    conn.close()
    print("Base de données mise à jour avec succès.")

# Appel de la fonction pour créer la table
table_valeurs_indicateur()


