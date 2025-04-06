# sentiment.py
import pandas as pd
import mysql.connector
from textblob import TextBlob
from db import get_connection

def extract_points(text):
    blob = TextBlob(text)
    sentences = blob.sentences
    positive = [str(s) for s in sentences if s.sentiment.polarity > 0.2]
    negative = [str(s) for s in sentences if s.sentiment.polarity < -0.2]
    return positive, negative

def run_sentiment_analysis():
    db = get_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM feedbacks")
    feedbacks = cursor.fetchall()

    updated_count = 0
    for entry in feedbacks:
        text = entry["feedback_text"]
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        label = "positive" if polarity > 0.1 else "negative" if polarity < -0.1 else "neutral"
        positive_points, negative_points = extract_points(text)

        cursor.execute("""
            UPDATE feedbacks SET 
                sentiment_label = %s,
                sentiment_score = %s,
                positive_points = %s,
                negative_points = %s,
                summary = %s
            WHERE id = %s
        """, (
            label,
            round(polarity, 2),
            "\n".join(positive_points),
            "\n".join(negative_points),
            text[:200],  # just a simple summary for now
            entry["id"]
        ))
        updated_count += 1

    db.commit()
    db.close()
    return f"✅ Sentiment analysis completed for {updated_count} entries."
