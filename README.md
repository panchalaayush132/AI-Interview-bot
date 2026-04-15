# SpeakFast Local (Django)

Offline adaptive spoken-English learning app for any native-language learner.

## Live Production
- https://www.edusycide.tech

## Features
- Local-only Django app (no API dependency)
- English-first learning design (works for any native language)
- Adaptive placement test to auto-assign level
- 5-level track: Starter, Beginner, Intermediate, Advanced, Expert
- Lesson-wise phrases with usage tips
- Quiz per lesson with instant review
- Session-based learner profile (name)
- XP, streak, and focus-session tracking (motivation loop)
- Level-locked progression for challenge pacing
- English Tutor Chat that talks back, corrects, and teaches locally
- Talk Mode for step-by-step speaking practice and live teaching
- Mistake practice mode from wrong answers
- Admin panel to manage lessons and questions

## Tech
- Python 3.14+
- Django 5
- SQLite (default local database)

No external database is required. SQLite is enough for the current offline version.

## Setup
1. Open terminal in project folder.
2. Install dependencies:
   ```powershell
   c:/python314/python.exe -m pip install -r requirements.txt
   ```
3. Run migrations:
   ```powershell
   c:/python314/python.exe manage.py makemigrations
   c:/python314/python.exe manage.py migrate
   ```
4. Seed starter lesson data:
   ```powershell
   c:/python314/python.exe manage.py seed_learning_data
   ```
5. Run server:
   ```powershell
   c:/python314/python.exe manage.py runserver
   ```
6. Open: http://127.0.0.1:8000/

## Admin Access (Optional)
Create admin user:
```powershell
c:/python314/python.exe manage.py createsuperuser
```
Then open: http://127.0.0.1:8000/admin/

## Where to add your own data
- Use Django admin to add/edit:
   - Placement questions
  - Lessons
  - Phrases
  - Quiz questions
   - Speaking prompts

## Suggested next upgrades
- Add pronunciation recording and local scoring
- Add spaced repetition scheduler
- Add downloadable PDF worksheets

## Use Installed Ollama Model In Tutor Chat
If you already installed a model, Tutor Chat can use it directly.

Set these environment variables before running Django:

```powershell
$env:OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
$env:OLLAMA_MODEL = "qwen2.5:3b"
$env:OLLAMA_TIMEOUT_SECONDS = "45"
```

Then run:

```powershell
c:/python314/python.exe manage.py runserver
```

Notes:
- If Ollama is unavailable, the tutor automatically falls back to local rule-based teaching.
- Keep model size small (3B/4B) for 4 GB VRAM devices.

## Talk Mode
Talk Mode is the interactive teaching flow.
It can speak the question aloud and listen to your voice reply in the browser.

Open:

```powershell
http://127.0.0.1:8000/talk-mode/
```

Use it to:
- practice short spoken English replies
- get instant grammar correction
- keep a back-and-forth teaching conversation
- speak the question aloud and answer by microphone
- start from very basic Q&A for weak beginners, then move to harder questions automatically

Best browsers for voice mode:
- Google Chrome
- Microsoft Edge

If voice recognition is not supported, type your reply in the box instead.

## Deploy On Vercel
You can deploy this Django app on Vercel.

### Live Production URL
- https://www.edusycide.tech

### 1) Push to GitHub
Push this project to a GitHub repository.

### 1.1) Show Deployment URL On GitHub
- Open your repository on GitHub.
- In About (right side), click the settings/gear icon.
- Set Website to https://www.edusycide.tech and save.
- This shows the production link in the repository header.

### 2) Create a Vercel Project
- Open Vercel dashboard.
- Import your GitHub repository.
- Framework preset: Other.

### 3) Set Environment Variables In Vercel
Add these variables in Project Settings -> Environment Variables:

- `SECRET_KEY` = your strong secret key
- `DEBUG` = `False`
- `ALLOWED_HOSTS` = your production domains, for example `www.edusycide.tech,edusycide.tech,your-app.vercel.app`
- `CSRF_TRUSTED_ORIGINS` = `https://www.edusycide.tech,https://edusycide.tech,https://your-app.vercel.app`

Optional for AI tutor:
- `OLLAMA_URL`
- `OLLAMA_MODEL`
- `OLLAMA_TIMEOUT_SECONDS`

### 4) Database Choice (Important)
- SQLite is not suitable for persistent production data on serverless platforms.
- Use PostgreSQL (Neon/Supabase/Render Postgres).
- Add `DATABASE_URL` in Vercel environment variables.

### 5) Build And Migrate
In Vercel build/deploy command flow, run:

```bash
python manage.py migrate
python manage.py collectstatic --noinput
```

### 6) Deploy
Redeploy the project after setting variables.

After deploy, open your Vercel URL and test:
- Home
- Placement Test
- Dataset Quiz
- Games
- Talk Mode
#
