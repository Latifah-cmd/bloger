from django.forms import ModelForm
from blog.models import Authour, Article

class AuthourForm(ModelForm):
    class Meta:
        model = Authour
        fields = '__all__'