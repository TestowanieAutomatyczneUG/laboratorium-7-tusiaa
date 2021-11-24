import requests
import unittest
from assertpy import assert_that
from Ingredient import Ingredient

i = requests.get('http://www.themealdb.com/api/json/v1/1/list.php?i=list')
i = i.json()["meals"][0]

class IngredientTest(unittest.TestCase):
    def setUp(self):
        self.temp = Ingredient(i)

    def test_get_ingredient(self):
        assert_that(self.temp.get()).is_equal_to("Chicken")

    def test_get_description(self):
        assert_that(self.temp.get("strDescription")).starts_with("The chicken is").ends_with("III.")

    def test_get_type(self):
        assert_that(self.temp.get("strType")).is_none()

    def test_get_wrong_attribute(self):
        assert_that(self.temp.get("strWrong")).is_none()

    def test_set_Ingredient(self):
        self.temp.set("strIngredient","Cheese")
        assert_that(self.temp.get()).is_equal_to("Cheese")

    def test_set_description(self):
        self.temp.set("strDescription","Chicken is cool")
        assert_that(self.temp.get("strDescription")).is_equal_to("Chicken is cool")

    def test_set_type(self):
        self.temp.set("strType","meat")
        assert_that(self.temp.get("strType")).is_equal_to("meat")

    def test_set_new_attribute(self):
        self.temp.set("strNew","New")
        assert_that(self.temp.get("strNew")).is_equal_to("New")

    def test_get_whole_ingredient(self):
        assert_that(self.temp.get_whole_ingredient()).starts_with("Chicken:").contains("Genetic studies").ends_with("III.")

    def test_get_wrong_attribute_number(self):
        assert_that(self.temp.get).raises(TypeError).when_called_with(1)
    
    def test_get_ingredient_wrong_attribute_float(self):
        assert_that(self.temp.get).raises(TypeError).when_called_with(2.5)

    def test_get_ingredient_wrong_attribute_list(self):
        assert_that(self.temp.get).raises(TypeError).when_called_with([1,2,3])

    def test_get_ingredient_wrong_attribute_object(self):
        assert_that(self.temp.get).raises(TypeError).when_called_with({"a":1,"b":2})

    def test_get_ingredient_wrong_attribute_boolean(self):
        assert_that(self.temp.get).raises(TypeError).when_called_with(True)

    def test_get_ingredient_wrong_attribute_none(self):
        assert_that(self.temp.get).raises(TypeError).when_called_with(None)

    def test_set_ingredient_wrong_attribute_number(self):
        assert_that(self.temp.set).raises(TypeError).when_called_with(1,"value")

    def test_set_ingredient_wrong_attribute_float(self):
        assert_that(self.temp.set).raises(TypeError).when_called_with(2.5,"value")

    def test_set_ingredient_wrong_attribute_list(self):
        assert_that(self.temp.set).raises(TypeError).when_called_with([1,2,3],"value")

    def test_set_ingredient_wrong_attribute_object(self):
        assert_that(self.temp.set).raises(TypeError).when_called_with({"a":1,"b":2},"value")

    def test_set_ingredient_wrong_attribute_boolean(self):
        assert_that(self.temp.set).raises(TypeError).when_called_with(True,"value")

    def test_set_ingredient_wrong_attribute_none(self):
        assert_that(self.temp.set).raises(TypeError).when_called_with(None,"value")

    def test_set_ingredient_wrong_value_number(self):
        assert_that(self.temp.set).raises(TypeError).when_called_with("attribute",1)

    def test_set_ingredient_wrong_value_float(self):  
        assert_that(self.temp.set).raises(TypeError).when_called_with("attribute",2.5)

    def test_set_ingredient_wrong_value_list(self):
        assert_that(self.temp.set).raises(TypeError).when_called_with("attribute",[1,2,3])

    def test_set_ingredient_wrong_value_object(self):
        assert_that(self.temp.set).raises(TypeError).when_called_with("attribute",{"a":1,"b":2})

    def test_set_ingredient_wrong_value_boolean(self):
        assert_that(self.temp.set).raises(TypeError).when_called_with("attribute",True)

    def test_set_ingredient_wrong_value_none(self):
        assert_that(self.temp.set).raises(TypeError).when_called_with("attribute",None)

