from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


class SignupForm(UserCreationForm):
   class Meta:
        model = get_user_model()
        fields = ['username']
        
   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      for field in self.fields.values():
         field.help_text = None
      # Choose what write in the widget
      self.fields['username'].widget.attrs['placeholder'] = 'Nom d\'utilisateur'
      # Center widget text
      self.fields['username'].widget.attrs['class'] = 'form-control text-center'
      # Write or not text helper
      self.fields['username'].label = ''
      
      self.fields['password1'].widget.attrs['placeholder'] = 'Mot de passe'
      self.fields['password1'].widget.attrs['class'] = 'form-control text-center'
      self.fields['password1'].label = ''
      
      self.fields['password2'].widget.attrs['placeholder'] = 'Mot de passe'
      self.fields['password2'].widget.attrs['class'] = 'form-control text-center'
      self.fields['password2'].label = ''

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Nom d\'utilisateur'
        self.fields['username'].widget.attrs['class'] = 'form-control text-center'
        self.fields['username'].label = ''
        self.fields['password'].widget.attrs['placeholder'] = 'Mot de passe'
        self.fields['password'].widget.attrs['class'] = 'form-control text-center'
        self.fields['password'].label = ''