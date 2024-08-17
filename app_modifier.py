import config as cf
import streamlit as st
import mysql.connector



import streamlit as st
import app_form as af


conn=cf.create_connection()
st.set_page_config(page_title="Formulaire de rejet", page_icon="📊")

st.markdown("""
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
                <style>

                    .custom-bold-text {
                        font-weight: bold;
                        color: black;
                        font-size: 45px; 
                    }
                    .stButton button {
                    background-color: orange;
                    color: white;
                    display: block;
                    margin: 0 auto;
                    font-weight: bold;
                     }

                </style>
            """, unsafe_allow_html=True)

# Couleur  pour css input text label
st.markdown("""
                <style>
                .stTextInput > label {
                font-size:150%; 
                font-weight:bold; 
                color:white; 
                background:linear-gradient(to bottom, #cccccc 0%, #999999 100%);
                border: 2px;
                border-radius: 3px;
                } 
                </style>
                """, unsafe_allow_html=True)

# La forme pour les labels
st.markdown("""
            <style>
            div[data-baseweb="base-input"]{ 

            border: 2px;
            border-radius: 3px;
            }

            input[class]{
            font-weight: bold;
            font-size:120%;
            color: black;
            }
            </style>
            """, unsafe_allow_html=True)

st.markdown("""
                <style>

                .stSelectbox label {
                  font-size:150%; 
                font-weight:bold; 
                color:blue; 
                background:linear-gradient(to bottom, #cccccc 0%, #999999 100%);
            border: 2px;
                border-radius: 3px;
                }
                </style>
                """, unsafe_allow_html=True)

# Pour le formulaire css
st.markdown("""
            <style>
            .stForm  {
                font-size: 1.8rem;
                font-weight: bold;
                color: white;
                background: linear-gradient(to bottom, #3399ff 0%, #00ffff 90%);
                border: 2px solid;
                border-radius: 3px;
            }
            </style>
            """, unsafe_allow_html=True)

