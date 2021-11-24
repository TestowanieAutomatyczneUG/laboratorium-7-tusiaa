from datetime import date
from Category import Category
from Ingredient import Ingredient

class Meal:
    def __init__(self, meal):
        for i in meal:
            if "Category" in i and type(meal[i]) != Category:
                setattr(self, i, Category({ "strCategory": meal[i] }))
            elif "Ingredient" in i and type(meal[i]) == str and meal[i] and meal[i].strip():
                setattr(self, i, Ingredient({ "strIngredient": meal[i] }))
            else:
                setattr(self, i, meal[i])

    def get(self, attribute: str = "strMeal"):
        if not isinstance(attribute, str):
            raise TypeError
        if hasattr(self, attribute):
            return getattr(self, attribute)

    def set(self, attribute: str, value):
        if not isinstance(attribute, str):
            raise TypeError
        if "Category" in attribute and type(value) != Category:
            setattr(self, attribute, Category({ "strCategory": value }))
        elif "Ingredient" in attribute and type(value) != Ingredient:
            setattr(self, attribute, Ingredient({ "strIngredient": value }))
        elif type(value) == str or type(value) == Category or type(value) == Ingredient:
            setattr(self, attribute, value)
        else:
            raise TypeError
        self.dateModified = date.today()

    def get_ingredients(self):
        ingredients = []
        for i in dir(self):
            if i.startswith('strIngredient'):
                if type(self.get(i)) != str and self.get(i):
                    ingredients.append(getattr(self, i).strIngredient)
        return ingredients

    def get_measures(self):
        measures = []
        for i in dir(self):
            if i.startswith('strMeasure'):
                if self.get(i) and self.get(i).strip():
                    measures.append(getattr(self, i))
        return measures

    def get_ingredients_measures(self):
        ingredients = self.get_ingredients()
        measures = self.get_measures()
        ingredients_measures = []
        for i in range(len(ingredients)):
            ingredients_measures.append((ingredients[i], measures[i]))
        return ingredients_measures

    def add_ingredient(self, ingredient: Ingredient, measure: str):
        if not isinstance(ingredient, Ingredient):
            raise TypeError
        if not isinstance(measure, str):
            raise TypeError
        for i in dir(self):
            if i.startswith('strIngredient'):
                if type(self.get(i)) == str or not self.get(i):
                    setattr(self, i, ingredient)
                    break
        for i in dir(self):
            if i.startswith('strMeasure'):
                if not (self.get(i) and self.get(i).strip()):
                    setattr(self, i, measure)
                    break 
        self.dateModified = date.today()

    def remove_ingredient_by_name(self, ingredient: str):
        if not isinstance(ingredient, str):
            raise TypeError
        place = 0
        if self.check_ingredient(ingredient):
            for i in dir(self):
                if i.startswith('strIngredient'):
                    if type(self.get(i)) == Ingredient and self.get(i).strIngredient == ingredient:
                        setattr(self, i, "")
                        break
                    place += 1
            for i in dir(self):
                if i.startswith('strMeasure'):
                    if place == 0:
                        setattr(self, i, "")
                        break
                    place -= 1
            self.dateModified = date.today()

    def add_tag(self, tag: str):
        if not isinstance(tag, str):
            raise TypeError
        if tag not in self.get("strTags"):
            self.strTags += ", " + tag
            self.dateModified = date.today()

    def remove_tag(self, tag: str):
        if not isinstance(tag, str):
            raise TypeError
        if self.check_tag(tag):
            self.strTags = self.strTags.replace(tag, "").replace(",,",",").replace(", ,",",")
            self.dateModified = date.today()

    def get_recipe(self):
        recipe = "\n" + self.get() + "\n"
        recipe += "\nIngredients:\n"
        ingredients_measures = self.get_ingredients_measures()
        for i in range(len(ingredients_measures)):
            recipe += ingredients_measures[i][0] + ": " + ingredients_measures[i][1] + "\n"
        recipe += "\nInstructions:\n"
        recipe += self.get("strInstructions")
        return recipe
    
    def get_recipe_with_tags(self):
        recipe = "\n" + self.get() + "\n"
        if self.get("strTags") and self.get("strTags").strip():
            recipe += "\nTags: " + self.get("strTags") + "\n"
        recipe += "\nIngredients:\n"
        ingredients_measures = self.get_ingredients_measures()
        for i in range(len(ingredients_measures)):
            recipe += ingredients_measures[i][0] + ": " + ingredients_measures[i][1] + "\n"
        recipe += "\nInstructions:\n"
        recipe += self.get("strInstructions")
        return recipe
    
    def check_ingredient(self, ingredient: str):
        if not isinstance(ingredient, str):
            raise TypeError
        if ingredient in self.get_ingredients():
            return True
        return False

    def check_measure_for_ingredient(self, ingredient: str):
        if not isinstance(ingredient, str):
            raise TypeError
        if ingredient in self.get_ingredients():
            ingredients_measures = self.get_ingredients_measures()
            for i in range(len(ingredients_measures)):
                if ingredients_measures[i][0] == ingredient:
                    return ingredients_measures[i][1]

    def check_tag(self, tag: str):
        if not isinstance(tag, str):
            raise TypeError
        if tag in self.get("strTags"):
            return True
        return False