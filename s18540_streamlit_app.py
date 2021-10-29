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



# st.subheader('Zadanie do wykonania')
# st.write('Wykorzystaj Huggin Face do stworzenia swojej własnej aplikacji tłumaczącej tekst z języka angielskiego na język niemiecki. Zmodyfikuj powyższy kod dodając do niego kolejną opcję, tj. tłumaczenie tekstu. Informacje potrzebne do zmodyfikowania kodu znajdziesz na stronie Huggin Face - https://huggingface.co/transformers/usage.html')
# st.write('🐞 Dodaj właściwy tytuł do swojej aplikacji, może jakieś grafiki?')
# st.write('🐞 Dodaj krótką instrukcję i napisz do czego służy aplikacja')
# st.write('🐞 Wpłyń na user experience, dodaj informacje o ładowaniu, sukcesie, błędzie, itd.')
# st.write('🐞 Na końcu umieść swój numer indeksu')
# st.write('🐞 Stwórz nowe repozytorium na GitHub, dodaj do niego swoją aplikację, plik z wymaganiami (requirements.txt)')
# st.write('🐞 Udostępnij stworzoną przez siebie aplikację (https://share.streamlit.io) a link prześlij do prowadzącego')
