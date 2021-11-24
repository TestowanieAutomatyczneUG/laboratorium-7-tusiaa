import requests
import unittest
from assertpy import assert_that
from Meal import Meal, Category, Ingredient, date

m = requests.get('http://www.themealdb.com/api/json/v1/1/lookup.php?i=52772')
m = m.json()["meals"][0]

ingredient = Ingredient({ "strIngredient": "chicken" })

class MealTest(unittest.TestCase):
    def setUp(self):
        self.temp = Meal(m)

    def test_init_(self):
        assert_that(self.temp).is_not_none()

    def test_get_Name(self):
        assert_that(self.temp.get()).is_equal_to("Teriyaki Chicken Casserole")

    def test_get_Alternate_Drink(self):
        assert_that(self.temp.get("strDrinkAlternate")).is_none()

    def test_get_Category(self):
        assert_that(self.temp.get("strCategory")).is_instance_of(Category)

    def test_get_Area(self):
        assert_that(self.temp.get("strArea")).is_equal_to("Japanese")

    def test_get_Instructions(self):
        assert_that(self.temp.get("strInstructions")).starts_with("Preheat oven").ends_with("Enjoy!")

    def test_get_Thumb(self):
        assert_that(self.temp.get("strMealThumb")).starts_with("https://www.").ends_with(".jpg")

    def test_get_Tags(self):
        assert_that(self.temp.get("strTags")).contains("Meat")

    def test_get_Video(self):
        assert_that(self.temp.get("strYoutube")).starts_with("https://www.youtube.com/")

    def test_get_Ingredient1(self):
        assert_that(self.temp.get("strIngredient1")).is_instance_of(Ingredient)

    def test_get_Ingredient20(self):
        assert_that(self.temp.get("strIngredient20")).is_none()

    def test_get_Measure1(self):
        assert_that(self.temp.get("strMeasure1")).is_equal_to("3/4 cup")

    def test_get_Measure20(self):
        assert_that(self.temp.get("strMeasure20")).is_none()

    def test_get_Source(self):
        assert_that(self.temp.get("strSource")).is_none()
    
    def test_get_Image_Source(self):
        assert_that(self.temp.get("strImageSource")).is_none()

    def test_get_Commons(self):
        assert_that(self.temp.get("strCreativeCommonsConfirmed")).is_none()

    def test_Date_Modified(self):
        self.temp.set("strDrinkAlternate", "Cola")
        assert_that(self.temp.get("dateModified")).is_instance_of(date).is_equal_to(date.today())

    def test_set_Name(self):
        self.temp.set("strMeal", "Pizza")
        assert_that(self.temp.get("strMeal")).is_equal_to("Pizza")

    def test_set_Alternate_Drink(self):
        self.temp.set("strDrinkAlternate", "Cola")
        assert_that(self.temp.get("strDrinkAlternate")).is_equal_to("Cola")

    def test_set_Category(self):
        self.temp.set("srtCategory", "Cheese")
        assert_that(self.temp.get("srtCategory")).is_instance_of(Category)

    def test_set_Area(self):
        self.temp.set("strArea", "Italian")
        assert_that(self.temp.get("strArea")).is_equal_to("Italian")

    def test_set_Instructions(self):
        self.temp.set("strInstructions", "Enjoy!")
        assert_that(self.temp.get("strInstructions")).is_equal_to("Enjoy!")

    def test_set_Thumb(self):
        self.temp.set("strMealThumb", "https://www.google.com")
        assert_that(self.temp.get("strMealThumb")).is_equal_to("https://www.google.com")

    def test_set_Tags(self):
        self.temp.set("strTags", "Cheese")
        assert_that(self.temp.get("strTags")).is_equal_to("Cheese")

    def test_set_Video(self):
        self.temp.set("strYoutube", "https://www.youtube.com/")
        assert_that(self.temp.get("strYoutube")).is_equal_to("https://www.youtube.com/")

    def test_set_Ingredient(self):
        self.temp.set("strIngredient1", "chicken")
        assert_that(self.temp.get("strIngredient1")).is_instance_of(Ingredient)

    def test_set_Measure(self):
        self.temp.set("strMeasure1", "1 cup")
        assert_that(self.temp.get("strMeasure1")).is_equal_to("1 cup")

    def test_set_Source(self):
        self.temp.set("strSource", "https://www.google.com")
        assert_that(self.temp.get("strSource")).is_equal_to("https://www.google.com")

    def test_set_Image_Source(self):
        self.temp.set("strImageSource", "https://www.google.com")
        assert_that(self.temp.get("strImageSource")).is_equal_to("https://www.google.com")

    def test_set_Commons(self):
        self.temp.set("strCreativeCommonsConfirmed", "eat")
        assert_that(self.temp.get("strCreativeCommonsConfirmed")).is_equal_to("eat")

    def test_set_new_attribute(self):
        self.temp.set("strNew", "new")
        assert_that(self.temp.get("strNew")).is_equal_to("new")

    def test_get_Ingredients(self):
        assert_that(self.temp.get_ingredients()).contains("chicken breasts").is_instance_of(list).is_length(9)

    def test_get_Measures(self):
        assert_that(self.temp.get_measures()).contains("2").is_instance_of(list).is_length(9)

    def test_get_Ingredients_Measures(self):
        assert_that(self.temp.get_ingredients_measures()).contains(("chicken breasts", "2")).is_instance_of(list).is_length(9)

    def test_add_Ingredient(self):
        self.temp.add_ingredient( ingredient, "half")
        assert_that(self.temp.get_ingredients_measures()).contains(("chicken","half")).is_instance_of(list).is_length(10)

    def test_remove_Ingredient(self):
        self.temp.remove_ingredient_by_name("chicken breasts")
        assert_that(self.temp.get_ingredients_measures()).does_not_contain(("chicken breasts","2")).is_instance_of(list).is_length(8)

    def test_add_Tag(self):
        self.temp.add_tag("chicken")
        assert_that(self.temp.get("strTags")).contains("chicken").is_instance_of(str)

    def test_remove_Tag(self):
        self.temp.remove_tag("Meat")
        assert_that(self.temp.get("strTags")).does_not_contain("Meat").is_instance_of(str)

    def test_get_recipe(self):
        assert_that(self.temp.get_recipe()).starts_with("\nTeriyaki Chicken Casserole\n").ends_with("Enjoy!").contains("chicken breasts: 2")

    def test_get_recipe_with_tags(self):
        assert_that(self.temp.get_recipe_with_tags()).starts_with("\nTeriyaki Chicken Casserole\n").ends_with("Enjoy!").contains("chicken breasts: 2").contains("Meat")
        
    def test_check_ingredient_true(self):
        assert_that(self.temp.check_ingredient("chicken breasts")).is_true()

    def test_check_ingredient_false(self):
        assert_that(self.temp.check_ingredient("cheese")).is_false()

    def test_check_tag_true(self):
        assert_that(self.temp.check_tag("Meat")).is_true()

    def test_check_tag_false(self):
        assert_that(self.temp.check_tag("Chicken")).is_false()

    def test_check_measure(self):
        assert_that(self.temp.check_measure_for_ingredient("chicken breasts")).is_equal_to("2")

    def test_get_wrong_attribute(self):
        assert_that(self.temp.get("wrong")).is_none()

    def test_get_wrong_attribute_number(self):
        assert_that(self.temp.get).raises(TypeError).when_called_with(1)

    def test_get_wrong_attribute_float(self):
        assert_that(self.temp.get).raises(TypeError).when_called_with(2.5)

    def test_get_wrong_attribute_list(self):
        assert_that(self.temp.get).raises(TypeError).when_called_with([1,2,3])

    def test_get_wrong_attribute_object(self):
        assert_that(self.temp.get).raises(TypeError).when_called_with({1:2,3:4})

    def test_get_wrong_attribute_None(self):
        assert_that(self.temp.get).raises(TypeError).when_called_with(None)

    def test_get_wrong_attribute_boolean(self):
        assert_that(self.temp.get).raises(TypeError).when_called_with(True)

    def test_set_wrong_value_number(self):
        assert_that(self.temp.set).raises(TypeError).when_called_with("attribute", 1)

    def test_set_wrong_value_float(self):
        assert_that(self.temp.set).raises(TypeError).when_called_with("attribute", 2.5)

    def test_set_wrong_value_list(self):
        assert_that(self.temp.set).raises(TypeError).when_called_with("attribute", [1,2,3])

    def test_set_wrong_value_object(self):
        assert_that(self.temp.set).raises(TypeError).when_called_with("attribute", {1:2,3:4})

    def test_set_wrong_value_None(self):
        assert_that(self.temp.set).raises(TypeError).when_called_with("attribute", None)

    def test_set_wrong_value_boolean(self):
        assert_that(self.temp.set).raises(TypeError).when_called_with("attribute", True)

    def test_set_wrong_attribute_number(self):
        assert_that(self.temp.set).raises(TypeError).when_called_with(1, "value")

    def test_set_wrong_attribute_float(self):
        assert_that(self.temp.set).raises(TypeError).when_called_with(2.5, "value")

    def test_set_wrong_attribute_list(self):
        assert_that(self.temp.set).raises(TypeError).when_called_with([1,2,3], "value")
    
    def test_set_wrong_attribute_object(self):
        assert_that(self.temp.set).raises(TypeError).when_called_with({1:2,3:4}, "value")

    def test_set_wrong_attribute_None(self):
        assert_that(self.temp.set).raises(TypeError).when_called_with(None, "value")

    def test_set_wrong_attribute_boolean(self):
        assert_that(self.temp.set).raises(TypeError).when_called_with(True, "value")

    def test_add_ingredient_wrong_ingredient_string(self):
        assert_that(self.temp.add_ingredient).raises(TypeError).when_called_with("ingredient", "measure")

    def test_add_ingredient_wrong_ingredient_number(self):
        assert_that(self.temp.add_ingredient).raises(TypeError).when_called_with(1, "measure")

    def test_add_ingredient_wrong_ingredient_float(self):
        assert_that(self.temp.add_ingredient).raises(TypeError).when_called_with(2.5, "measure")

    def test_add_ingredient_wrong_ingredient_list(self):   
        assert_that(self.temp.add_ingredient).raises(TypeError).when_called_with([1,2,3], "measure")

    def test_add_ingredient_wrong_ingredient_object(self):
        assert_that(self.temp.add_ingredient).raises(TypeError).when_called_with({1:2,3:4}, "measure")

    def test_add_ingredient_wrong_ingredient_None(self):
        assert_that(self.temp.add_ingredient).raises(TypeError).when_called_with(None, "measure")

    def test_add_ingredient_wrong_ingredient_boolean(self):
        assert_that(self.temp.add_ingredient).raises(TypeError).when_called_with(True, "measure")

    def test_add_ingredient_wrong_measure_number(self):
        assert_that(self.temp.add_ingredient).raises(TypeError).when_called_with(ingredient, 1)
    
    def test_add_ingredient_wrong_measure_float(self):
        assert_that(self.temp.add_ingredient).raises(TypeError).when_called_with(ingredient, 2.5)

    def test_add_ingredient_wrong_measure_list(self):
        assert_that(self.temp.add_ingredient).raises(TypeError).when_called_with(ingredient, [1,2,3])

    def test_add_ingredient_wrong_measure_object(self):
        assert_that(self.temp.add_ingredient).raises(TypeError).when_called_with(ingredient, {1:2,3:4})

    def test_add_ingredient_wrong_measure_None(self):
        assert_that(self.temp.add_ingredient).raises(TypeError).when_called_with(ingredient, None)

    def test_add_ingredient_wrong_measure_boolean(self):
        assert_that(self.temp.add_ingredient).raises(TypeError).when_called_with(ingredient, True)

    def test_remove_ingredient_wrong_ingredient_number(self):
        assert_that(self.temp.remove_ingredient_by_name).raises(TypeError).when_called_with(1)
    
    def test_remove_ingredient_wrong_ingredient_float(self):
        assert_that(self.temp.remove_ingredient_by_name).raises(TypeError).when_called_with(2.5)

    def test_remove_ingredient_wrong_ingredient_list(self):
        assert_that(self.temp.remove_ingredient_by_name).raises(TypeError).when_called_with([1,2,3])

    def test_remove_ingredient_wrong_ingredient_object(self):
        assert_that(self.temp.remove_ingredient_by_name).raises(TypeError).when_called_with({1:2,3:4})

    def test_remove_ingredient_wrong_ingredient_None(self):
        assert_that(self.temp.remove_ingredient_by_name).raises(TypeError).when_called_with(None)

    def test_remove_ingredient_wrong_ingredient_boolean(self):
        assert_that(self.temp.remove_ingredient_by_name).raises(TypeError).when_called_with(True)

    def test_add_tag_wrong_tag_number(self):
        assert_that(self.temp.add_tag).raises(TypeError).when_called_with(1)

    def test_add_tag_wrong_tag_float(self):
        assert_that(self.temp.add_tag).raises(TypeError).when_called_with(2.5)

    def test_add_tag_wrong_tag_list(self):
        assert_that(self.temp.add_tag).raises(TypeError).when_called_with([1,2,3])

    def test_add_tag_wrong_tag_object(self):
        assert_that(self.temp.add_tag).raises(TypeError).when_called_with({1:2,3:4})

    def test_add_tag_wrong_tag_None(self):
        assert_that(self.temp.add_tag).raises(TypeError).when_called_with(None)

    def test_add_tag_wrong_tag_boolean(self):
        assert_that(self.temp.add_tag).raises(TypeError).when_called_with(True)

    def test_remove_tag_wrong_tag_number(self):
        assert_that(self.temp.remove_tag).raises(TypeError).when_called_with(1)

    def test_remove_tag_wrong_tag_float(self):
        assert_that(self.temp.remove_tag).raises(TypeError).when_called_with(2.5)

    def test_remove_tag_wrong_tag_list(self):
        assert_that(self.temp.remove_tag).raises(TypeError).when_called_with([1,2,3])

    def test_remove_tag_wrong_tag_object(self):
        assert_that(self.temp.remove_tag).raises(TypeError).when_called_with({1:2,3:4})

    def test_remove_tag_wrong_tag_None(self):
        assert_that(self.temp.remove_tag).raises(TypeError).when_called_with(None)

    def test_remove_tag_wrong_tag_boolean(self):
        assert_that(self.temp.remove_tag).raises(TypeError).when_called_with(True)

    def test_check_tag_wrong_tag_number(self):
        assert_that(self.temp.check_tag).raises(TypeError).when_called_with(1)

    def test_check_tag_wrong_tag_float(self):
        assert_that(self.temp.check_tag).raises(TypeError).when_called_with(2.5)

    def test_check_tag_wrong_tag_list(self):
        assert_that(self.temp.check_tag).raises(TypeError).when_called_with([1,2,3])

    def test_check_tag_wrong_tag_object(self):
        assert_that(self.temp.check_tag).raises(TypeError).when_called_with({1:2,3:4})

    def test_check_tag_wrong_tag_None(self):
        assert_that(self.temp.check_tag).raises(TypeError).when_called_with(None)

    def test_check_tag_wrong_tag_boolean(self):
        assert_that(self.temp.check_tag).raises(TypeError).when_called_with(True)

    def test_check_ingredient_wrong_ingredient_number(self):
        assert_that(self.temp.check_ingredient).raises(TypeError).when_called_with(1)
    
    def test_check_ingredient_wrong_ingredient_float(self):
        assert_that(self.temp.check_ingredient).raises(TypeError).when_called_with(2.5)

    def test_check_ingredient_wrong_ingredient_list(self):
        assert_that(self.temp.check_ingredient).raises(TypeError).when_called_with([1,2,3])

    def test_check_ingredient_wrong_ingredient_object(self):
        assert_that(self.temp.check_ingredient).raises(TypeError).when_called_with({1:2,3:4})

    def test_check_ingredient_wrong_ingredient_None(self):
        assert_that(self.temp.check_ingredient).raises(TypeError).when_called_with(None)

    def test_check_ingredient_wrong_ingredient_boolean(self):
        assert_that(self.temp.check_ingredient).raises(TypeError).when_called_with(True)

    def test_check_measure_wrong_ingredient_number(self):
        assert_that(self.temp.check_measure_for_ingredient).raises(TypeError).when_called_with(1)

    def test_check_measure_wrong_ingredient_float(self):
        assert_that(self.temp.check_measure_for_ingredient).raises(TypeError).when_called_with(2.5)

    def test_check_measure_wrong_ingredient_list(self):
        assert_that(self.temp.check_measure_for_ingredient).raises(TypeError).when_called_with([1,2,3])

    def test_check_measure_wrong_ingredient_object(self):
        assert_that(self.temp.check_measure_for_ingredient).raises(TypeError).when_called_with({1:2,3:4})

    def test_check_measure_wrong_ingredient_None(self):
        assert_that(self.temp.check_measure_for_ingredient).raises(TypeError).when_called_with(None)

    def test_check_measure_wrong_ingredient_boolean(self):
        assert_that(self.temp.check_measure_for_ingredient).raises(TypeError).when_called_with(True)

    def tearDown(self):
        del self.temp

