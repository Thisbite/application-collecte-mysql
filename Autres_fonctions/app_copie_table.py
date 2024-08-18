import mysql.connector
import pandas as pd
import Autres_fonctions.config as cf

def afficher_valeurs_indicateurs():
    conn = cf.create_connection()
    cursor = conn.cursor()

    query = """
    SELECT 
        VI.id,
        R.nom_region,
        D.nom_departement,
        SP.nom_sousprefecture,
        I.nom_indicateur,
        VI.Valeur,
        VI.Annee,
        S.sexe,
        GA.groupe_age,
        A.age,
        C.nom_cycle,
        NP.nom_prescolaire,
        N1C.nom_primaire,
        NS1C.nom_secondaire_1er_cycle,
        NS2C.nom_secondaire_2nd_cycle,
        NT.nom_technique,
        NS.nom_superieur,
        NP2.nom_professionnel,  -- Changé 'NP' en 'NP2' pour Niveau_Professionnel
        TE.nom_type_examen,
        SIS.nom_infrastructures_sanitaires,
        LA.nom_lieu_accouchement,
        EV.nom_etat_vaccinal,
        TV.nom_types_de_vaccination,
        P.nom_pathologie,
        TA.nom_tranche_age,
        MP.nom_maladies_du_pev,
        MI.nom_maladies_infectieuses,
        IRES.nom_infectieuses_respiratoire
        IST.nom_maladies_ist,
        TM.nom_type_de_maladie,
        AI.nom_activites_iec,
        SM.nom_service_medicaux,
        TIS.nom_type_infrastructures_sportives,
        DS.nom_disciplines_sportives,
        TIC.nom_type_infrastructures_culturelles,
        PCI.nom_type_patrimoines_culturels_immatériels,
        ACA.nom_type_actions_culturelles_artistiques,
        OE.nom_type_operateurs_oeuvres_esprit,
        GC.nom_type_groupes_culturels,
        MC.nom_type_manifestations_culturelles,
        
        
        TRIM.nom_trimestre,
        TDO.nom_etat_des_ouvrages,
        TABO.nom_type_abonnnement,
        TPSU.nom_type_suivi,
        TVUL.nom_type_de_vulnerabilite,
        TPCH.nom_type_de_prise_charge,
        NIVE.nom_niveau
        
    FROM ValeursIndicateurs VI
    
    LEFT JOIN Region R ON VI.f_region_id = R.region_id
    LEFT JOIN Departement D ON VI.f_departement_id = D.departement_id
    LEFT JOIN SousPrefectures SP ON VI.f_sous_prefecture_id = SP.sousprefect_id
    LEFT JOIN Indicateur I ON VI.f_indicateur_id = I.indicateur_id
    LEFT JOIN Sexe S ON VI.f_sexe_id = S.sexe_id
    LEFT JOIN GroupeAge GA ON VI.f_grp_age_id = GA.grp_age_id
    LEFT JOIN Age A ON VI.f_age_id = A.age_id
    LEFT JOIN Cycle C ON VI.f_cycle_id = C.id_cycle
    LEFT JOIN Niveau_Prescolaire NP ON VI.f_niveau_prescolaire_id = NP.niv_prescolaire_id
    LEFT JOIN Niveau_Primaire N1C ON VI.f_niveau_primaire_id = N1C.niv_primaire_id
    LEFT JOIN Niveau_Secondaire_1er_cycle NS1C ON VI.f_niveau_secondaire_1er_cycle_id = NS1C.niv_secondaire_1er_cycle_id
    LEFT JOIN Niveau_Secondaire_2nd_cycle NS2C ON VI.f_niveau_secondaire_2nd_cycle_id = NS2C.niv_secondaire_2nd_cycle_id
    LEFT JOIN Niveau_Technique NT ON VI.f_niveau_technique_id = NT.niv_technique_id
    LEFT JOIN Niveau_Superieur NS ON VI.f_niveau_superieur_id = NS.niv_superieur_id
    LEFT JOIN Niveau_Professionnel NP2 ON VI.f_niveau_professionnel_id = NP2.niv_professionnel_id  -- Utilisation de l'alias 'NP2'
    LEFT JOIN Type_examen TE ON VI.f_type_examen_id = TE.id_type_examen
    LEFT JOIN Infrastructures_sanitaires SIS ON VI.f_infrastructures_sanitaires_id = SIS.id_infrastructures_sanitaires
    LEFT JOIN Lieu_accouchement LA ON VI.f_lieu_accouchement_id = LA.id_lieu_accouchement
    LEFT JOIN Etat_vaccinal EV ON VI.f_etat_vaccinal_id = EV.id_etat_vaccinal
    LEFT JOIN Types_de_vaccination TV ON VI.f_types_de_vaccination_id = TV.id_types_de_vaccination
    LEFT JOIN Pathologie P ON VI.f_pathologie_id = P.id_pathologie
    LEFT JOIN Tranche_age TA ON VI.f_tranche_age_id = TA.id_tranche_age
    LEFT JOIN Maladies_du_PEV MP ON VI.f_maladies_du_pev_id = MP.id_maladies_du_pev
    LEFT JOIN Maladies_infectieuses MI ON VI.f_maladies_infectieuses_id = MI.id_maladies_infectieuses
    LEFT JOIN Infection_respiratoire IRES ON VI.f_infectieuses_respiratoire_id=IRES.id_infectieuses_respiratoire
    LEFT JOIN Maladies_IST IST ON VI.f_maladies_ist_id = IST.id_maladies_ist
    LEFT JOIN Type_de_Maladie TM ON VI.f_type_de_maladie_id = TM.id_type_de_maladie
    LEFT JOIN Activites_IEC AI ON VI.f_activites_iec_id = AI.id_activites_iec
    LEFT JOIN Service_Medicaux SM ON VI.f_service_medicaux_id = SM.id_service_medicaux
    LEFT JOIN Type_infrastructures_ou_organisations_sportives TIS ON VI.f_type_infrastructures_ou_organisations_sportives_id = TIS.id_type_infrastructures_sportives
    LEFT JOIN Disciplines_sportives DS ON VI.f_disciplines_sportives_id = DS.id_disciplines_sportives
    LEFT JOIN Type_infrastructures_culturelles TIC ON VI.f_type_infrastructures_culturelles_id = TIC.id_type_infrastructures_culturelles
    LEFT JOIN Type_de_Patrimoines_culturels_immatériels PCI ON VI.f_type_de_patrimoines_culturels_immat_id = PCI.id_type_patrimoines_culturels_immatériels
    LEFT JOIN Type_actions_culturelles_et_artistiques ACA ON VI.f_type_actions_culturelles_et_artistiques_id = ACA.id_type_actions_culturelles_artistiques
    LEFT JOIN Type_operateurs_des_oeuvres_esprit OE ON VI.f_type_operateurs_des_oeuvres_esprit_id = OE.id_type_operateurs_oeuvres_esprit
    LEFT JOIN Type_de_groupes_culturels GC ON VI.f_type_de_groupes_culturels_id = GC.id_type_groupes_culturels
    LEFT JOIN Type_de_manifestations_culturelles MC ON VI.f_type_de_manifestations_culturelles_id = MC.id_type_manifestations_culturelles
    
    LEFT JOIN Trimestre TRIM ON VI.f_trimestre_id=TRIM.id_trimestre
    LEFT JOIN Etat_des_ouvrages TDO ON VI.f_etat_des_ouvrages_id=TDO.id_etat_des_ouvrages
    LEFT JOIN Type_abonnement TABO ON VI.f_type_abonnement_id=TABO.id_type_abonnnement
    LEFT JOIN Type_suivi TPSU ON VI.f_type_suivi_id=TPSU.id_type_suivi
    LEFT JOIN Type_de_vulnerabilite  TVUL ON VI.f_type_de_vulnerabilite_id=TVUL.id_type_de_vulnerabilite
    LEFT JOIN Type_de_prise_charge TPCH ON VI.f_type_de_prise_charge_id=TPCH.id_type_de_prise_charge
    LEFT JOIN Niveau NIVE ON VI.f_niveau_id=NIVE.id_niveau
    """

    cursor.execute(query)
    rows = cursor.fetchall()

    df = pd.DataFrame(rows, columns=[
        "ID", "Région", "Département", "Sous-préfecture", "Indicateur", "Valeur Indicateur", "Année de collecte", "Sexe",
        "Groupe d'âge", "Age", "Cycle scolaire", "Niveau préscolaire", "Niveau primaire", "Niveau Secondaire 1er cycle",
        "Niveau Secondaire 2nd cycle", "Niveau Technique", "Niveau Supérieur", "Niveau Professionnel", "Type d'examen",
        "Infrastructures sanitaires", "Lieu d'accouchement", "État vaccinal", "Types de vaccination", "Pathologie",
        "Tranche d'âge", "Maladies du PEV", "Maladies infectieuses","Infectieuses respiratoire", "Maladies IST", "Type de maladie", "Activités IEC",
        "Services médicaux", "Type d'infrastructures sportives", "Disciplines sportives", "Type d'infrastructures culturelles",
        "Type de patrimoines culturels immatériels", "Type d'actions culturelles et artistiques", "Type d'opérateurs des œuvres d'esprit",
        "Type de groupes culturels", "Type de manifestations culturelles","Trimestre","Etat des ouvrages","Type d'abonnement",
        "Type de suivi","Type de vulnerabilité","Type de prise en charge","Niveau"
    ])

    conn.close()
    return df





