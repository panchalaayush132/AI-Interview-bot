# AI Interview System
live at edusycide.tech
An intelligent interview platform that leverages Google's Gemini AI to automate resume analysis and conduct personalized technical interviews.

## Features

### Resume Analysis
- **AI-Powered Scoring**: Automatically analyzes uploaded resumes using Gemini AI
- **Feedback Generation**: Provides detailed feedback on candidate qualifications
- **Text Extraction**: Extracts text from PDF resumes for analysis

### Interview Management
- **AI Interviewer**: Conducts structured technical interviews based on candidate resumes
- **Real-time Chat**: Interactive interview sessions with conversational AI
- **Context-Aware Questions**: Questions tailored to the candidate's background and skills

### HR Dashboard
- **Candidate Overview**: View all candidates sorted by AI-generated scores
- **Resume Management**: Centralized storage and access to candidate resumes
- **Scoring Insights**: Detailed feedback and scoring for each candidate

## Tech Stack

- **Backend**: Django 6.0
- **AI Engine**: Google Gemini AI
- **Database**: SQLite3
- **PDF Processing**: PyMuPDF (fitz)
- **Frontend**: HTML/CSS/JavaScript (Django templates)

## Prerequisites

- Python 3.8+
- Google Gemini API key

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd interview
   ```

2. **Create and activate virtual environment**:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install django python-dotenv google-generativeai PyMuPDF
   ```

4. **Set up environment variables**:
   - Copy the `.env` file and update it with your Gemini API key:
   ```
   GEMINI_API_KEY=your_actual_gemini_api_key_here
   ```

5. **Run database migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the application**:
   - Open your browser and go to `http://127.0.0.1:8000`

## Usage

### For Candidates
1. Navigate to the resume upload page
2. Fill in your name and email
3. Upload your resume (PDF format)
4. View your AI-generated score and feedback

### For HR/Interviewers
1. Access the HR dashboard to view all candidates
2. Review AI scores and feedback
3. Conduct interviews using the interview room feature

### Interview Process
1. The AI interviewer starts with basic introduction questions
2. Progresses to technical questions based on the candidate's resume
3. Maintains conversation context throughout the interview
4. Asks one question at a time for focused responses

## API Configuration

The application uses Google's Gemini AI API. To get an API key:

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Add the key to your `.env` file as `GEMINI_API_KEY`

## Project Structure

```
interview/
├── core/                    # Django project settings
├── candidates/             # Resume upload and analysis app
│   ├── models.py          # Candidate model
│   ├── views.py           # Upload and dashboard views
│   ├── gemini_service.py  # AI resume analysis
│   └── templates/         # HTML templates
├── interview_session/      # Interview chat app
│   ├── gemini_chat.py     # AI interviewer logic
│   ├── views.py           # Interview room views
│   └── templates/         # Interview interface
├── media/                  # Uploaded files storage
└── db.sqlite3             # Database file
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This tool is designed to assist with the interview process but should not replace human judgment. Always review AI-generated assessments and conduct thorough interviews.</content>
<parameter name="filePath">d:\Main coding\python\AI\interview\README.md
