from .models import Review
from django.forms import ModelForm, TextInput, Textarea, RadioSelect



class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['headline', 'rating', 'body']
        CHOICES = [(0,'0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]
        labels = {'headline':'Titre' , 'rating':'Note', 'body':'Commentaire'}
        widgets = {
            'headline': TextInput(attrs={'class': 'form-control'}),
            'rating': RadioSelect(choices=CHOICES, attrs={'style':'display:inline-block'}),
            'body': Textarea(attrs={'name': 'evaluation','class': 'form-control'}),
            }