import streamlit as st
import mysql.connector
import config as cf


def update_and_delete_record(row):
    try:
        conn = cf.create_connection()
        cursor = conn.cursor()

        # Mettre à jour l'enregistrement dans la table valeur_indicateur_libelle
        query_update = f"""
            UPDATE valeur_indicateur_libelle 
            SET 
                nom_region = %s, nom_departement = %s, nom_sousprefecture = %s, 
                nom_indicateur = %s, Valeur = %s, Annee = %s, sexe = %s, 
                groupe_age = %s, age = %s, nom_cycle = %s, nom_prescolaire = %s, 
                nom_primaire = %s, nom_secondaire_1er_cycle = %s, nom_secondaire_2nd_cycle = %s, 
                nom_technique = %s, nom_superieur = %s, nom_professionnel = %s, 
                nom_type_examen = %s, nom_infrastructures_sanitaires = %s, 
                nom_lieu_accouchement = %s, nom_etat_vaccinal = %s, nom_types_de_vaccination = %s, 
                nom_pathologie = %s, nom_tranche_age = %s, nom_maladies_du_pev = %s, 
                nom_maladies_infectieuses = %s, nom_infectieuses_respiratoire = %s, 
                nom_maladies_ist = %s, nom_type_de_maladie = %s, nom_activites_iec = %s, 
                nom_service_medicaux = %s, nom_type_infrastructures_sportives = %s, 
                nom_disciplines_sportives = %s, nom_type_infrastructures_culturelles = %s, 
                nom_type_patrimoines_culturels_immatériels = %s, 
                nom_type_actions_culturelles_artistiques = %s, nom_type_operateurs_oeuvres_esprit = %s, 
                nom_type_groupes_culturels = %s, nom_type_manifestations_culturelles = %s, 
                nom_trimestre = %s, nom_etat_des_ouvrages = %s, nom_type_abonnnement = %s, 
                nom_type_suivi = %s, nom_type_de_vulnerabilite = %s, 
                nom_type_de_prise_charge = %s, nom_niveau = %s, statut =%s, 
                commentaires = %s, date_rejet = %s, Agent = %s
            WHERE id = %s
        """

        cursor.execute(query_update, (*row[1:], row[0]))

        # Supprimer l'enregistrement de la table valeur_rejet
        query_delete = "DELETE FROM valeur_rejet WHERE id = %s"
        cursor.execute(query_delete, (row[0],))

        conn.commit()
    except mysql.connector.Error as err:
        st.error(f"Erreur lors de la mise à jour et suppression : {err}")
    finally:
        cursor.close()
        conn.close()


def main():
    conn = cf.create_connection()
    cursor = conn.cursor()

    # Sélectionner les enregistrements dans valeur_rejet
    query_select = "SELECT * FROM valeur_rejet"
    cursor.execute(query_select)
    rows = cursor.fetchall()

    # Parcourir les enregistrements et créer un formulaire pour chacun
    for row in rows:
        with st.expander(f"ID: {row[0]} - {row[4]}"):
            st.write("Modifier les informations ci-dessous:")

            # Créer un formulaire pour chaque champ
            form = st.form(key=str(row[0]))
            labels = {
                'nom_region': 'Région',
                'nom_departement': 'Département',
                'nom_sousprefecture': 'Sous-préfecture',
                'nom_indicateur': 'Indicateur',
                'Valeur': 'Valeur indicateur',
                'Annee': 'Année de collecte',
                'sexe': 'Sexe',
                'groupe_age': 'Groupe d’âge',
                'age': 'Âge',
                'nom_cycle': 'Cycle éducatif',
                'nom_prescolaire': 'Niveau préscolaire',
                'nom_primaire': 'Niveau primaire',
                'nom_secondaire_1er_cycle': '1er cycle secondaire',
                'nom_secondaire_2nd_cycle': '2nd cycle secondaire',
                'nom_technique': 'Niveau technique',
                'nom_superieur': 'Niveau supérieur',
                'nom_professionnel': 'Niveau professionnel',
                'nom_type_examen': 'Type d’examen',
                'nom_infrastructures_sanitaires': 'Infrastructures sanitaires',
                'nom_lieu_accouchement': 'Lieu d’accouchement',
                'nom_etat_vaccinal': 'État vaccinal',
                'nom_types_de_vaccination': 'Types de vaccination',
                'nom_pathologie': 'Pathologie',
                'nom_tranche_age': 'Tranche d’âge',
                'nom_maladies_du_pev': 'Maladies du PEV',
                'nom_maladies_infectieuses': 'Maladies infectieuses',
                'nom_infectieuses_respiratoire': 'Maladies respiratoires infectieuses',
                'nom_maladies_ist': 'Maladies IST',
                'nom_type_de_maladie': 'Type de maladie',
                'nom_activites_iec': 'Activités IEC',
                'nom_service_medicaux': 'Services médicaux',
                'nom_type_infrastructures_sportives': 'Infrastructures sportives',
                'nom_disciplines_sportives': 'Disciplines sportives',
                'nom_type_infrastructures_culturelles': 'Infrastructures culturelles',
                'nom_type_patrimoines_culturels_immatériels': 'Patrimoines culturels immatériels',
                'nom_type_actions_culturelles_artistiques': 'Actions culturelles artistiques',
                'nom_type_operateurs_oeuvres_esprit': 'Opérateurs d’œuvres de l’esprit',
                'nom_type_groupes_culturels': 'Groupes culturels',
                'nom_type_manifestations_culturelles': 'Manifestations culturelles',
                'nom_trimestre': 'Trimestre',
                'nom_etat_des_ouvrages': 'État des ouvrages',
                'nom_type_abonnnement': 'Type d’abonnement',
                'nom_type_suivi': 'Type de suivi',
                'nom_type_de_vulnerabilite': 'Type de vulnérabilité',
                'nom_type_de_prise_charge': 'Type de prise en charge',
                'nom_niveau': 'Niveau',
                'date_rejet':'Date de rejet',
                'statut': 'Statut'
            }

            new_values = []

            for i, column in enumerate(cursor.description[1:], 1):  # Exclure l'ID
                column_name = column[0]
                label = labels.get(column_name,
                                   column_name)  # Utiliser le label personnalisé ou le nom de la colonne par défaut
                new_value = form.text_input(label, value=row[i])
                new_values.append(new_value)
            # Bouton "Achevé"
            if form.form_submit_button("Achevé"):
                update_and_delete_record((row[0], *new_values))
                st.success(f"Correction du questionnaire ID {row[0]}  effectué avec succès")

    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()







