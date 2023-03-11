from django.forms import ModelForm, Textarea
from django.utils.translation import gettext_lazy
from .models import ReviewLaptop

class ReviewLaptopForm(ModelForm):
    class Meta:
        model = ReviewLaptop
        fields = ['rate','comment']
        labels = {
            'comment': gettext_lazy('Review'),
            'rate':gettext_lazy('Rate')
        }
        widgets = {
            'comment': Textarea(attrs={'cols': 40, 'rows': 7}),
        }