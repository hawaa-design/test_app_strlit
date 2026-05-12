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