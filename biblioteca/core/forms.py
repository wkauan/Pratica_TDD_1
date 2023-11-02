from django import forms
from django.core.exceptions import ValidationError
from core.models import LivroModel


def validate_titulo(value):
    if len(value) < 3:
        raise ValidationError('Deve ter pelo menos 3 caracteres')

def validate_editora(value):
    if len(value) < 3:
        raise ValidationError('Deve ter pelo menos 3 caracteres')

def validate_autor(value):
    if len(value) < 10:
        raise ValidationError('Autor deve ter pelo menos 10 caracteres')
    
def validate_isbn(value):
    if len(value) < 13:
        raise ValidationError('Deve ter pelo menos 13 caracteres')
    if not value.isdigit():
        raise ValidationError('Deve ter pelo menos 13 caracteres e devem ser todos numéricos') 
               
def validate_numPages(value):
    if not 1 <= len(value) <= 3:
        raise ValidationError('Deve ter entre 1 e 3 caracteres')
    if not value.isdigit():
        raise ValidationError('Deve ter 1 a 3 caracteres e devem ser todos numéricos')

def validate_anoEscrita(value):
    if len(value) < 4:
        raise ValidationError('O ano que a obra foi escrita deve ter 4 caracteres')
    if not value.isdigit():
        raise ValidationError('O ano que a obra foi escrita deve ter 4 caracteres e numéricos')


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
                'required': ("Informe o ISBN do livro"),
            },
            'numPages': {
                'required': ("Informe o número de páginas do livro"),
            },
            'anoEscrita': {
                'required': ("Informe o ano que a obra foi escrita"),
            },
        }

    def clean_titulo(self):
        titulo = self.cleaned_data['titulo']
        validate_titulo(titulo)
        return titulo

    def clean_editora(self):
        editora = self.cleaned_data['editora']
        validate_editora(editora)
        return editora

    def clean_autor(self):
        autor = self.cleaned_data['autor']
        validate_autor(autor)
        return autor

    def clean_isbn(self):
        isbn = self.cleaned_data['isbn']
        validate_isbn(isbn)
        return isbn

    def clean_numPages(self):
        numPages = self.cleaned_data['numPages']
        validate_numPages(numPages)
        return numPages

    def clean_anoEscrita(self):
        anoEscrita = self.cleaned_data['anoEscrita']
        validate_anoEscrita(anoEscrita)
        return anoEscrita

    def clean(self):
        self.cleaned_data = super().clean()
        return self.cleaned_data
