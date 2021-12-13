from vaccine import Vaccine
from datetime import date


def main():
    print("ok")
    v = Vaccine(name="AstraZeneca", friendly_name="COVID-19 Vaccine AstraZeneca") \
        .classify(manufacturer="AstraZeneca AB", brand="Vaxzevria") \
        .configure(doses=2, interval=21) \
        .add_product_code("foo") \
        .add_product_code("bah") \
        .add_product_code("meep")

    print(v.satisfies_interval(date(2000, 1, 1), date(2000, 1, 21)))


if __name__ == '__main__':
    main()