def insert_into_valeur_indicateur_libelle():
    conn = cf.create_connection()
    cursor = conn.cursor()

    # Sélectionner les données à insérer
    query_select = """
    SELECT 
        VI.id,
        R.nom_region,
        D.nom_departement,
        SP.nom_sousprefecture,
        I.nom_indicateur,
        VI.Valeur,
        VI.Annee,
        S.sexe,
        GA.groupe_age,
        A.age,
        C.nom_cycle,
        NP.nom_prescolaire,
        N1C.nom_primaire,
        NS1C.nom_secondaire_1er_cycle,
        NS2C.nom_secondaire_2nd_cycle,
        NT.nom_technique,
        NS.nom_superieur,
        NP2.nom_professionnel,  -- Changé 'NP' en 'NP2' pour Niveau_Professionnel
        TE.nom_type_examen,
        SIS.nom_infrastructures_sanitaires,
        LA.nom_lieu_accouchement,
        EV.nom_etat_vaccinal,
        TV.nom_types_de_vaccination,
        P.nom_pathologie,
        TA.nom_tranche_age,
        MP.nom_maladies_du_pev,
        MI.nom_maladies_infectieuses,
        IRES.nom_infectieuses_respiratoire,
        IST.nom_maladies_ist,
        TM.nom_type_de_maladie,
        AI.nom_activites_iec,
        SM.nom_service_medicaux,
        TIS.nom_type_infrastructures_sportives,
        DS.nom_disciplines_sportives,
        TIC.nom_type_infrastructures_culturelles,
        PCI.nom_type_patrimoines_culturels_immatériels,
        ACA.nom_type_actions_culturelles_artistiques,
        OE.nom_type_operateurs_oeuvres_esprit,
        GC.nom_type_groupes_culturels,
        MC.nom_type_manifestations_culturelles,
        TRIM.nom_trimestre,
        TDO.nom_etat_des_ouvrages,
        TABO.nom_type_abonnnement,
        TPSU.nom_type_suivi,
        TVUL.nom_type_de_vulnerabilite,
        TPCH.nom_type_de_prise_charge,
        NIVE.nom_niveau
    FROM ValeursIndicateurs VI
    LEFT JOIN Region R ON VI.f_region_id = R.region_id
    LEFT JOIN Departement D ON VI.f_departement_id = D.departement_id
    LEFT JOIN SousPrefectures SP ON VI.f_sous_prefecture_id = SP.sousprefect_id
    LEFT JOIN Indicateur I ON VI.f_indicateur_id = I.indicateur_id
    LEFT JOIN Sexe S ON VI.f_sexe_id = S.sexe_id
    LEFT JOIN GroupeAge GA ON VI.f_grp_age_id = GA.grp_age_id
    LEFT JOIN Age A ON VI.f_age_id = A.age_id
    LEFT JOIN Cycle C ON VI.f_cycle_id = C.id_cycle
    LEFT JOIN Niveau_Prescolaire NP ON VI.f_niveau_prescolaire_id = NP.niv_prescolaire_id
    LEFT JOIN Niveau_Primaire N1C ON VI.f_niveau_primaire_id = N1C.niv_primaire_id
    LEFT JOIN Niveau_Secondaire_1er_cycle NS1C ON VI.f_niveau_secondaire_1er_cycle_id = NS1C.niv_secondaire_1er_cycle_id
    LEFT JOIN Niveau_Secondaire_2nd_cycle NS2C ON VI.f_niveau_secondaire_2nd_cycle_id = NS2C.niv_secondaire_2nd_cycle_id
    LEFT JOIN Niveau_Technique NT ON VI.f_niveau_technique_id = NT.niv_technique_id
    LEFT JOIN Niveau_Superieur NS ON VI.f_niveau_superieur_id = NS.niv_superieur_id
    LEFT JOIN Niveau_Professionnel NP2 ON VI.f_niveau_professionnel_id = NP2.niv_professionnel_id
    LEFT JOIN Type_examen TE ON VI.f_type_examen_id = TE.id_type_examen
    LEFT JOIN Infrastructures_sanitaires SIS ON VI.f_infrastructures_sanitaires_id = SIS.id_infrastructures_sanitaires
    LEFT JOIN Lieu_accouchement LA ON VI.f_lieu_accouchement_id = LA.id_lieu_accouchement
    LEFT JOIN Etat_vaccinal EV ON VI.f_etat_vaccinal_id = EV.id_etat_vaccinal
    LEFT JOIN Types_de_vaccination TV ON VI.f_types_de_vaccination_id = TV.id_types_de_vaccination
    LEFT JOIN Pathologie P ON VI.f_pathologie_id = P.id_pathologie
    LEFT JOIN Tranche_age TA ON VI.f_tranche_age_id = TA.id_tranche_age
    LEFT JOIN Maladies_du_PEV MP ON VI.f_maladies_du_pev_id = MP.id_maladies_du_pev
    LEFT JOIN Maladies_infectieuses MI ON VI.f_maladies_infectieuses_id = MI.id_maladies_infectieuses
    LEFT JOIN Infection_respiratoire IRES ON VI.f_infectieuses_respiratoire_id=IRES.id_infectieuses_respiratoire
    LEFT JOIN Maladies_IST IST ON VI.f_maladies_ist_id = IST.id_maladies_ist
    LEFT JOIN Type_de_Maladie TM ON VI.f_type_de_maladie_id = TM.id_type_de_maladie
    LEFT JOIN Activites_IEC AI ON VI.f_activites_iec_id = AI.id_activites_iec
    LEFT JOIN Service_Medicaux SM ON VI.f_service_medicaux_id = SM.id_service_medicaux
    LEFT JOIN Type_infrastructures_ou_organisations_sportives TIS ON VI.f_type_infrastructures_ou_organisations_sportives_id = TIS.id_type_infrastructures_sportives
    LEFT JOIN Disciplines_sportives DS ON VI.f_disciplines_sportives_id = DS.id_disciplines_sportives
    LEFT JOIN Type_infrastructures_culturelles TIC ON VI.f_type_infrastructures_culturelles_id = TIC.id_type_infrastructures_culturelles
    LEFT JOIN Type_de_Patrimoines_culturels_immatériels PCI ON VI.f_type_de_patrimoines_culturels_immat_id = PCI.id_type_patrimoines_culturels_immatériels
    LEFT JOIN Type_actions_culturelles_et_artistiques ACA ON VI.f_type_actions_culturelles_et_artistiques_id = ACA.id_type_actions_culturelles_artistiques
    LEFT JOIN Type_operateurs_des_oeuvres_esprit OE ON VI.f_type_operateurs_des_oeuvres_esprit_id = OE.id_type_operateurs_oeuvres_esprit
    LEFT JOIN Type_de_groupes_culturels GC ON VI.f_type_de_groupes_culturels_id = GC.id_type_groupes_culturels
    LEFT JOIN Type_de_manifestations_culturelles MC ON VI.f_type_de_manifestations_culturelles_id = MC.id_type_manifestations_culturelles
    LEFT JOIN Trimestre TRIM ON VI.f_trimestre_id=TRIM.id_trimestre
    LEFT JOIN Etat_des_ouvrages TDO ON VI.f_etat_des_ouvrages_id=TDO.id_etat_des_ouvrages
    LEFT JOIN Type_abonnement TABO ON VI.f_type_abonnement_id=TABO.id_type_abonnnement
    LEFT JOIN Type_suivi TPSU ON VI.f_type_suivi_id=TPSU.id_type_suivi
    LEFT JOIN Type_de_vulnerabilite  TVUL ON VI.f_type_de_vulnerabilite_id=TVUL.id_type_de_vulnerabilite
    LEFT JOIN Type_de_prise_charge TPCH ON VI.f_type_de_prise_charge_id=TPCH.id_type_de_prise_charge
    LEFT JOIN Niveau NIVE ON VI.f_niveau_id=NIVE.id_niveau
    """

    cursor.execute(query_select)
    rows = cursor.fetchall()

    # Insérer les données dans la nouvelle table
    query_insert = """
    INSERT INTO valeur_indicateur_libelle (
        id, nom_region, nom_departement, nom_sousprefecture, nom_indicateur, Valeur, Annee, sexe, groupe_age, age,
        nom_cycle, nom_prescolaire, nom_primaire, nom_secondaire_1er_cycle, nom_secondaire_2nd_cycle, nom_technique,
        nom_superieur, nom_professionnel, nom_type_examen, nom_infrastructures_sanitaires, nom_lieu_accouchement,
        nom_etat_vaccinal, nom_types_de_vaccination, nom_pathologie, nom_tranche_age, nom_maladies_du_pev,
        nom_maladies_infectieuses,nom_infectieuses_respiratoire ,nom_maladies_ist, nom_type_de_maladie, nom_activites_iec, nom_service_medicaux,
        nom_type_infrastructures_sportives, nom_disciplines_sportives, nom_type_infrastructures_culturelles,
        nom_type_patrimoines_culturels_immatériels, nom_type_actions_culturelles_artistiques, nom_type_operateurs_oeuvres_esprit,
        nom_type_groupes_culturels, nom_type_manifestations_culturelles, nom_trimestre, nom_etat_des_ouvrages,
        nom_type_abonnnement, nom_type_suivi, nom_type_de_vulnerabilite, nom_type_de_prise_charge, nom_niveau
    ) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s)
    ON DUPLICATE KEY UPDATE
        id = VALUES(id)
      
    """
    for row in rows:
        # Create a tuple with all values, including the id
        values = (row[0],) + row[1:]  # Add id at the beginning

        # Check if the row exists more efficiently
        cursor.execute("SELECT 1 FROM valeur_indicateur_libelle WHERE id = %s LIMIT 1", (row[0],))
        exists = cursor.fetchone() is not None

        if not exists:
            cursor.execute(query_insert, values)

    conn.commit()
    cursor.close()
    conn.close()


import mysql.connector


def insert_rejet():
    try:
        conn = cf.create_connection()
        cursor = conn.cursor()

        # Sélectionner les données à insérer
        query_select = """
            SELECT * FROM valeur_indicateur_libelle WHERE statut = 'Rejeté'
        """
        cursor.execute(query_select)
        rows = cursor.fetchall()

        # Générer dynamiquement la liste des colonnes et des valeurs
        columns = ', '.join([desc[0] for desc in cursor.description])
        placeholders = ', '.join(['%s'] * len(cursor.description))

        # Construire la requête d'insertion
        query_insert = f"""
            INSERT INTO valeur_rejet ({columns}) VALUES ({placeholders})
            ON DUPLICATE KEY UPDATE 
            {', '.join([f"{desc[0]} = VALUES({desc[0]})" for desc in cursor.description if desc[0] != 'id'])}
        """

        for row in rows:
            cursor.execute(query_insert, row)

        conn.commit()
    except mysql.connector.Error as err:
        print(f"Erreur lors de l'insertion : {err}")
    finally:
        cursor.close()
        conn.close()


insert_into_valeur_indicateur_libelle()
insert_rejet()





