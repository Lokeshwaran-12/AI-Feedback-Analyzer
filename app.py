# app.py

import streamlit as st
import pandas as pd
from charts import get_summary_data
from sentiment import run_sentiment_analysis
from db import get_connection

# ------------------------- AUTH -------------------------
def check_login():
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    return username == "angelina jeba" and password == "HOD"

# ------------------- FEEDBACK PAGE ----------------------
def feedback_form():
    st.title("📋 Student Feedback Form")
    feedback_type = st.radio("Feedback For:", ("Staff", "Course"))

    if feedback_type == "Staff":
        name = st.selectbox("Select Staff Name", ["Prof. Meena", "Dr. Kumar", "Mrs. Latha"])
        course = st.text_input("Course Name")
    else:
        course = st.selectbox("Select Course Name", ["AI", "DBMS", "DSA"])
        name = st.text_input("Staff Name")

    student_name = st.text_input("Your Name")
    rating = st.slider("Rate (0 - 5)", 0.0, 5.0, 3.0, 0.5)
    feedback_text = st.text_area("Write Feedback Summary")

    if st.button("Submit Feedback"):
        db = get_connection()
        cursor = db.cursor()
        cursor.execute("""
            INSERT INTO feedbacks (student_name, staff_name, course_name, feedback_text, original_rating)
            VALUES (%s, %s, %s, %s, %s)
        """, (student_name, name, course, feedback_text, rating))
        db.commit()
        db.close()
        st.success("✅ Feedback submitted successfully!")

# ------------------- SENTIMENT PAGE ----------------------
def sentiment_interface():
    st.title("🧠 Sentiment Analysis Dashboard")
    if not check_login():
        st.warning("Please login to view sentiment analysis.")
        return

    st.success("Login Successful ✅")

    updated = False
    if st.button("Run Sentiment Analysis"):
        result = run_sentiment_analysis()
        st.success(result)
        updated = True

    sentiment_counts, avg_rating_staff, avg_rating_course, df = get_summary_data()

    option = st.radio("Select View:", ["Staff Analysis", "Course Analysis", "Overall Ratings", "View Table"])

    if option == "Staff Analysis":
        staff = st.selectbox("Choose Staff", df["staff_name"].dropna().unique())
        entries = df[df["staff_name"] == staff]

        if updated:
            for _, entry in entries.iterrows():
                st.text(f"👨‍🏫 Staff: {entry['staff_name']}")
                st.text(f"📚 Course: {entry['course_name']}")
                st.text(f"🧠 Overall Sentiment: {entry.get('sentiment_label', 'Unknown').capitalize()} ({entry.get('sentiment_score', 'N/A')})")
                st.text("✅ Good Points Mentioned by Students:")
                st.text(entry.get('positive_points', '(none)').strip() or '(none)')
                st.text("❌ Bad Points Mentioned by Students:")
                st.text(entry.get('negative_points', '(none)').strip() or '(none)')
                st.text("📝 Summary:")
                st.text(entry.get('summary', '(No summary)'))
                st.markdown("---")

    elif option == "Course Analysis":
        course = st.selectbox("Choose Course", df["course_name"].dropna().unique())
        entries = df[df["course_name"] == course]

        if updated:
            for _, entry in entries.iterrows():
                st.text(f"👨‍🏫 Staff: {entry['staff_name']}")
                st.text(f"📚 Course: {entry['course_name']}")
                st.text(f"🧠 Overall Sentiment: {entry.get('sentiment_label', 'Unknown').capitalize()} ({entry.get('sentiment_score', 'N/A')})")
                st.text("✅ Good Points Mentioned by Students:")
                st.text(entry.get('positive_points', '(none)').strip() or '(none)')
                st.text("❌ Bad Points Mentioned by Students:")
                st.text(entry.get('negative_points', '(none)').strip() or '(none)')
                st.text("📝 Summary:")
                st.text(entry.get('summary', '(No summary)'))
                st.markdown("---")

    elif option == "Overall Ratings":
        st.subheader("📊 Average Ratings for Staff")
        st.write(avg_rating_staff)

        st.subheader("📊 Average Ratings for Courses")
        st.write(avg_rating_course)

    elif option == "View Table":
        st.dataframe(df)

# ------------------- MAIN APP ----------------------
st.sidebar.title("🎓 Feedback System")
selection = st.sidebar.radio("Go to", ("Submit Feedback", "Sentiment Analysis"))

if selection == "Submit Feedback":
    feedback_form()
elif selection == "Sentiment Analysis":
    sentiment_interface()
