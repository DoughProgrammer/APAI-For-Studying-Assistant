#imprting streamlit

import streamlit as st
import google.generativeai as genai
#1. app titles

st.title('🤖 Studying AI assistant')

#2. Creating colums

col1, col2 = st.columns(2)

with col1:
    subjects = ['English', 'Arabic', '➕Math', '💻Digital Design',
                '🔬Science', '☪️Islamic Relgion','🥐French', '🍔German']
    subject = st.selectbox('📓Choose Subject:', subjects)
    tones = ['🎓Professional', '🏫Student']
    tone = st.selectbox('😇Choose Tone:', tones)

with col2:
    details = ['Brief', 'Meduim', 'Detailed']
    detail = st.selectbox ('📝Choose details level:', details)

    edu_levels = ['Elementary', 'Jonior', 'Senior']
    edu_level = st.selectbox('🧑‍🎓 Choose education level:', edu_levels)

st.divider()

#Taking user's question

question = st.text_area('Enter your question...')

if st.button('Enter📩'):

    #1. Accessing Gemini
    genai.configure(api_key='AIzaSyCL00b41P9nAubFcA_cq1DPc_QnssdF34I')

    #2. Choosing the model
    model = genai.GenerativeModel(model_name = 'gemini-3-flash-preview')

    #3. Giving Request
    prompt = f'''
    I am a student in {edu_level} stage and I am studying {subject}.
    So, I need you to help me with the question:
    {question} with a {tone} and {detail} level of detail
    '''
    #4. Getting The Answer
    with st.spinner('✨Generating...'):
        response = model.generate_content(prompt)
        st.write(response.text)