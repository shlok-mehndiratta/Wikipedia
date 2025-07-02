# Wiki Encyclopedia 

A Markdown-based encyclopedia web application built with Django, allowing users to view, search, create, and edit knowledge entries through a clean, structured interface.

## 🔍 Project Overview

This project replicates a simplified version of Wikipedia. Each encyclopedia entry is stored as a Markdown file and dynamically rendered into HTML. Users can:

- View individual entries
- Search for exact or partial matches
- Create new entries
- Edit existing content
- Load a random entry for exploration

---

## 📌 Key Features

### Entry Page
- Route: `/wiki/<title>`
- Displays the content of an encyclopedia entry in HTML (converted from Markdown).
- Returns a custom error page if the entry does not exist.

### Index Page
- Displays all existing encyclopedia entries.
- Each title links directly to its detailed entry page.

### Search
- Sidebar search box for quick access.
- If the query matches an existing title (case-insensitive), user is redirected to that page.
- Otherwise, a search results page is shown with all matching titles (substring search).

### Create New Page
- Allows creation of new entries by entering a title and Markdown content.
- Prevents duplication: shows an error if the title already exists.

### Edit Page
- Provides an editable form pre-filled with existing Markdown content.
- Saves changes and redirects the user back to the entry page.

### Random Page
- Loads a random encyclopedia entry from the collection.

### Markdown Rendering
- Markdown files are converted into HTML using the `markdown2` Python library.

---

## 🧱 Tech Stack

- **Framework**: Django (Python)
- **Templating**: Django Templates
- **Markdown Parser**: [markdown2](https://github.com/trentm/python-markdown2)
- **Language**: Python 3.x
- **Storage**: Local file system (Markdown `.md` files)

---

## Project Structure

```bash
wiki/
├── encyclopedia/
│ ├── static/ # Static files (CSS) for the app.
│ ├── entries/ # Markdown files (content storage)
│ ├── templates/encyclopedia # HTML templates
│   ├── layout.html → Common layout with sidebar and other common features.
│   ├── index.html → Displays a list of all encyclopedia entries.
│   ├── entry.html → Displays detailed content of a specific entry.
│   ├── error.html → Displays error for invalid entries or inputs.
│   ├── new_page.html → Form for creating a new encyclopedia entry.
│   ├── edit_page.html → Form for editing an existing entry.
│
│ ├── views.py # Main view logic
│ ├── urls.py # Route definitions
│ ├── util.py # Helper functions for file handling
│       - list_entries( ) → get all page titles
│       - get_entry(title) → get content of a page
│       - save_entry(title, content) → save a new or edited page
├── manage.py
```
---

## ⚙️ Setup & Installation

1. **Clone the Repository**
   ``` bash
   git clone https://github.com/shlok-mehndiratta/wiki-encyclopedia.git
   cd wiki-encyclopedia
   ```
2. **Install Dependencies**
    ``` bash
    pip install -r requirements.txt
    ```
3. **Run the Django Development Server**
    ``` bash
    python manage.py runserver
    ```
4. **Open your browser and navigate to:**
    ```bash
    http://127.0.0.1:8000
    ```
---

### 🚧 Future Improvements:

- Add user authentication and page ownership
- Implement version history for entries
- Add support for images or embedded media
- Move to a database-backed entry model
- Add rich Markdown preview/editing support

### 📄 License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for more details.

---
### 🙋‍♂️ Author
Shlok Mehndiratta<br>
BS in EECS, IISER Bhopal<br>
[GitHub](https://github.com/shlok-mehndiratta) • [LinkedIn](https://www.linkedin.com/in/shlok-mehndiratta)
