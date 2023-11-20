import streamlit as st
import requests
import xml.etree.ElementTree as ET

# Inicializar el estado de la aplicación
if 'state' not in st.session_state:
    st.session_state.state = {
        'app_id': 'TPLJ58-T88JA64PR4',
        'opcion': None,
        'input_expr': None,
        'paso_a_paso': False,
        'pregunta': None,
    }

def calcular_integral_paso_a_paso():
    app_id = st.session_state.state['app_id']
    input_expr = st.session_state.state['input_expr']

    # La URL de la API de Wolfram Alpha
    url = 'http://api.wolframalpha.com/v2/query'

    # Los parámetros de la consulta
    params = {
        'appid': app_id,
        'input': input_expr,
        'output': 'xml'
    }

    # Enviar la consulta a la API de Wolfram Alpha
    response = requests.get(url, params=params)

    # Analizar la respuesta de la API
    root = ET.fromstring(response.content)
    pod = root.find('.//pod[@id="IndefiniteIntegral"]')
    subpod = pod.find('.//subpod')
    output_text = subpod.find('.//plaintext').text

    # Presentar la solución al usuario
    st.write(f"Expresión ingresada: {input_expr}")
    st.markdown("### Paso a paso:")
    st.latex(output_text)  # Muestra la salida en notación matemática LaTeX


def main():
    # Menú de opciones
    st.title("La Callatrex")
    opcion = st.sidebar.selectbox("Selecciona una opción:", ["Calcular integral", "Responder pregunta", "Salir"], key="menu_option")

    if opcion == "Calcular integral":
        st.session_state.state['opcion'] = opcion
        st.session_state.state['input_expr'] = st.text_input("Ingrese la expresión matemática:")
        st.session_state.state['paso_a_paso'] = st.checkbox("¿Quieres ver el paso a paso?")

        if st.button("Calcular"):
            calcular_integral_paso_a_paso()

    elif opcion == "Responder pregunta":
        st.session_state.state['opcion'] = opcion
        st.session_state.state['pregunta'] = st.text_input("Ingrese su pregunta:")
        if st.button("Responder"):
            st.write("Respuesta: Esta función aún no está implementada.")

    elif opcion == "Salir":
        st.write("¡Hasta luego!")

if __name__ == "__main__":
    main()






# import streamlit as st
# import requests
# import xml.etree.ElementTree as ET

# # Inicializar el estado de la aplicación
# if 'state' not in st.session_state:
#     st.session_state.state = {
#         'app_id': 'TPLJ58-T88JA64PR4',
#         'opcion': None,
#         'input_expr': None,
#         'paso_a_paso': False,
#         'pregunta': None,
#     }

# def calcular_integral_paso_a_paso():
#     app_id = st.session_state.state['app_id']
#     input_expr = st.session_state.state['input_expr']

#     # La URL de la API de Wolfram Alpha
#     url = 'http://api.wolframalpha.com/v2/query'

#     # Los parámetros de la consulta
#     params = {
#         'appid': app_id,
#         'input': input_expr,
#         'output': 'xml'
#     }

#     # Enviar la consulta a la API de Wolfram Alpha
#     response = requests.get(url, params=params)

#     # Analizar la respuesta de la API
#     root = ET.fromstring(response.content)
#     pod = root.find('.//pod[@id="IndefiniteIntegral"]')
#     subpod = pod.find('.//subpod')
#     output_text = subpod.find('.//plaintext').text

#     # Extraer y mostrar pasos detallados
#     steps = root.findall('.//step')
#     for step in steps:
#         st.write(step.find('.//plaintext').text)

#     # Presentar la solución al usuario
#     st.latex(output_text)  # Muestra la salida en notación matemática LaTeX

# def main():
#     # Menú de opciones
#     st.title("Calculadora de Integrales")
#     opcion = st.sidebar.selectbox("Selecciona una opción:", ["




