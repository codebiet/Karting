from django import forms
from kartingapp.models import Search

class FormName(forms.ModelForm):
	class Meta:
	    Name = forms.CharField(label='Name',widget=forms.TextInput(attrs={'class':'td1','class' : 'contact-form'}))
	    Email = forms.EmailField(label='Email Address', widget=forms.TextInput(attrs={'class':'td1','class':'contact-form'}))
	    Contact=forms.IntegerField(label='Contact No.', widget=forms.TextInput(attrs={'class':'td1','class':'contact-form'}))
	    Message = forms.CharField(widget=forms.Textarea(attrs={'class':'td1', 'class':'contact-form', 'line-height' : '2', 'margin' : '3%'}))


# class SearchBar(forms.Form):
class SearchBar(forms.Form):
	Search = forms.CharField(label='', max_length=100, 
    	widget=forms.TextInput(attrs={'placeholder':'What are you looking for?',
    	                              'class' : "search-input"
                                       }))

	# class Meta:
	# 	model=Search
	# 	fields=['mdl_search']
	# 	widgets ={'mdl_search': forms.TextInput(attrs={'placeholder':'What are you looking for?',
 #    	                              'class' : "search-input"
 #                                       })}