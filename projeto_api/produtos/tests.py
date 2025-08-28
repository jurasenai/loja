# produtos/tests.py

from django.test import TestCase
from .models import Categoria, Produto
from django.core.files.uploadedfile import SimpleUploadedFile

class CategoriaProdutoModelTest(TestCase):

    def setUp(self):
        self.categoria = Categoria.objects.create(nome="Eletrônicos")

    def test_criacao_categoria(self):
        self.assertEqual(self.categoria.nome, "Eletrônicos")
        self.assertEqual(str(self.categoria), "Eletrônicos")

    def test_criacao_produto_sem_imagem(self):
        produto = Produto.objects.create(
            nome="Notebook",
            descricao="Notebook rápido",
            preco=3500.00,
            categoria=self.categoria
        )
        self.assertEqual(produto.nome, "Notebook")
        self.assertEqual(produto.preco, 3500.00)
        self.assertEqual(str(produto), "Notebook")
        self.assertIsNone(produto.imagem.name)  # Verifica que o 'name' é None, que é o comportamento padrão

    def test_criacao_produto_com_imagem(self):
        imagem_mock = SimpleUploadedFile(
            name='notebook.jpg',
            content=b'fake-image-data',
            content_type='image/jpeg'
        )
        produto = Produto.objects.create(
            nome="Notebook com imagem",
            descricao="Com imagem",
            preco=4200.00,
            categoria=self.categoria,
            imagem=imagem_mock
        )
        self.assertIsNotNone(produto.imagem)
        self.assertTrue(produto.imagem.name.startswith('produtos/'))
