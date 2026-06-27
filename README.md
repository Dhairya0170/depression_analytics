# Depression Assessment Analytics System 🧠

A backend RESTful API built with Django and Django REST Framework (DRF) designed to process, evaluate, and store PHQ-9 depression assessments. The system automatically calculates severity scores based on clinical thresholds and securely supports both authenticated and anonymous submissions.

## 🛠️ Tech Stack
* **Framework:** Python, Django
* **API Interface:** Django REST Framework (DRF)
* **Database:** SQLite (Development) / Easily scalable to PostgreSQL
* **Architecture:** Model-View-Controller (MVC) / REST API

---

## ✨ Core Features

* **Automated Clinical Scoring:** Overrides default save methods to dynamically calculate a user's total score (0-27) based on 9 core assessment questions.
* **Intelligent Severity Classification:** Automatically categorizes results into clinical tiers: *Minimal, Mild, Moderate, Moderately Severe, or Severe*.
* **Flexible Authentication:** The database schema is designed to accept foreign keys for logged-in users, while safely allowing `null/blank` entries for completely anonymous assessments.
* **Secure Read-Only Fields:** API serializers strictly prevent users from manually manipulating their total score or severity tier via POST requests.

---

## 🗄️ Database Schema

### `Assessment` Model
| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | Primary Key | Unique identifier for the test. |
| `user` | Foreign Key | Links to Django `User` model (Nullable for anonymity). |
| `q1` - `q9` | Integer | Responses to standard PHQ-9 questions (0-3 scale). |
| `q10_difficulty` | Integer | Tracks how difficult these problems have made daily life. |
| `total_score` | Integer | Backend-calculated total score. |
| `severity` | String | Backend-calculated classification (e.g., "Moderate"). |
| `taken_at` | DateTime | Auto-stamped creation time. |

---

## 🚀 API Endpoints

The API is fully routed using DRF's `DefaultRouter`.

### `GET /api/assessments/`
Retrieves a list of all submitted assessments, ordered by the most recent (`-taken_at`).

### `POST /api/assessments/`
Submits a new assessment. 
* **Required Payload:** `q1` through `q9`, and `q10_difficulty`.
* **Ignored Payload:** `total_score`, `severity`, `taken_at` (System generates these automatically).

---

## 💻 Local Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Dhairya0170/depression_analytics.git
   cd depression_analytics
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install django djangorestframework
   ```

4. **Run database migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Start the development server:**
   ```bash
   python manage.py runserver
   ```
   *The API will be available at `http://127.0.0.1:8000/api/assessments/`*

---
**Author:** [Dhairya Parmar](https://github.com/Dhairya0170)  
*GATE CSE 2026 Qualified | Computer Engineering Graduate*
