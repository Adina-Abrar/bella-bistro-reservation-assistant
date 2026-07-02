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

#  Vapi Voice Assistant Integration

This project supports voice-based restaurant reservations using **Vapi AI**.

The voice assistant communicates with the FastAPI backend through REST APIs exposed using **ngrok**.

---

## Prerequisites

Before testing the voice assistant, ensure that:

- The backend server is running.
- The frontend is optional (only required for the web interface).
- ngrok is installed.
- A Vapi account has been created.
- A Vapi Assistant has been configured.

---

## Step 1: Start the Backend

Run the FastAPI server:

```bash
python -m uvicorn backend.main:app --reload
```

The backend will start on:

```
http://127.0.0.1:8000
```

---

## Step 2: Expose the Local Server

Vapi cannot access your local machine directly.

Expose the FastAPI server using ngrok.

Run:

```bash
ngrok http 8000
```

Example output:

```
Forwarding

https://abcd-1234.ngrok-free.app
```

Copy the HTTPS URL.

Example:

```
https://abcd-1234.ngrok-free.app
```

---

## Step 3: Configure Vapi Tools

Replace every localhost URL inside the Vapi tools with the ngrok URL.

Example:

Instead of:

```
http://127.0.0.1:8000/reservation/create-reservation
```

Use:

```
https://abcd-1234.ngrok-free.app/reservation/create-reservation
```

Repeat this for every tool.

---

## Tool Configuration

### Check Availability

Method

```
POST
```

Endpoint

```
/reservation/check-availability
```

---

### Create Reservation

Method

```
POST
```

Endpoint

```
/reservation/create-reservation
```

---

### Find Reservation

Method

```
POST
```

Endpoint

```
/reservation/find-reservation
```

---

### Modify Reservation

Method

```
PUT
```

Endpoint

```
/reservation/modify-reservation
```

---

### Cancel Reservation

Method

```
PUT
```

Endpoint

```
/reservation/cancel-reservation
```

---

## Required Headers

For every tool, include the following header:

```
Content-Type: application/json
```

---

## Testing the Voice Assistant

Once the tools are configured, start a conversation with the assistant.

Example conversations:

### Check Availability

> Is there a table available tomorrow at 7 PM for 4 people?

---

### Create Reservation

> I'd like to book a table for tomorrow at 7 PM for 4 people. My name is Ahmad and my phone number is 03001234567.

---

### Find Reservation

> Find my reservation using phone number 03001234567.

---

### Modify Reservation

> Change my reservation to 8 PM.

---

### Cancel Reservation

> Cancel my reservation.

---

## Voice Assistant Flow

```
Customer
    │
    ▼
Vapi AI Assistant
    │
    ▼
HTTP Request
    │
    ▼
FastAPI Backend
    │
    ▼
Reservation Service
    │
    ▼
SQLite Database
    │
    ▼
FastAPI Response
    │
    ▼
Vapi AI
    │
    ▼
Customer receives spoken response
```

---

## Troubleshooting

### 404 Not Found

- Verify the ngrok URL is correct.
- Ensure the endpoint path matches the FastAPI route.
- Confirm the backend server is running.

---

### Connection Failed

- Make sure ngrok is running.
- Verify the HTTPS forwarding URL is being used.
- Restart ngrok if the URL has changed.

---

### Tool Not Working

- Verify the HTTP method (POST or PUT).
- Confirm the request body matches the API schema.
- Check that the `Content-Type` header is set to `application/json`.

---

### Voice Assistant Doesn't Respond

- Confirm all required Vapi tools are enabled.
- Check the Vapi dashboard logs for request and response details.
- Ensure the backend API is reachable through the ngrok URL.

---

## Important Notes

- The ngrok URL changes each time ngrok is restarted unless you have a reserved domain.
- Whenever the ngrok URL changes, update all Vapi tool URLs.
- Keep the FastAPI server running while testing the voice assistant.
- Keep the ngrok tunnel active during testing.
