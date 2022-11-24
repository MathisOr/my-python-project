import unittest
import Person

class Testing(unittest.TestCase):
    def test_string(self):
        a = 'some'
        b = 'some'
        self.assertEqual(a, b)

    def test_boolean(self):
        a = True
        b = True
        self.assertEqual(a, b)

    def test_failing(self):
        a = 'titi'
        b = 'titi'
        self.assertEqual(a, b)

class TestingPerson(unittest.TestCase):
    def test_id(self):
        person = Person.Person()
        first_id = person.set_name('Alice')
        self.assertEqual(first_id, 0)
        second_id = person.set_name('Bob')
        self.assertEqual(second_id, 1)
        self.assertEquam(first_id, second_id)

if __name__ == '__main__':
    unittest.main()
