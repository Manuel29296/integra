import unittest
from menu import Plato, Menu

class TestMenu(unittest.TestCase):

    def test_crear_plato(self):
        plato = Plato("Pizza", 15.5)
        self.assertEqual(plato.nombre, "Pizza")
        self.assertEqual(plato.precio, 15.5)
        self.assertEqual(str(plato), "Pizza - $15.50")

    def test_agregar_y_obtener_plato(self):
        menu = Menu()
        menu.agregar_plato("Sopa", 7.0)
        plato = menu.obtener_plato("Sopa")
        self.assertIsNotNone(plato)
        self.assertEqual(plato.nombre, "Sopa")
        self.assertEqual(plato.precio, 7.0)

    def test_obtener_plato_inexistente(self):
        menu = Menu()
        self.assertIsNone(menu.obtener_plato("Taco"))

if __name__ == '__main__':
    unittest.main()
