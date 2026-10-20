
import unittest
from main import produtos, cadastrar_produto


class TestEstoque(unittest.TestCase):

    def setUp(self):
        produtos.clear()

    def test_lista_inicia_vazia(self):
        self.assertEqual(produtos, [])

    def test_cadastro_direto_de_produto(self):
        produtos.append({
            "nome": "Brinco",
            "quantidade": 10
        })

        self.assertEqual(len(produtos), 1)
        self.assertEqual(produtos[0]["quantidade"], 10)


if __name__ == "__main__":
    unittest.main()
