import unittest
from menu import Menu, Plato
from restaurante import Pedido, Restaurante

class TestPedido(unittest.TestCase):

    def test_agregar_plato_y_calcular_total(self):
        pedido = Pedido()
        pedido.agregar_plato(Plato("Hamburguesa", 10.0))
        pedido.agregar_plato(Plato("Refresco", 3.0))
        self.assertEqual(len(pedido.platos), 2)
        self.assertEqual(pedido.calcular_total(), 13.0)

class TestRestaurante(unittest.TestCase):

    def setUp(self):
        self.menu = Menu()
        self.menu.agregar_plato("Pasta", 12.0)
        self.menu.agregar_plato("Ensalada", 8.0)
        self.restaurante = Restaurante(self.menu)

    def test_crear_pedido(self):
        pedido = self.restaurante.crear_pedido()
        self.assertEqual(len(self.restaurante.pedidos), 1)
        self.assertIsInstance(pedido, Pedido)

    def test_agregar_plato_existente_a_pedido(self):
        pedido = self.restaurante.crear_pedido()
        result = self.restaurante.agregar_plato_a_pedido(pedido, "Pasta")
        self.assertTrue(result)
        self.assertEqual(pedido.calcular_total(), 12.0)

    def test_agregar_plato_inexistente(self):
        pedido = self.restaurante.crear_pedido()
        result = self.restaurante.agregar_plato_a_pedido(pedido, "Sushi")
        self.assertFalse(result)
        self.assertEqual(pedido.calcular_total(), 0.0)

if __name__ == '__main__':
    unittest.main()
