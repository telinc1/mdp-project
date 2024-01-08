import streamlit as st
import os
from mysql.connector import connect, Error

if 'username' in st.session_state:
    st.write(f'''You are already logged in, {st.session_state['username']}''')
    st.stop()

try:
    with connect(
        host=os.environ["MYSQL_HOST"],
        user=os.environ["MYSQL_USERNAME"],
        password=os.environ["MYSQL_PASSWORD"],
        database="wwtbam",
    ) as connection:
        with st.form("login_form"):
            username = st.text_input("Username")
            password = st.text_input("Password")

            login = st.form_submit_button('Login')

        if login:
            with connection.cursor() as cursor:
                cursor.execute(
                    f"select * from users where username = '{username}' and password = '{password}'"
                )

                result = cursor.fetchone()

                st.session_state['username'] = result[1]

                st.write(result)
except Error as e:
    st.text(e)
