import requests
import unittest
from assertpy import assert_that
from Category import Category

c = requests.get('http://www.themealdb.com/api/json/v1/1/categories.php')
c = c.json()["categories"][0]

class CategoryTest(unittest.TestCase):
    def setUp(self):
        self.temp = Category(c)

    def test_get_category(self):
        assert_that(self.temp.get()).is_equal_to("Beef")

    def test_get_category_description(self):
        assert_that(self.temp.get("strCategoryDescription")).starts_with("Beef is the culinary name").ends_with(".[2]")

    def test_get_category_photo(self):
        assert_that(self.temp.get("strCategoryThumb")).starts_with("https://www.").ends_with("beef.png")

    def test_get_wrong_attribute(self):
        assert_that(self.temp.get("strWrong")).is_none()

    def test_set_category(self):
        self.temp.set("strCategory","Chicken")
        assert_that(self.temp.get()).is_equal_to("Chicken")

    def test_set_category_description(self):
        self.temp.set("strCategoryDescription","Chicken is cool")
        assert_that(self.temp.get("strCategoryDescription")).is_equal_to("Chicken is cool")

    def test_set_category_photo(self):
        self.temp.set("strCategoryThumb","https://www.chicken.png")
        assert_that(self.temp.get("strCategoryThumb")).is_equal_to("https://www.chicken.png")

    def test_set_new_attribute(self):
        self.temp.set("strNew","New")
        assert_that(self.temp.get("strNew")).is_equal_to("New")

    def test_get_whole_category(self):
        assert_that(self.temp.get_whole_category()).starts_with("Beef:").contains("Beef is the culinary name").ends_with("beef.png")

    def test_get_category_wrong_attribute_number(self):
        assert_that(self.temp.get).raises(TypeError).when_called_with(1)
    
    def test_get_category_wrong_attribute_float(self):
        assert_that(self.temp.get).raises(TypeError).when_called_with(2.5)

    def test_get_category_wrong_attribute_list(self):
        assert_that(self.temp.get).raises(TypeError).when_called_with([1,2,3])

    def test_get_category_wrong_attribute_object(self):
        assert_that(self.temp.get).raises(TypeError).when_called_with({"a":1,"b":2})

    def test_get_category_wrong_attribute_boolean(self):
        assert_that(self.temp.get).raises(TypeError).when_called_with(True)

    def test_get_category_wrong_attribute_none(self):
        assert_that(self.temp.get).raises(TypeError).when_called_with(None)

    def test_set_category_wrong_attribute_number(self):
        assert_that(self.temp.set).raises(TypeError).when_called_with(1,"value")

    def test_set_category_wrong_attribute_float(self):
        assert_that(self.temp.set).raises(TypeError).when_called_with(2.5,"value")

    def test_set_category_wrong_attribute_list(self):
        assert_that(self.temp.set).raises(TypeError).when_called_with([1,2,3],"value")

    def test_set_category_wrong_attribute_object(self):
        assert_that(self.temp.set).raises(TypeError).when_called_with({"a":1,"b":2},"value")

    def test_set_category_wrong_attribute_boolean(self):
        assert_that(self.temp.set).raises(TypeError).when_called_with(True,"value")

    def test_set_category_wrong_attribute_none(self):
        assert_that(self.temp.set).raises(TypeError).when_called_with(None,"value")

    def test_set_category_wrong_value_number(self):
        assert_that(self.temp.set).raises(TypeError).when_called_with("attribute",1)

    def test_set_category_wrong_value_float(self):  
        assert_that(self.temp.set).raises(TypeError).when_called_with("attribute",2.5)

    def test_set_category_wrong_value_list(self):
        assert_that(self.temp.set).raises(TypeError).when_called_with("attribute",[1,2,3])

    def test_set_category_wrong_value_object(self):
        assert_that(self.temp.set).raises(TypeError).when_called_with("attribute",{"a":1,"b":2})

    def test_set_category_wrong_value_boolean(self):
        assert_that(self.temp.set).raises(TypeError).when_called_with("attribute",True)

    def test_set_category_wrong_value_none(self):
        assert_that(self.temp.set).raises(TypeError).when_called_with("attribute",None)

    

