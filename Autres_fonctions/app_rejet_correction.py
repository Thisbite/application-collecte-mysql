import streamlit as st
import mysql.connector
import Autres_fonctions.config as cf

st.markdown("""
    <style>
        .title-container {
            display: flex;
            justify-content: center;
            align-items: center;
            border: 4px solid orange;
            border-left-color: green;
            border-right-color:green;
            border-radius: 5px;
            padding: 10px;
            margin: 20px 0;
            background-color: white;
        }
        .title-text {
            font-size: 2.5rem;
            font-weight: bold;
            color: black;
        }
    </style>
    <div class="title-container">
        <h2 class="title-text">Formulaire de rejet </h2>
    </div>
""", unsafe_allow_html=True)


def remplacer_nulls(record):
    for key, value in record.items():
        if value is None:
            if isinstance(value, str):
                record[key] = ""
            elif isinstance(value, int) or isinstance(value, float):
                record[key] = 0
    return record


def afficher_questionnaire(id):
    conn =cf.create_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM valeur_indicateur_libelle WHERE id = %s", (id,))
    record = cursor.fetchone()
    cursor.close()
    conn.close()

    if record:
        record = remplacer_nulls(record)

    return record


# Utilisation dans votre application
id = st.number_input("ID du Questionnaire", min_value=1, step=1)

if st.button("Charger Questionnaire"):
    record = afficher_questionnaire(id)
    if record:
        st.write(record)
        commentaires = st.text_area("Commentaires de Rejet")

    else:
        st.error("Questionnaire non trouvé.")
