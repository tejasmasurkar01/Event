import streamlit as st
import pymysql


st.title("College Event Registration Form")


name = st.text_input("Name")
email = st.text_input("Email")
phone = st.text_input("Phone")
event_choice = st.selectbox("Select Event", ["Event A", "Event B", "Event C"])
payment_option = st.radio("Payment Option", ["Credit Card", "PayPal", "Cash"])
agree_terms = st.checkbox("I agree to the terms and conditions")


def mysqlconnect(name, email, phone, event_choice, payment_option, agree_terms):
    try:
        
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="Tejas@1200",
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor
        )

        
        cursor = conn.cursor()

        
        cursor.execute("CREATE DATABASE IF NOT EXISTS eventdb")
        conn.select_db("eventdb")

        
        create_table_query = """
        CREATE TABLE IF NOT EXISTS event_registration (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            email VARCHAR(255),
            phone VARCHAR(15),
            event_choice VARCHAR(255),
            payment_option VARCHAR(255),
            agree_terms BOOLEAN
        )
        """
        cursor.execute(create_table_query)

        
        query = "INSERT INTO event_registration (name, email, phone, event_choice, payment_option, agree_terms) VALUES (%s, %s, %s, %s, %s, %s)"
        data = (name, email, phone, event_choice, payment_option, agree_terms)
        cursor.execute(query, data)

        
        conn.commit()

        
        cursor.close()
        conn.close()

        return True
    except pymysql.Error as err:
        st.error(f"Error: {err}")
        return False


if st.button("Submit"):
    
    if not name:
        st.error("Please enter your name")
    elif not email:
        st.error("Please enter your email")
    elif not phone:
        st.error("Please enter your phone number")
    elif not agree_terms:
        st.error("Please agree to the terms and conditions")
    else:
        
        if mysqlconnect(name, email, phone, event_choice, payment_option, agree_terms):
            st.success("Registration successful!")
        else:
            st.error("An error occurred while registering. Please try again later.")

