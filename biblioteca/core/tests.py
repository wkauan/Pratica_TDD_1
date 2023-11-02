from django.test import TestCase
from django.shortcuts import resolve_url as r
from http import HTTPStatus
from .models import LivroModel
from .forms import LivroForm


class IndexGetTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('core:index'), follow=True)

    def test_status_code(self):
        self.assertEqual(self.resp.status_code , HTTPStatus.OK)

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'index.html')

    def test_found_html(self):
        tags = (
            ('<html', 1),
            ('<body>', 1),
            ('Biblioteca', 2),
            ('<input', 2),
            ('<br>', 3),
            ('</body>', 1),
            ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)


class IndexPostTest(TestCase):
    def setUp(self):
        self.resp = self.client.post(r('core:index'))
        self.resp2 = self.client.post(r('core:index'), follow=True)

    def test_status_code(self):
        self.assertEqual(self.resp.status_code , HTTPStatus.FOUND)
        self.assertEqual(self.resp2.status_code , HTTPStatus.OK)

    def test_template_used(self):
        self.assertTemplateUsed(self.resp2, 'index.html')


class CadastroGetTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('core:cadastro'), follow=True)

    def test_status_code(self):
        self.assertEqual(self.resp.status_code , HTTPStatus.OK)

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'cadastro.html')

    def test_found_html(self):
        tags = (
            ('<html', 1),
            ('<body>', 1),
            ('Biblioteca', 2),
            ('<input', 9),
            ('<br>', 4),
            ('</body>', 1),
            ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)


class CadastroPostOk(TestCase):
    def setUp(self):
        data = {'titulo': 'Contos de Machado de Assis',
                'editora': 'editora Brasil',
                'autor':'Machado de Assis',
                'isbn':'1111111111111',
                'numPages':'26',
                'anoEscrita':'2016'}
        self.resp = self.client.post(r('core:cadastro'), data, follow=True)
        self.resp2 = self.client.post(r('core:cadastro'), data)

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'index.html')

    def test_status_code(self):
        self.assertEqual(self.resp.status_code , HTTPStatus.OK)
        self.assertEqual(self.resp2.status_code , HTTPStatus.FOUND)

    def test_dados_persistidos(self):
        print(LivroModel.objects.all())
        self.assertTrue(LivroModel.objects.exists())

    def test_found_html(self):
        tags = (
            ('<html', 1),
            ('<body>', 1),
            ('Biblioteca', 2),
            ('<input', 2),
            ('<br>', 3),
            ('</body>', 1),
            ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)


class CadastroPostFail(TestCase):
    def setUp(self):
        data = {'titulo': 'Livro sem editora',
                'autor':'Machado de Assis',
                'isbn':'1111111111111',
                'numPages':'26',
                'anoEscrita':'2016'}
        self.resp = self.client.post(r('core:cadastro'), data)

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'cadastro.html')

    def test_status_code(self):
        self.assertEqual(self.resp.status_code , HTTPStatus.OK)

    def test_dados_persistidos(self):
        self.assertFalse(LivroModel.objects.exists())


class ListarGet_withoutBook_Test(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('core:listar'), follow=True)

    def test_status_code(self):
        self.assertEqual(self.resp.status_code , HTTPStatus.OK)

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'listar.html')

    def test_found_html(self):
        tags = (
            ('<html', 1),
            ('<body>', 1),
            ('Biblioteca', 2),
            ('<input', 1),
            ('Nenhum livro cadastrado', 1),
            ('<br>', 2),
            ('</body>', 1),
            ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)


class ListarPost_withoutBook_Test(TestCase):
    def setUp(self):
        data = {}
        self.resp = self.client.post(r('core:listar'), data)

    def test_status_code(self):
        self.assertEqual(self.resp.status_code , HTTPStatus.OK)

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'detalhes.html')

    def test_found_html(self):
        tags = (
            ('<html', 1),
            ('<body>', 1),
            ('Biblioteca', 2),
            ('<input', 1),
            ('Nenhum livro cadastrado', 1),
            ('<br>', 2),
            ('</body>', 1),
            ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)


class ListarGet_OneBook_Test(TestCase):
    def setUp(self):
        self.livro = LivroModel(
            titulo='Contos de Machado de Assis',
            editora='editora Brasil',
            autor='Machado de Assis',
            isbn='1111111111111',
            numPages='262',
            anoEscrita='2016')
        self.livro.save()
        self.resp = self.client.get(r('core:listar'), follow=True)

    def test_status_code(self):
        self.assertEqual(self.resp.status_code , HTTPStatus.OK)

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'listar.html')

    def test_found_html(self):
        tags = (
            ('<html', 1),
            ('<body>', 1),
            ('Biblioteca', 2),
            ('<input', 4),
            ('Contos de Machado de Assis', 1),
            ('<br>', 2),
            ('</body>', 1),
            ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)


