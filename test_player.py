import unittest
import person
 
class TestPersonClass(unittest.TestCase):
    def test_init_id(self):
        test_person = person.Person("Jennifer", "curious student")
        expected = "Jennifer"
        self.assertEqual(test_person.get_id(), expected)
 
    def test_init_desc(self):
        test_person = person.Person("Jennifer", "curious student")
        expected = "curious student"
        self.assertEqual(test_person.get_desc(), expected)