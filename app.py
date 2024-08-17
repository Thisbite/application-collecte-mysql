import streamlit as st
import app_form as af
import config as cf
import pandas as pd
import app_modifier as am
conn=cf.create_connection()
st.set_page_config(page_title="Formulaire de collecte", page_icon="📊")

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

af.form()
#am.modifier()


