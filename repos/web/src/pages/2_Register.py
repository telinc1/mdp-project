import streamlit as st
import os
from mysql.connector import connect, Error
import uuid

if 'username' in st.session_state:
    st.write(f'''You are already registered, {st.session_state['username']}''')
    st.stop()

try:
    with connect(
        host=os.environ["MYSQL_HOST"],
        user=os.environ["MYSQL_USERNAME"],
        password=os.environ["MYSQL_PASSWORD"],
        database="wwtbam",
    ) as connection:
        with st.form("register_form"):
            username = st.text_input("Username")
            password = st.text_input("Password")

            register = st.form_submit_button('Register')

        if register:
            with connection.cursor() as cursor:
                cursor.execute(
                    f"insert into users values ('{str(uuid.uuid4())}', '{username}', '{password}')"
                )

                connection.commit()

                st.write("Success!")
except Error as e:
    st.text(e)
