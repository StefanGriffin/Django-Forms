from django import forms 

class ReviewForm(forms.Form):
    user_name = forms.CharField(label="Your name", max_length=5, error_messages={
        "required": "Your name must not be empty",
        "max_length": "Please enter a max 5 character word"
    })
