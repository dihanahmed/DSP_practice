import streamlit as st
from person import Person
from api import call_api

st.title("My character comparision")

endpoint = 'https://swapi.dev/api/people/?format=json'

response= call_api(url=endpoint)
people_list = response.get('results')
st.json(people_list)

index1 = st.number_input('Type the index of the first character', format='%i', step=1, min_value=0, max_value=len(people_list))
index2 = st.number_input('Type the index of the second character', format='%i', step=1, min_value=0, max_value=len(people_list))

if st.button('Compare'):
    st.header("Age Comparison")
    st.text("this is for third commit")
    st.header(f"Character {index1}")
    st.header(f"Character {index2}")
    

person1 = Person()
person1.from_json(people_list[index1])
st.write(person1.print_name())
st.write(person1.count_starships())

person2 = Person()
person2.from_json(people_list[index2])
st.write(person2.print_name())
st.write(person2.count_starships())

st.write(person1.compare_age(person2))