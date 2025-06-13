# Wiki Encyclopedia Project

This project implements a Wiki-like encyclopedia using Django, where users can create, edit, and search entries stored as Markdown files.

## Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS (Bootstrap optional)
- **Markdown Conversion**: [`markdown2`](https://github.com/trentm/python-markdown2)


## Project Structure

- **wiki/**: Django project directory.
  - **encyclopedia/**: Django app for managing encyclopedia entries.
    - ** ``urls.py`` **: URL routing for the app.
    - **views.py**: Defines views for rendering pages.
    - **util.py**: Utility functions for interacting with encyclopedia entries.
        - `list_entries()` → get all page titles
        - `get_entry(title)` → get content of a page
        - `save_entry(title, content)` → save a new or edited page
    - **templates/**: HTML templates for rendering pages.
      - **encyclopedia/**: Templates specific to the encyclopedia app.
        - **layout.html**: Basic common layout with sidebar and other common features.
        - **index.html**: Displays a list of all encyclopedia entries.
        - **entry.html**: Displays detailed content of a specific entry.
        - **error.html**: Displays error for invalid entries or inputs.
        - **new_page.html**: Form for creating a new encyclopedia entry.
        - **edit_page.html**: Form for editing an existing entry.
    - **entries/**: Directory for storing Markdown files of encyclopedia entries.
    - **static/**: Static files (CSS) for the app.

## Features Implemented

### Entry Page
- Visiting `/wiki/TITLE` renders the content of the encyclopedia entry.
- Handles non-existent entries with an error page.

### Index Page
- Updated `index.html` to make entry names clickable, leading directly to entry pages.

### Search
- Users can search for entries using the sidebar search box.
- Matches direct to entry pages or display search results listing all matching entries.

### New Page
- Allows creation of new encyclopedia entries with title and Markdown content.
- Validates against existing entries before saving.

### Edit Page
- Enables editing of existing entry Markdown content.
- Saves changes and redirects back to the entry page.

### Random Page
- Clicking "Random Page" directs users to a random encyclopedia entry.

### Markdown to HTML Conversion
- Converts Markdown content of entries to HTML using `markdown2` library.

## Setup Instructions

1. Clone the repository.
2. Install dependencies:
```pip install -r requirements.txt```
3. Run migrations:
```python manage.py migrate```
4. Start the Django development server:
```python manage.py runserver```
5. Access the application at `http://localhost:8000`.

## Contribution

Feel free to fork the repository and submit pull requests for any improvements or additional features.

## License

This project is licensed under the MIT License - see the LICENSE file for details.


``Made with 💻 by [Shlok Mehndiratta](https://github.com/shlok-mehndiratta)``
