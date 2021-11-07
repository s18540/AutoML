import streamlit as st
import pickle
from datetime import datetime
startTime = datetime.now()
# import znanych nam bibliotek

filename = "model_szpital.sv"
model = pickle.load(open(filename,'rb'))
# otwieramy wcześniej wytrenowany model

# objawy = {0:"Kobieta",1:"Mężczyzna"}
# pclass_d = {0:"Pierwsza",1:"Druga", 2:"Trzecia"}
# embarked_d = {0:"Cherbourg", 1:"Queenstown", 2:"Southampton"}
# o ile wcześniej kodowaliśmy nasze zmienne, to teraz wprowadzamy etykiety z ich nazewnictwem
def main():

	st.set_page_config(page_title="Czy osoba charkteryzująca się poniższymi parametrami ma szanse na wyzdrowienie?")
	overview = st.container()
	center = st.container()
	prediction = st.container()

	st.image("./covid-skull.jpg")

	with overview:
		st.title("Czy osoba charkteryzująca się poniższymi parametrami ma szanse na wyzdrowienie?")

	with center:
		objawy_slider = st.slider("Objawy", value=1, min_value=1, max_value=5, step=1)
		wiek_slider = st.slider( "Wiek pacjenta (w latach)", min_value=1, max_value=100, step=1)
		choroby_slider = st.slider( "Liczba chorób współistniejących", min_value=0, max_value=5, step=1)
		wzrost_slider = st.slider( "Wzrost pacjenta (w cm)", min_value=30, max_value=215, step=1)

	data = [[objawy_slider, wiek_slider, choroby_slider, wzrost_slider]]
	survival = model.predict(data)
	s_confidence = model.predict_proba(data)

	with prediction:
		st.header("Czy dana osoba wyzdrowieje? {0}".format("Nie" if survival[0] == 1 else "Tak"))
		st.subheader("Pewność predykcji {0:.2f} %".format(s_confidence[0][survival][0] * 100))

if __name__ == "__main__":
    main()
st.caption("Created by s18540")