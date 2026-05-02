import streamlit as st
import requests

st.title("Smart Dictionary App")

word = st.text_input("Enter a word")

if st.button("Search"):
    if word:
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            st.subheader(f"Word: {data[0]['word']}")

            count = 1

            for meaning in data[0]["meanings"]:
                part = meaning["partOfSpeech"]

                for definition in meaning["definitions"][:2]:
                    st.write(f"{count}. ({part}) {definition['definition']}")
                    count += 1

                if count > 3:
                    break

        else:
            st.error("Word not found")