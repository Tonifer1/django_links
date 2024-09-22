from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 8, 'cols': 30}),  # Säätää content-kentän kokoa lomakkeessa 
        }
        labels = {
            'title': 'Note Title',  # Muuttaa labelin nimen
            'content': ' Content',  # Muuttaa content-kentän nimen
        }
