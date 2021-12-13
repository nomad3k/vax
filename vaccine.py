from datetime import date, timedelta

class Vaccine:

    foo: str
    __name: str
    __friendly_name: str
    __manufacturer: str
    __brand: str
    __product_codes: [str]
    __doses: int
    __interval: int

    @property
    def name(self) -> str: return self.__name

    @property
    def friendly_name(self) -> str: return self.__friendly_name

    def rename(self, name: str, friendly_name: str):
        assert name != "", "name must not be empty"
        assert friendly_name != "", "friendly_name must not be empty"
        self.__name = name
        self.__friendly_name = friendly_name
        return self

    @property
    def manufacturer(self) -> str: return self.__manufacturer

    @property
    def brand(self) -> str: return self.__brand

    def classify(self, manufacturer: str, brand: str):
        assert manufacturer != "", "manufacturer must not be empty"
        assert brand != "", "brand must not be empty"
        self.__manufacturer = manufacturer
        self.__brand = brand
        return self

    @property
    def product_codes(self) -> [str]: return self.__product_codes

    @property
    def doses(self) -> int: return self.__doses

    @property
    def interval(self): return self.__interval

    def configure(self, doses: int = 2, interval: int = 21):
        assert doses >= 1, "doses must be 1+"
        assert interval >= 0, "interval must be 0+"
        self.__doses = doses
        self.__interval = interval
        return self

    def satisfies_interval(self, a: date, b: date) -> bool:
        return (b - a).days >= self.__interval

    def add_product_code(self, product_code):
        if self.has_product_code(product_code):
            raise KeyError("Product Code exists")
        self.__product_codes.append(product_code)
        return self

    def has_product_code(self, product_code):
        return self.__product_codes.__contains__(product_code)

    def __init__(self, name, friendly_name):
        self.rename(name, friendly_name)
        self.configure()
        self.__product_codes = []
