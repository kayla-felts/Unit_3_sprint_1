from random import randint, sample, uniform
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_product(num_prod=30):
    products = []
    # TODO

    while num_prod > 0:
        num_prod -= 1

        name1 = sample(ADJECTIVES, k=1)
        name2 = sample(NOUNS, k=1)
        name = name1 + name2
        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = uniform(0.0, 2.5)

        prod = Product(name, price, weight, flammability)
        products.append(prod)

    return products


def inventory_report(products):
    pass  # TODO
    for p in products:
        return p
    print('Unique product names:', len(products))
    print('Average price:', sum(products.price) / len(prodicts))
    print('Average weight:', sum(products.weight) / len(products))
    print('Average flammability:', sum(products.flammability) / len(products))

if __name__ == '__main__':
    inventory_report(generate_product())

    