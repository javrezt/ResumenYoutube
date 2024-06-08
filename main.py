import streamlit as st
import requests
import os

# Encabezado de la aplicación
st.header('Desplegando asistente para extraer insights artículos')

# Campo para recibir una consulta
query = st.text_area('Ingresa tu consulta y la información que quieres procesar:')

# Input de selección múltiple para escoger el lenguaje
language = st.selectbox('Seleccione el lenguaje', ('ENGLISH', 'SPANISH'))

# Guardar los valores en variables
if st.button('Consultar'):
    base_url = "https://api.dify.ai/v1"
    path = "/completion-messages"
    # Debes reemplazar esto con tu API key real
    my_secret = os.environ['DIFY_APP_SECRET']

    # Encabezados para la petición
    headers = {
        'Authorization': f'Bearer {my_secret}',
        'Content-Type': 'application/json'
    }

    # Datos a enviar en la petición
    data = {
        "inputs": {
            "query": query,
            "language": language
        },
        "response_mode": "blocking",
        "user": "CRDZ-LS-11"
    }

    # Realizar la petición POST
    response = requests.post(f'{base_url}{path}', json=data, headers=headers)

    # Mostrar la respuesta de la API
    if response.status_code == 200:
        st.success('Consulta enviada con éxito!')
        #st.json(response.json())
        result = response.json()
        st.markdown('### Resultado de la solicitud:')
        st.markdown(result['answer'])
    else:
        st.error('Error al enviar la consulta')
        print(response.content)
