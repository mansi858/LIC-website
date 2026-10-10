# Nishita J. Kubavat | LIC Insurance Advisor

A professional LIC Insurance Advisor website designed to help visitors explore insurance plan information and send an inquiry easily.

> **Note:** This website is an independent advisor website. For official policy terms, benefits, eligibility, premiums, and claim decisions, always confirm details with LIC's official resources or an authorized representative.

## Features

- Responsive website layout for desktop and mobile
- LIC insurance plan information and descriptions
- Inquiry/contact form for prospective clients
- WhatsApp contact option (if configured)
- Flask backend for handling contact inquiries (if enabled)
- SQLite database support for storing inquiry details (if enabled)

## Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite
- **Version control:** Git and GitHub

> Edit this section to match the technologies and features actually present in your repository.

## Project Structure

Example structure:

```text
LIC-website/
├── app.py
├── templates/
│   ├── index.html
│   └── ...
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── requirements.txt
├── README.md
└── .gitignore
```

Your actual folder and file names may differ. Update this tree to match your project.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/mansi858/LIC-website.git
cd LIC-website
```

### 2. Create and activate a virtual environment

**Windows (Command Prompt):**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

If the project includes `requirements.txt`:

```bash
pip install -r requirements.txt
```

If it does not, install the packages your code actually uses. For a Flask app, that may include:

```bash
pip install Flask
```

### 4. Run the website

If your Flask entry file is `app.py`:

```bash
python app.py
```

Then open the local URL printed in the terminal (commonly `http://127.0.0.1:5000/`).

## Configuration

- Keep passwords, API keys, and other secrets in environment variables or a local `.env` file.
- Do **not** commit `.env`, virtual environments, or private customer information to GitHub.
- If using WhatsApp links, update the contact details in the relevant configuration/template file.
- If using SQLite, check how and where the application creates its database.

## Screenshots

Add screenshots of the homepage, plan cards, and inquiry form here. For example, place images in a `screenshots/` folder and link them like this:

```markdown
![LIC website homepage](screenshots/homepage.png)
```

Only add screenshots that exist in your repository.

## Future Improvements

- Improve mobile accessibility and form validation
- Add clear privacy information for inquiry submissions
- Add automated tests for important routes and form handling
- Improve deployment documentation
- Keep plan information current and clearly sourced

## Disclaimer

This website is for informational and inquiry purposes. It does not replace official LIC documentation or personalized financial advice. Policy terms, premium amounts, benefits, eligibility, and availability may change; verify them through official LIC channels before making a decision.

## Author

**Mansi Kubavat**  
GitHub: [@mansi858](https://github.com/mansi858)

---

If you use or adapt this project, please review all content and replace example structure or optional features with details that accurately reflect the current codebase.
