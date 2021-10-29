import streamlit as st
import streamlit as st
from transformers import pipeline

st.success('Aplikacja jest uruchomiona!')
st.title('Aplikacja do tłumaczenia tekstu z języka angielskiego na niemiecki')
st.header('Sposób działania aplikacji')
st.write('Aplikacja wykorzystuje model T5, który został wstępnie przeszkolony tylko na zbiorze danych wielozadaniowych (w tym WMT), ale mimo to zapewnia imponujące wyniki tłumaczenia.')
st.header('Instrukcja obsługi aplikacji')
st.write('Do pola poniżej wprowadź tekst w języku angielski i naciśnij przycisk "Tłumacz". Wynik w postaci tekstu w języku niemieckim otrzymasz poniżej.')

with st.form("my_form"):
    text_en = st.text_area(label="Wpisz proszę tekst w języku angielskim:")
    submitted = st.form_submit_button("Tłumacz")
    if submitted:
        if text_en:
            placeholder = st.empty()
            placeholder.empty()
            with st.spinner('Poczekaj proszę, tłumaczę Twój tekst...'):
                translator = pipeline("translation_en_to_de")
                result = translator(text_en)
            with placeholder.container():
                st.balloons()
                st.success('Udało się! Tekst w języku niemieckim znajdziesz poniżej:')
                value = result[0].get('translation_text')
                st.write(value) 
        else:
            st.error("Wprowadź tekst do tłumaczenia!")
st.caption("Created by s18540")
