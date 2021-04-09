import pytest
from acme import Product
from acme_report import generate_product, ADJECTIVES, NOUNS

#Testing Product class builder
prod = Product('Test Product', 10, 5)


def test_default_product_price():
    '''Test default product price being 10'''
    assert prod.price == 10


def test_default_product_flammability():
    '''Testing default product flammability bieng 0.5'''
    assert prod.flammability == 0.5


def test_product_methods():
    '''Testing product stealability and explode methods'''
    assert prod.stealability() == 'Kinda stealable.'
    assert prod.explode() == '...fizzle.'


#Testing acme_report methods
prod_list = generate_product()


def test_default_num_products():
    '''Testing that length of products generated is 30'''
    assert len(prod_list) == 30


def test_legal_names():
    '''Testing that all names genertated contain item from ADJECTIVES
    and an item from Nouns'''
    assert 'Awesome' in prod_list
    assert 'Anvil' in prod_list


