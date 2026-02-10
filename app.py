import streamlit as st

st.title("Въпросник")

st.write("Отговори на въпросите по-долу:")

category = st.selectbox(
    "Избери област:",
    ("География", "История")
)

if category == "География":
    st.subheader("Въпрос по География")
    question = "Коя е столицата на България?"

    answer = st.radio(
        question,
        ("Пловдив", "София", "Варна", "Бургас")
    )

    if st.button("Провери отговора"):
        if answer == "София":
            st.success("Браво! Отговорът е верен ")
        else:
            st.error("Грешен отговор, Опитай пак!")

elif category == "История":
    st.subheader("Въпрос по История")
    question = "През коя година е основана българската държава?"
    

    answer = st.text_input("През коя година е основана българската държава?")
    answer2 = st.text_input("Князът покръстител")

    if st.button("Провери"):
        if answer == "681":
            st.success("Точно така! 681 година")
        else:
            st.error("Неправилно! Верният отговор е 681.")

    if st.button("Провери"):
        if answer2 == "Борис":
            st.success("Точно така! Княз Борис")
        else:
            st.error("Неправилно! Верният отговор е княз Борис")
 



