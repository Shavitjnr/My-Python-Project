# Web Scraper

A simple and flexible Web Scraper written in Python. This tool allows you to scrape news headlines (from BBC News as a demo), and save the results to CSV, JSON, or display them directly in the terminal.

---

## 🌐 Features
- **Scrape News Headlines:** Collects headlines from BBC News (can be extended for jobs, products, etc.).
- **Flexible Output:** Save results as CSV, JSON, or display in the CLI.
- **Easy to Extend:** Add more scraping targets (job listings, product prices) with minimal code changes.
- **User-Friendly CLI:** Menu-driven interface for scraping and saving options.

---

## 🛠️ Requirements
- **Python:** 3.6 or higher
- **Libraries:**
  - `requests`
  - `beautifulsoup4`

Install dependencies with:
```bash
pip install requests beautifulsoup4
```

---

## 🚀 Installation & Usage
1. **Clone or Download this Project Folder**
2. **Install Dependencies:**
   ```bash
   pip install requests beautifulsoup4
   ```
3. **Run the Application:**
   ```bash
   python3 main.py
   ```
4. **Follow the Prompts:**
   - Choose what to scrape (news headlines)
   - Choose output format (CSV, JSON, or CLI display)

---

## 📁 File Structure
```
Project 13/
├── main.py      # Main web scraper script
└── README.md    # Project documentation
```

---

## 📝 About This Project
This Web Scraper was created to demonstrate basic web scraping with Python using requests and BeautifulSoup. It is ideal for learning, prototyping, or quickly collecting data from web pages.

Feel free to use, modify, or extend this project for your own needs!