# Pour les paragraphes
st.markdown(
    """
    <style>
    .custom-label {
        font-size: 1.2rem;
        color: blue;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Couleur du label number
st.markdown("""
        <style>
        .stNumberInput label {
             color: blue;
            font-weight: bold;
            font-size: 1.5rem;
            text-align: center;
             background:linear-gradient(to bottom, #cccccc 0%, #999999 100%);
                border: 2px;
                border-radius: 3px;
        }

        }
        </style>
        """, unsafe_allow_html=True)

st.markdown("""
        <style>
        .stTextInput label {
              color: blue;
              font-weight: bold;
              font-size: 1.5rem;
              text-align: center;
        }
        .stTextInput label {


             font-size: 45px; 

        }
        </style>
        """, unsafe_allow_html=True)

def modifier_valeur_indicateur_libelle(id, nom_region=None, nom_departement=None, nom_sousprefecture=None,
                                      nom_indicateur=None,
                                      Valeur=None, Annee=None, sexe=None, groupe_age=None, age=None, nom_cycle=None,
                                      nom_prescolaire=None, nom_primaire=None, nom_secondaire_1er_cycle=None,
                                      nom_secondaire_2nd_cycle=None,
                                      nom_technique=None, nom_superieur=None, nom_professionnel=None,
                                      nom_type_examen=None,
                                      nom_infrastructures_sanitaires=None, nom_lieu_accouchement=None,
                                      nom_etat_vaccinal=None,
                                      nom_types_de_vaccination=None, nom_pathologie=None, nom_tranche_age=None,
                                      nom_maladies_du_pev=None,
                                      nom_maladies_infectieuses=None, nom_infectieuses_respiratoire=None,
                                      nom_maladies_ist=None,
                                      nom_type_de_maladie=None, nom_activites_iec=None, nom_service_medicaux=None,
                                      nom_type_infrastructures_sportives=None, nom_disciplines_sportives=None,
                                      nom_type_infrastructures_culturelles=None,
                                      nom_type_patrimoines_culturels_immatériels=None,
                                      nom_type_actions_culturelles_artistiques=None,
                                      nom_type_operateurs_oeuvres_esprit=None,
                                      nom_type_groupes_culturels=None, nom_type_manifestations_culturelles=None,
                                      nom_trimestre=None,
                                      nom_etat_des_ouvrages=None, nom_type_abonnnement=None, nom_type_suivi=None,
                                      nom_type_de_vulnerabilite=None,
                                      nom_type_de_prise_charge=None, nom_niveau=None):
    try:
        # Connexion à la base de données
        conn = cf.create_connection()
        cursor = conn.cursor()

        # Création de la requête SQL
        query = """
            UPDATE valeur_indicateur_libelle
            SET nom_region = %s, nom_departement = %s, nom_sousprefecture = %s, nom_indicateur = %s,
                Valeur = %s, Annee = %s, sexe = %s, groupe_age = %s, age = %s, nom_cycle = %s,
                nom_prescolaire = %s, nom_primaire = %s, nom_secondaire_1er_cycle = %s,
                nom_secondaire_2nd_cycle = %s, nom_technique = %s, nom_superieur = %s,
                nom_professionnel = %s, nom_type_examen = %s, nom_infrastructures_sanitaires = %s,
                nom_lieu_accouchement = %s, nom_etat_vaccinal = %s, nom_types_de_vaccination = %s,
                nom_pathologie = %s, nom_tranche_age = %s, nom_maladies_du_pev = %s,
                nom_maladies_infectieuses = %s, nom_infectieuses_respiratoire = %s, nom_maladies_ist = %s,
                nom_type_de_maladie = %s, nom_activites_iec = %s, nom_service_medicaux = %s,
                nom_type_infrastructures_sportives = %s, nom_disciplines_sportives = %s,
                nom_type_infrastructures_culturelles = %s, nom_type_patrimoines_culturels_immatériels = %s,
                nom_type_actions_culturelles_artistiques = %s, nom_type_operateurs_oeuvres_esprit = %s,
                nom_type_groupes_culturels = %s, nom_type_manifestations_culturelles = %s,
                nom_trimestre = %s, nom_etat_des_ouvrages = %s, nom_type_abonnnement = %s,
                nom_type_suivi = %s, nom_type_de_vulnerabilite = %s, nom_type_de_prise_charge = %s,
                nom_niveau = %s
            WHERE id = %s
            """  # Exécution de la requête
        cursor.execute(query, (
            nom_region, nom_departement, nom_sousprefecture, nom_indicateur, Valeur, Annee, sexe,
            groupe_age, age, nom_cycle, nom_prescolaire, nom_primaire, nom_secondaire_1er_cycle,
            nom_secondaire_2nd_cycle, nom_technique, nom_superieur, nom_professionnel, nom_type_examen,
            nom_infrastructures_sanitaires, nom_lieu_accouchement, nom_etat_vaccinal, nom_types_de_vaccination,
            nom_pathologie, nom_tranche_age, nom_maladies_du_pev, nom_maladies_infectieuses,
            nom_infectieuses_respiratoire, nom_maladies_ist, nom_type_de_maladie, nom_activites_iec,
            nom_service_medicaux, nom_type_infrastructures_sportives, nom_disciplines_sportives,
            nom_type_infrastructures_culturelles, nom_type_patrimoines_culturels_immatériels,
            nom_type_actions_culturelles_artistiques, nom_type_operateurs_oeuvres_esprit, nom_type_groupes_culturels,
            nom_type_manifestations_culturelles, nom_trimestre, nom_etat_des_ouvrages, nom_type_abonnnement,
            nom_type_suivi, nom_type_de_vulnerabilite, nom_type_de_prise_charge, nom_niveau, id
        ))

        # Validation de la transaction
        conn.commit()
        cursor.close()
        conn.close()

        print("L'enregistrement a été mis à jour avec succès.")
    except mysql.connector.Error as err:
        print(f"Erreur : {err}")


def modifier():
    st.markdown("<h2 class='text-center text-primary custom-bold-text'>Formulaire de rejet</h2>",
                unsafe_allow_html=True)
    id = st.number_input("ID de l'enregistrement", min_value=1, step=1)
    if id:
        with st.form("modification"):
            try:
                # Connexion à la base de données pour obtenir les valeurs existantes
                conn = cf.create_connection()
                cursor = conn.cursor(dictionary=True)
                cursor.execute("SELECT * FROM valeur_indicateur_libelle WHERE id = %s", (id,))
                record = cursor.fetchone()
                cursor.close()
                conn.close()

                if record:
                    # Disposer les champs sur 4 colonnes
                    cols = st.columns(4)

                    with cols[0]:
                        nom_region = st.text_input("Nom de la région", value=record['nom_region'])
                        nom_departement = st.text_input("Nom du département", value=record['nom_departement'])
                        nom_sousprefecture = st.text_input("Nom de la sous-préfecture",
                                                           value=record['nom_sousprefecture'])
                        nom_indicateur = st.text_input("Nom de l'indicateur", value=record['nom_indicateur'])
                        Valeur = st.number_input("Valeur", value=float(record['Valeur']) if record['Valeur']
                        is not None else 0.0, format = "%.2f")

                        Annee = st.number_input("Année", value=int(record['Annee']) if record['Annee']
                        is not None else 2024)
                        sexe = st.text_input("Sexe", value=record['sexe'])
                        groupe_age = st.text_input("Groupe d'âge", value=record['groupe_age'])
                        age = st.number_input("Âge", value=int(record['age']) if record['age']
                        is not None else 0)
                        nom_cycle = st.text_input("Nom du cycle", value=record['nom_cycle'])
                        nom_prescolaire = st.text_input("Nom du préscolaire", value=record['nom_prescolaire'])
                        nom_primaire = st.text_input("Nom du primaire", value=record['nom_primaire'])
                        nom_secondaire_1er_cycle = st.text_input("Nom du secondaire 1er cycle",
                                                                 value=record['nom_secondaire_1er_cycle'])

                    with cols[1]:
                        nom_secondaire_2nd_cycle = st.text_input("Nom du secondaire 2nd cycle",
                                                                 value=record['nom_secondaire_2nd_cycle'])
                        nom_technique = st.text_input("Nom du technique", value=record['nom_technique'])
                        nom_superieur = st.text_input("Nom du supérieur", value=record['nom_superieur'])
                        nom_professionnel = st.text_input("Nom du professionnel", value=record['nom_professionnel'])
                        nom_type_examen = st.text_input("Nom du type d'examen", value=record['nom_type_examen'])
                        nom_infrastructures_sanitaires = st.text_input("Nom des infrastructures sanitaires",
                                                                       value=record['nom_infrastructures_sanitaires'])
                        nom_lieu_accouchement = st.text_input("Nom du lieu d'accouchement",
                                                              value=record['nom_lieu_accouchement'])
                        nom_etat_vaccinal = st.text_input("Nom de l'état vaccinal", value=record['nom_etat_vaccinal'])
                        nom_types_de_vaccination = st.text_input("Nom des types de vaccination",
                                                                 value=record['nom_types_de_vaccination'])
                        nom_pathologie = st.text_input("Nom de la pathologie", value=record['nom_pathologie'])
                        nom_tranche_age = st.text_input("Nom de la tranche d'âge", value=record['nom_tranche_age'])
                        nom_maladies_du_pev = st.text_input("Nom des maladies du PEV",
                                                            value=record['nom_maladies_du_pev'])

                    with cols[2]:
                        nom_maladies_infectieuses = st.text_input("Nom des maladies infectieuses",
                                                                  value=record['nom_maladies_infectieuses'])
                        nom_infectieuses_respiratoire = st.text_input("Nom des maladies infectieuses respiratoires",
                                                                      value=record['nom_infectieuses_respiratoire'])
                        nom_maladies_ist = st.text_input("Nom des maladies IST", value=record['nom_maladies_ist'])
                        nom_type_de_maladie = st.text_input("Nom du type de maladie",
                                                            value=record['nom_type_de_maladie'])
                        nom_activites_iec = st.text_input("Nom des activités IEC", value=record['nom_activites_iec'])
                        nom_service_medicaux = st.text_input("Nom du service médical",
                                                             value=record['nom_service_medicaux'])
                        nom_type_infrastructures_sportives = st.text_input("Nom du type d'infrastructures sportives",
                                                                           value=record[
                                                                               'nom_type_infrastructures_sportives'])
                        nom_disciplines_sportives = st.text_input("Nom des disciplines sportives",
                                                                  value=record['nom_disciplines_sportives'])
                        nom_type_infrastructures_culturelles = st.text_input(
                            "Nom du type d'infrastructures culturelles",
                            value=record['nom_type_infrastructures_culturelles'])
                        nom_type_patrimoines_culturels_immatériels = st.text_input(
                            "Nom du type de patrimoines culturels immatériels",
                            value=record['nom_type_patrimoines_culturels_immatériels'])
                        nom_type_actions_culturelles_artistiques = st.text_input(
                            "Nom du type d'actions culturelles artistiques",
                            value=record['nom_type_actions_culturelles_artistiques'])

                    with cols[3]:
                        nom_type_operateurs_oeuvres_esprit = st.text_input("Nom du type d'opérateurs d'œuvres d'esprit",
                                                                           value=record[
                                                                               'nom_type_operateurs_oeuvres_esprit'])
                        nom_type_groupes_culturels = st.text_input("Nom du type de groupes culturels",
                                                                   value=record['nom_type_groupes_culturels'])
                        nom_type_manifestations_culturelles = st.text_input("Nom du type de manifestations culturelles",
                                                                            value=record[
                                                                                'nom_type_manifestations_culturelles'])
                        nom_trimestre = st.text_input("Nom du trimestre", value=record['nom_trimestre'])
                        nom_etat_des_ouvrages = st.text_input("Nom de l'état des ouvrages",
                                                              value=record['nom_etat_des_ouvrages'])
                        nom_type_abonnnement = st.text_input("Nom du type d'abonnement",
                                                             value=record['nom_type_abonnnement'])
                        nom_type_suivi = st.text_input("Nom du type de suivi", value=record['nom_type_suivi'])
                        nom_type_de_vulnerabilite = st.text_input("Nom du type de vulnérabilité",
                                                                  value=record['nom_type_de_vulnerabilite'])
                        nom_type_de_prise_charge = st.text_input("Nom du type de prise en charge",
                                                                 value=record['nom_type_de_prise_charge'])
                        nom_niveau = st.text_input("Nom du niveau", value=record['nom_niveau'])

                    if st.form_submit_button("Mettre à jour"):
                        modifier_valeur_indicateur_libelle(
                            id, nom_region, nom_departement, nom_sousprefecture, nom_indicateur, Valeur, Annee,
                            sexe, groupe_age, age, nom_cycle, nom_prescolaire, nom_primaire, nom_secondaire_1er_cycle,
                            nom_secondaire_2nd_cycle, nom_technique, nom_superieur, nom_professionnel, nom_type_examen,
                            nom_infrastructures_sanitaires, nom_lieu_accouchement, nom_etat_vaccinal,
                            nom_types_de_vaccination, nom_pathologie, nom_tranche_age, nom_maladies_du_pev,
                            nom_maladies_infectieuses, nom_infectieuses_respiratoire, nom_maladies_ist,
                            nom_type_de_maladie,
                            nom_activites_iec, nom_service_medicaux, nom_type_infrastructures_sportives,
                            nom_disciplines_sportives,
                            nom_type_infrastructures_culturelles, nom_type_patrimoines_culturels_immatériels,
                            nom_type_actions_culturelles_artistiques, nom_type_operateurs_oeuvres_esprit,
                            nom_type_groupes_culturels,
                            nom_type_manifestations_culturelles, nom_trimestre, nom_etat_des_ouvrages,
                            nom_type_abonnnement,
                            nom_type_suivi, nom_type_de_vulnerabilite, nom_type_de_prise_charge, nom_niveau)
                        st.success("Enregistrement avec succès")

            except mysql.connector.Error as err:
                st.error(f"Erreur : {err}")
    else:
        st.error("Aucun enregistrement trouvé.")






modifier()





import pandas as pd
conn=cf.create_connection()
cursor=conn.cursor()
cursor.execute("SELECT * FROM valeur_indicateur_libelle")
df=cursor.fetchall()
df=pd.DataFrame(df)
st.dataframe(df)