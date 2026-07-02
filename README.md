#  Bella Bistro Reservation Assistant

An AI-powered restaurant reservation system built with **FastAPI**, **SQLite**, **Streamlit**, and **Vapi**.

The application allows customers to check table availability, create reservations, find existing reservations, modify bookings, and cancel reservations through both a web interface and an AI voice assistant.

---

##  Features

-  Check table availability
-  Create a reservation
-  Find a reservation
-  Modify an existing reservation
-  Cancel a reservation
-  SQLite database integration
-  Streamlit frontend
-  FastAPI backend
-  RESTful API
-  AI Voice Assistant integration using Vapi

---

##  Technologies Used

- Python 3.14
- FastAPI
- Streamlit
- SQLAlchemy
- SQLite
- Uvicorn
- Pydantic
- Vapi
- Ngrok (for local testing)

---

#  Project Structure

```
Bella-Bistro-Reservation-Assistant/
│
├── backend/
│   ├── api/
│   ├── database/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── utils/
│   └── main.py
│
├── frontend/
│   ├── pages/
│   ├── utils/
│   └── app.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

#  Installation

## 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Bella-Bistro-Reservation-Assistant.git
```

Navigate into the project:

```bash
cd Bella-Bistro-Reservation-Assistant
```

---

## 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it:

### Windows

```bash
.venv\Scripts\activate
```

### Mac/Linux

```bash
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

#  Running the Backend

Start the FastAPI server:

```bash
python -m uvicorn backend.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

#  Running the Frontend

Open another terminal.

Run:

```bash
python -m streamlit run frontend/app.py
```

The Streamlit application will open automatically in your browser.

---

#  API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/reservation/check-availability` | Check table availability |
| POST | `/reservation/create-reservation` | Create a reservation |
| POST | `/reservation/find-reservation` | Find a reservation |
| PUT | `/reservation/modify-reservation` | Modify a reservation |
| PUT | `/reservation/cancel-reservation` | Cancel a reservation |

---

#  Vapi Integration

To test the AI Voice Assistant:

1. Start the FastAPI backend.
2. Run
