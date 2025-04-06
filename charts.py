# charts.py
import pandas as pd
from db import get_connection

def get_summary_data():
    db = get_connection()
    df = pd.read_sql("SELECT * FROM feedbacks", db)
    db.close()

    sentiment_counts = df["sentiment_label"].value_counts().to_dict()
    avg_rating_staff = df.groupby("staff_name")["original_rating"].mean().round(2)
    avg_rating_course = df.groupby("course_name")["original_rating"].mean().round(2)

    return sentiment_counts, avg_rating_staff, avg_rating_course, df
