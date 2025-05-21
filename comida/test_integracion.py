import unittest
from unittest.mock import MagicMock
from menu import Plato
from restaurante import Restaurante

class TestRestauranteIntegracionConMocks(unittest.TestCase):

    def setUp(self):
        # Simulamos el menú y el pedido
        self.menu_mock = MagicMock()
        self.pedido_mock = MagicMock()
        
        # Creamos un restaurante con el menú simulado
        self.restaurante = Restaurante(self.menu_mock)
        
        # Sobrescribimos el método crear_pedido para devolver el mock de pedido
        self.restaurante.crear_pedido = MagicMock(return_value=self.pedido_mock)

    def test_agregar_plato_mockeado(self):
        # Creamos un plato real
        plato_real = Plato("Hamburguesa", 25.0)

        # El menú devuelve ese plato
        self.menu_mock.obtener_plato.return_value = plato_real

        # Simulamos que el pedido tiene una lista de platos
        self.pedido_mock.platos = []
        self.pedido_mock.calcular_total.return_value = 25.0

        resultado = self.restaurante.agregar_plato_a_pedido(self.pedido_mock, "Hamburguesa")

        self.assertTrue(resultado)
        self.assertEqual(self.pedido_mock.calcular_total(), 25.0)
        self.menu_mock.obtener_plato.assert_called_with("Hamburguesa")
        self.pedido_mock.agregar_plato.assert_called_once_with(plato_real)

    def test_agregar_plato_no_encontrado(self):
        # Simulamos que el menú no encuentra el plato
        self.menu_mock.obtener_plato.return_value = None

        resultado = self.restaurante.agregar_plato_a_pedido(self.pedido_mock, "Café")

        self.assertFalse(resultado)
        self.menu_mock.obtener_plato.assert_called_once_with("Café")
        self.pedido_mock.agregar_plato.assert_not_called()
        self.pedido_mock.calcular_total.assert_not_called()

if __name__ == '__main__':
    unittest.main()

