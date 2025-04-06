# AI-Powered Feedback Analyzer for Academic Improvement

Include Emojis: No
Status: Draft

# AI-Powered Feedback Analyzer for Academic Improvement

A sophisticated web application that leverages artificial intelligence to transform academic feedback into actionable insights. Built with Streamlit and powered by advanced NLP capabilities, this tool helps educational institutions make data-driven decisions for continuous improvement.

## 🧠 Project Overview

This Streamlit-based web application revolutionizes how academic institutions collect and analyze student feedback. By combining the power of Natural Language Processing (NLP) with intuitive visualization, it provides:

- Automated sentiment analysis of student feedback for both staff and courses
- Smart categorization of feedback into positive and negative aspects
- AI-powered summary generation
- Sentiment rating calculation
- Secure data storage using MySQL

## 💻 Tech Stack

- Python - Core programming language
- Streamlit - Web application framework
- MySQL - Database management
- TextBlob - Sentiment analysis
- NLTK - Natural Language Processing
- Pandas - Data manipulation and analysis

## 📦 Requirements

Install all dependencies using:

```bash
pip install -r requirements.txt
```

Contents of `requirements.txt`:

```
streamlit==1.32.2
mysql-connector-python==8.3.0
textblob==0.17.1
nltk==3.8.1
pandas==2.2.2
```

## 📸 Screenshots

[Feedback Form Screenshot]

Student feedback collection interface with course/staff selection, rating system, and feedback input field.

[Analytics Dashboard Screenshot]

Administrative dashboard showing sentiment analysis results, feedback summaries, and statistical visualizations.

## 🛠️ Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/yourusername/ai-feedback-analyzer.git
cd ai-feedback-analyzer
```

1. Install dependencies:

```bash
pip install -r requirements.txt
```

1. Configure MySQL database:

```python
# config.py
DB_CONFIG = {
    'host': 'your_host',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'feedback_db'
}
```

1. Run the application:

```bash
streamlit run app.py
```

## 📂 Project Structure

```
ai-feedback-analyzer/
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── static/
│   └── assets/
└── utils/
    ├── analyzer.py
    ├── database.py
    └── preprocessor.py
```

## 🙋 Usage

### For Students:

- Select feedback type (Staff/Course)
- Choose the specific staff member or course
- Provide rating (1-5 stars)
- Submit detailed feedback

### For Administrators:

- Login to access the admin dashboard
- View aggregated feedback analytics
- Access sentiment analysis reports
- Export data for further analysis

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📫 Contact

For questions and support, please contact:

- GitHub: [Your GitHub Username]
- Email: [your.email@example.com]

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 🌟 Acknowledgments

- TextBlob team for their excellent NLP library
- Streamlit community for the amazing web framework
- All contributors and testers who helped improve this project