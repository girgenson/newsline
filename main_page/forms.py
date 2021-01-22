from django import forms
from . models import PieceOfNews


class PieceOfNewsForm(forms.ModelForm):
    class Meta:
        model = PieceOfNews
        fields = [
            'title',
            'text',
        ]
