HTTP-Server

# HTTP-Server

A lightweight HTTP server implemented from scratch in Python to demonstrate network socket programming and protocol parsing.

---

## Features

- **Low-Level Socket Handling:** Listens on configurable TCP ports using raw socket interfaces.
- **HTTP/1.1 Request Parsing:** Handles standard HTTP requests (`GET`, `POST`) and parses headers.
- **Response Handling:** Delivers basic HTML content and standard HTTP status responses (`200 OK`, `404 Not Found`).

## Tech Stack

- **Language:** Python 3.x
- **Modules:** `socket`, `sys`

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/bruh109-cyber/HTTP-Server.git](https://github.com/bruh109-cyber/HTTP-Server.git)
   cd HTTP-Server
Usage
Start the HTTP server locally:

Bash
python HTTPServer.py
Navigate to http://localhost:8080 (or configured port) in your web browser.

Project Structure
Plaintext
├── HTTPServer.py        # Socket listener and request dispatcher
└── README.md        # Documentation
