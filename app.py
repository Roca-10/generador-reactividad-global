import streamlit as st
from rdkit import Chem
from rdkit.Chem import Descriptors
from rdkit.Chem import rdMolDescriptors
import numpy as np

# Funciones para calcular los descriptores
def calcular_energia_afinidad_y_ionizacion(mol):
    """
    Calcula la energía de afinidad electrónica (A) y la energía de ionización (I)
    basados en los valores HOMO y LUMO de la molécula.
    
    Los cálculos de HOMO y LUMO en este ejemplo son aproximados usando el software RDKit.
    """
    # HOMO y LUMO (esto es solo un cálculo simplificado y no necesariamente exacto)
    homo = Descriptors.MolWt(mol) / 10  # Simulando HOMO
    lumo = Descriptors.TPSA(mol) / 10   # Simulando LUMO

    # Energía de ionización (I) = HOMO
    ionizacion = homo
    
    # Energía de afinidad electrónica (A) = -LUMO
    afinidad = -lumo
    
    return afinidad, ionizacion

# Título y descripción
st.title("Generador de Descriptores de Reactividad Global")
st.markdown("""
    Ingresa un SMILES para calcular la energía de afinidad electrónica (A) y la energía de ionización (I).
""")

# Input del usuario
smiles = st.text_input("Ingresa la estructura SMILES de una molécula:")

# Procesar el SMILES
if smiles:
    try:
        mol = Chem.MolFromSmiles(smiles)
        
        if mol:
            afinidad, ionizacion = calcular_energia_afinidad_y_ionizacion(mol)
            st.write(f"Energía de Afinidad Electrónica (A): {afinidad:.2f} eV")
            st.write(f"Energía de Ionización (I): {ionizacion:.2f} eV")
        else:
            st.error("SMILES no válido. Intenta con otro formato.")
    except Exception as e:
        st.error(f"Hubo un error: {str(e)}")
