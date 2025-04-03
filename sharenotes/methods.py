from .models import Notes
def Opened_Note(note: Notes) -> dict:
    """
    Function to open a note and return its details.
    """
    return {'opened_note': note, 'page_title': note.title, 'open_note': True}