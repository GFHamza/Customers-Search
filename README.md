Google Places API Scraper
📍 A Python script to fetch business details (name, address, phone, website, and coordinates) from Google Places API and export them to JSON.
✨ Features
✔ Google Places Text Search – Retrieve businesses based on a search query (e.g., "coffee shops in New York").
✔ Detailed Place Information – Fetch contact details (phone, website), addresses, and coordinates.
✔ Paginated Results – Automatically handles multiple pages of search results.
✔ JSON Export – Save structured data in google_maps_results_with_contacts.json.
✔ User-Friendly CLI – Simple terminal prompts for API key and search query.
🚀 Installation
Prerequisites
Python 3.6+

requests library

A valid Google Places API key

Setup
Clone the repo:

bash
Copy
git clone https://github.com/GFHamza/Customers-Search.git
cd Customers-Search
Install dependencies:

bash
Copy
pip install requests
🛠️ Usage
Run the script:

bash
Copy
python places.py
Enter your Google Maps API key when prompted.

Type a search query (e.g., "restaurants in Berlin").

Output
A JSON file (google_maps_results_with_contacts.json) with all business details.

Printed summary in the terminal (name, address, phone, website, and coordinates).

Example Output
json
Copy
[
{
  "name": "Central Coffee",
    "latitude": 40.7128,
    "longitude": -74.0060,
    "address": "123 Main St, New York, NY",
    "phone": "+1 555-123-4567",
    "website": "https://centralcoffee.com"
  }
]

📂 Project Structure
plaintext
Copy
google-places-scraper/
├── places.py           # Main Python script
├── README.md            # This file
└── google_maps_results_with_contacts.json  # (Generated after run)
⚠️ Important Notes
Google Places API Costs: This script uses the Google Places Text Search API, which is not free for high-volume requests.

Rate Limits: Avoid rapid requests; the script includes a 2-second delay between paginated calls.

Privacy: Do not share your API key in the script or GitHub repo.

🤝 Contributing
Fork the repo.

Create a feature branch:

bash
Copy
git checkout -b feature/new-feature
Commit changes:

bash
Copy
git commit -m "Add pagination limit"
Push and open a Pull Request.

📜 License
MIT License. See LICENSE for details.

🙏 Credits
Your Name – @GFHamza

Google Places API – Documentation

🚀 Happy Scraping! Leave a ⭐ if this tool helps you.
