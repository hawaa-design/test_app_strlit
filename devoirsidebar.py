import streamlit as st

st.sidebar.title("Menu")
choix = st.sidebar.radio("Choix", ["Accueil", "Liste étudiants"])

etudiants = [
    {"nom": "Abakar", "prenom": "Rania", "note": 14},
    {"nom": "Ali", "prenom": "Abakar", "note": 8},
    {"nom": "Ahmed", "prenom": "Ali", "note": 12},
    {"nom": "David", "prenom": "Monzoh", "note": 9},
    {"nom": "Abdoulaye", "prenom": "Hawa", "note": 17},
    {"nom": "Farid", "prenom": "Baker", "note": 5},
]

if choix == "Accueil":
    st.header("Bienvenu à ISMAGI")
    st.write("Application des admis à ISMAGI.")

elif choix == "Liste étudiants":
    st.header("Liste des etudiants")
    st.write("Ceci est la page de la liste des etudiants.")
    tab1, tab2 = st.tabs(["Liste des admis", "Liste des exclus"])

    admis = [e for e in etudiants if e["note"] >= 10]
    exclus = [e for e in etudiants if e["note"] < 10]

    with tab1:
        st.subheader("Liste des admis")
        st.table(admis)

    with tab2:
        st.subheader("Liste des exclus")
        st.table(exclus)

import streamlit as st
import pandas as pd

# Titre de l'application
st.title("Formulaire Étudiant")

# Formulaire
with st.form("form_etudiant"):

    nom = st.text_input("Nom")
    prenom = st.text_input("Prénom")
    age = st.number_input("Âge", min_value=15, max_value=100, step=1)
    sexe = st.selectbox("Sexe", ["Homme", "Femme", "Autre"])
    filiere = st.selectbox(
        "Filière",
        ["Informatique", "Mathématiques", "Physique", "Chimie"]
    )
    email = st.text_input("Email")
    date_naissance = st.date_input("Date de naissance")

    submitted = st.form_submit_button("Enregistrer")

# Traitement après soumission
if submitted:

    if nom and prenom and email:
        st.success("Étudiant enregistré avec succès !")

        # Création des données
        data = {
            "Nom": [nom],
            "Prénom": [prenom],
            "Âge": [age],
            "Sexe": [sexe],
            "Filière": [filiere],
            "Email": [email],
            "Date de naissance": [date_naissance]
        }

        df = pd.DataFrame(data)

        # Affichage des données
        st.subheader("Informations enregistrées")
        st.dataframe(df)

    else:
        st.error("Veuillez remplir tous les champs obligatoires.")