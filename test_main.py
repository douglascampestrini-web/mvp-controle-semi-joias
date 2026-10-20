
import unittest
from io import StringIO
from unittest.mock import patch

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

    @patch("builtins.input", side_effect=["Brinco", "10"])
    def test_cadastro_com_dados_validos(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as saida:
            cadastrar_produto()

        self.assertEqual(len(produtos), 1)
        self.assertEqual(produtos[0]["nome"], "Brinco")
        self.assertEqual(produtos[0]["quantidade"], 10)
        self.assertIn("cadastrado com sucesso", saida.getvalue())

    @patch("builtins.input", return_value="   ")
    def test_rejeita_nome_vazio(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as saida:
            cadastrar_produto()

        self.assertEqual(produtos, [])
        self.assertIn("nome não pode ficar vazio", saida.getvalue())

    @patch("builtins.input", side_effect=["Brinco", "-1"])
    def test_rejeita_quantidade_negativa(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as saida:
            cadastrar_produto()

        self.assertEqual(produtos, [])
        self.assertIn("quantidade não pode ser negativa", saida.getvalue())

    @patch("builtins.input", side_effect=["Brinco", "abc"])
    def test_rejeita_quantidade_nao_inteira(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as saida:
            cadastrar_produto()

        self.assertEqual(produtos, [])
        self.assertIn("quantidade inteira válida", saida.getvalue())


if __name__ == "__main__":
    unittest.main()
