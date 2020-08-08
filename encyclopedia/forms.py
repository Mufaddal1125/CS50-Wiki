from django import forms


class Create(forms.Form):
    title = forms.CharField(label="Title", max_length=64)
    text = forms.CharField(widget=forms.Textarea, label="Article")


class Edit(forms.Form):
    title = forms.CharField(label="Title", max_length=64)
    content = forms.CharField(label="Content", widget=forms.Textarea)
