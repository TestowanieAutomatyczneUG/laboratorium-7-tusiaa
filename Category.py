class Category:
    def __init__(self, category):
        self.strCategory = ""
        self.strCategoryThumb = ""
        self.strCategoryDescription = ""
        for i in category:
            setattr(self, i, category[i])

    def get(self, attribute: str = "strCategory"):
        if not isinstance(attribute, str):
            raise TypeError
        if hasattr(self, attribute):
            return getattr(self, attribute)

    def set(self, attribute: str, value: str):
        if not isinstance(attribute, str) or not isinstance(value, str):
            raise TypeError
        setattr(self, attribute, value)

    def get_whole_category(self):
        result = self.strCategory
        if self.strCategoryDescription and self.strCategoryDescription.strip():
            result += ":\n" + self.strCategoryDescription
        if self.strCategoryThumb and self.strCategoryThumb.strip():
            result += "\nPhoto: " + self.strCategoryThumb
        return result