class ListarPost_OneBook_Test(TestCase):
    def setUp(self):
        self.livro = LivroModel(
            titulo='Contos de Machado de Assis',
            editora='editora Brasil',
            autor='Machado de Assis',
            isbn='1111111111111',
            numPages='262',
            anoEscrita='2016')
        self.livro.save()
        data = {'livro_id': self.livro.pk}
        self.resp = self.client.post(r('core:listar'), data)

    def test_status_code(self):
        self.assertEqual(self.resp.status_code , HTTPStatus.OK)

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'detalhes.html')

    def test_found_html(self):
        tags = (
            ('<html', 1),
            ('<body>', 1),
            ('Biblioteca', 2),
            ('<input', 1),
            ('Contos de Machado de Assis', 1),
            ('<br>', 14),
            ('</body>', 1),
            ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)


class LivroModelModelTest(TestCase):
    def setUp(self):
        self.livro = LivroModel(
            titulo='Contos de Machado de Assis',
            editora='editora Brasil',
            autor='Machado de Assis',
            isbn='1111111111111',
            numPages='262',
            anoEscrita='2016')
        self.livro.save()

    def test_created(self):
        self.assertTrue(LivroModel.objects.exists())


class LivroFormTest(TestCase):
    def test_fields_in_form(self):
        form = LivroForm()
        expected = ['titulo', 'editora', 'autor', 'isbn', 'numPages', 'anoEscrita']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_form_all_OK(self):
        dados = dict(titulo='Contos do Machado de Assis', 
                     editora='Editora Brasil', 
                     autor='Machado de Assis',
                     isbn='1111111111111',
                     numPages='262',
                     anoEscrita='2016')
        form = LivroForm(dados)
        errors = form.errors
        self.assertEqual({}, errors)

    def test_form_without_data_1(self):
        dados = dict(titulo='Contos do Machado de Assis')
        form = LivroForm(dados)
        errors = form.errors
        errors_list = errors['editora']
        msg = 'Informe a editora do livro.'
        self.assertEqual([msg], errors_list)

    def test_form_without_data_2(self):
        dados = dict(editora='Editora Brasil')
        form = LivroForm(dados)
        errors = form.errors
        errors_list = errors['titulo']
        msg = 'Informe o título do livro.'
        self.assertEqual([msg], errors_list)

    def test_form_without_data_3(self):
        dados = dict(editora='Editora Brasil')
        form = LivroForm(dados)
        errors = form.errors
        errors_list = errors['autor']
        msg = 'Informe o autor do livro'
        self.assertEqual([msg], errors_list)

    def test_form_without_data_4(self):
        dados = dict(editora='Editora Brasil')
        form = LivroForm(dados)
        errors = form.errors
        errors_list = errors['isbn']
        msg = 'Informe o ISBN do livro'
        self.assertEqual([msg], errors_list)
    
    def test_form_without_data_3(self):
        dados = dict(editora='Editora Brasil')
        form = LivroForm(dados)
        errors = form.errors
        errors_list = errors['numPages']
        msg = 'Informe o número de páginas do livro'
        self.assertEqual([msg], errors_list)

    def test_form_without_data_3(self):
        dados = dict(editora='Editora Brasil')
        form = LivroForm(dados)
        errors = form.errors
        errors_list = errors['anoEscrita']
        msg = 'Informe o ano que a obra foi escrita'
        self.assertEqual([msg], errors_list)

    def test_form_less_than_10_character_1(self):
        dados = dict(autor='Assis')
        form = LivroForm(dados)
        errors = form.errors
        errors_list = errors['autor']
        msg = 'Autor deve ter pelo menos 10 caracteres'
        self.assertEqual([msg], errors_list)

    def test_form_less_than_3_character_1(self):
        dados = dict(titulo='Co')
        form = LivroForm(dados)
        errors = form.errors
        errors_list = errors['titulo']
        msg = 'Deve ter pelo menos 3 caracteres'
        self.assertEqual([msg], errors_list)
        
    def test_form_less_than_3_character_2(self):
        dados = dict(editora='Co')
        form = LivroForm(dados)
        errors = form.errors
        errors_list = errors['editora']
        msg = 'Deve ter pelo menos 3 caracteres'
        self.assertEqual([msg], errors_list)

    def test_form_less_than_13_character_1(self):
        dados = dict(isbn='1')
        form = LivroForm(dados)
        errors = form.errors
        errors_list = errors['isbn']
        msg = 'Deve ter pelo menos 13 caracteres'
        self.assertEqual([msg], errors_list)

    def test_form_max_3_character_1(self):
        dados = dict(numPages='')
        form = LivroForm(dados)
        errors = form.errors
        errors_list = errors['numPages']
        msg = 'Informe o número de páginas do livro'
        self.assertEqual([msg], errors_list)
    
    def test_form_less_than_4_character_1(self):
        dados = dict(anoEscrita='202')
        form = LivroForm(dados)
        errors = form.errors
        errors_list = errors['anoEscrita']
        msg = 'O ano que a obra foi escrita deve ter 4 caracteres'
        self.assertEqual([msg], errors_list)
