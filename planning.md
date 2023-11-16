Markdown. Still working on these stages of the project.

- getting the wiki search bar to actually search and connect. 

In the sidebar template, create a search form that sends a GET request with the query.
  - Create a view that handles the search request, using `util.list_entries()` to find matching entries.
  - If an exact match is found, redirect to that entry's page. Otherwise, display a list of entries containing the query substring.

4. New Page
- **Objective:** Allow users to create new encyclopedia entries.
- **Implementation Steps:**
  - Create a form for new page creation, including fields for the title and Markdown content.
  - In `encyclopedia/views.py`, write a view to handle form submission.
  - Check if the title already exists using `util.get_entry(title)`.
  - If it's a new title, save the entry using `util.save_entry(title, content)` and redirect to the new entry's page.
  - If the title exists, return an error message.

5. Edit Page
- **Objective:** Allow users to edit existing encyclopedia entries.
- **Implementation Steps:**
  - Add an 'Edit' link on each entry page.
  - Create a view and template for editing, pre-populating the form with the existing Markdown content.
  - On submission, save the updated content and redirect to the updated entry's page.

6. Random Page
- **Objective:** Implement a feature to view a random encyclopedia entry.
- **Implementation Steps:**
  - Use `util.list_entries()` and Python's `random` module to select a random entry.
  - Redirect to the selected entry's page.


7. Markdown to HTML Conversion
- **Objective:** Convert Markdown content to HTML on entry pages.
- **Implementation Steps:**
  - Use the `markdown2` Python package (`pip3 install markdown2`) for conversion.
  - In the entry view, convert the Markdown content to HTML before passing it to the template.
  - Use `|safe` in the template to render HTML content.
