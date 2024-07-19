#1 IMPORTATION DES LIBRAIRIES
#2 DESCRIPTION DU POJET
#3 CHARGEMENT DU MODELE
#4 DEFINITION DE LA FONCTION D'INTERFERENCE(PERMET DE FAIRE LA PREDICTION)
#5 SAISIE DES INFORMATIONS
#6 CREATION DU BOUTON DE PREDICTION


#1 imporation des librairies
import streamlit as st
import numpy as np
import pandas as pd 
import pickle as pkl

#2 DESCRIPTION DU PROJET

st.title("PREDICTION DE LA PRESENCE DE DIABETE")



#3 CHARGEMENT DU MODELE

file = open("gr.pkl","rb")
model = pkl.load(file)
file.close()


#4 DEFINITION DE LA FONCTION D'INTERFERENCE
#image
import streamlit as st

def interference(Glucose, BMI, Age,DiabetesPedigreeFunction):
    
    if model is not None:
        df = np.array([Glucose, BMI, Age,DiabetesPedigreeFunction])
        try:
            pred = model.predict(df.reshape(1, -1))
            return pred
        except AttributeError as e:
            st.error(f"Erreur de prédiction: {e}")
            return None
    else:
        st.error("Modèle non chargé correctement.")
        return None
    
#5 SAISIE DES INFORMATIONS DU CLIENT

st.sidebar.header("PREDICTION")

st.sidebar.write('Entrez les informations du client')


Glucose =st.sidebar.number_input(label="Taux de glucose")

BMI= st.sidebar.number_input(label="Indice de masse corporelle(BMI)")

Age = st.sidebar.number_input(label="Age du patient")

DiabetesPedigreeFunction = st.sidebar.number_input(label='Fonction pédigrée du diabete')

#CHARGEMENT DE LA BD
#data = pd.read_csv("C:/Users/HP/Documents/DATASCIENCE/base de donnees/diabetes.csv")


#st.dataframe(data[['Glucose','BMI','Age','DiabetesPedigreeFunction','Outcome']])
st.write("Le modèle utilisé pour le jeux de donnée DIABETE est le RandomForest.")
st.write("Il nous permet de prédire si le patient est malade (1) ou non(0) en entrant les informations correctes.")
st.image("C:/Users/HP/Downloads/The Power of Empathy in the Patient-Doctor Relationship_ Enhancing Healthcare Experiences.jpeg")
#6 CREATION DU BOUTON DE PREDICTION

if st.sidebar.button('predict'):
    result_pred = interference(DiabetesPedigreeFunction, Age, BMI, Glucose)
    if result_pred[0]==0:
        st.success("Le patient n'est pas diabétique ",icon="✅")
        st.image('download (1).jpeg', caption='BONNE SANTE',width = 180)

    elif result_pred[0]==1:
        st.warning("Malheureusement vous êtes diabétiques ",icon="🔥")
        st.image("C:/Users/HP/Desktop/diabete/triste.jpeg", caption='vous êtes diabétiques',width=185)





 
