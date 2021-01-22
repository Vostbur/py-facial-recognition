from django import forms


class UploadFileForm(forms.Form):
    imgfile = forms.FileField(label='Select an image file')
