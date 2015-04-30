from django import forms
from django.contrib.admin import widgets
from models import Entry

class WideTextArea(forms.Textarea):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('attrs', {}).update({'rows': '10', 'cols': '40'})
        super(WideTextArea, self).__init__(*args, **kwargs)


class EntryForm(forms.ModelForm):

	title = forms.CharField(max_length=100,
			required=False,
			widget=forms.TextInput(attrs={'size': '40'}))
	body = forms.CharField(widget=WideTextArea(attrs={'class': 'resizable'}))

	def __init__(self, *args, **kwargs):
		self.request = kwargs.pop('request', None)
		super(EntryForm, self).__init__(*args, **kwargs)
		self.fields['owner'].widget = forms.HiddenInput()


	class Meta:
		model = Entry
		fields = ('title', 'body', 'tags', 'owner')
