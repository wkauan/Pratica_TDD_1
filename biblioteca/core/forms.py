from django import forms
from django.core.exceptions import ValidationError
from core.models import LivroModel


def validate_title(value):
    if len(value) < 10:
        raise ValidationError('Deve ter pelo menos dez caracteres')


class LivroForm(forms.ModelForm):

    class Meta:
        model = LivroModel
        fields = ['titulo', 'editora', 'autor', 'isbn', 'numPages', 'anoEscrita']
        error_messages = {
            'titulo': {
                'required': ("Informe o título do livro."),
            },
            'editora': {
                'required': ("Informe a editora do livro."),
            },
            'autor': {
                'required': ("Informe o autor do livro"),
            },
            'isbn': {
                'required': ("Informe o isbn do livro"),
            },
            'numPages': {
                'required': ("Informe o número de páginas do liro"),
            },
            'anoEscrita': {
                'required': {"Informe o ano que a obra foi escrita"},
            },
        }

    def clean_titulo(self):
        titulo = self.cleaned_data['titulo']
        validate_title(titulo)
        return titulo

    def clean_editora(self):
        editora = self.cleaned_data['editora']
        validate_title(editora)
        return editora

    def clean_autor(self):
        autor = self.cleaned_data['autor']
        validate_title(autor)
        return autor

    def clean_isbn(self):
        isbn = self.cleaned_data['isbn']
        validate_title(isbn)
        return isbn

    def clean_numPages(self):
        numPages = self.cleaned_data['numPages']
        validate_title(numPages)
        return numPages

    def clean_anoEscrita(self):
        anoEscrita = self.cleaned_data['anoEscrita']
        validate_title(anoEscrita)
        return anoEscrita

    def clean(self):
        self.cleaned_data = super().clean()
        return self.cleaned_data
