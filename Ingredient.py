class Ingredient:
    def __init__(self, ingredient):
        self.strIngredient = ""
        self.strDescription = ""
        self.strType = ""
        for i in ingredient:
            setattr(self, i, ingredient[i])

    def get(self, attribute: str = "strIngredient"):
        if not isinstance(attribute, str):
            raise TypeError
        if hasattr(self, attribute):
            return getattr(self, attribute)

    def set(self, attribute: str, value: str):
        if not isinstance(attribute, str) or not isinstance(value, str):
            raise TypeError
        setattr(self, attribute, value)

    def get_whole_ingredient(self):
        result = ""
        if self.strType and self.strType.strip():
            result += "Type:" + self.strType + ", "
        result += self.strIngredient
        if self.strDescription and self.strDescription.strip():
            result += ":\n" + self.strDescription
        return result