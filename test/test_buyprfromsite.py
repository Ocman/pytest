import pytest
from model.basket_form import basket
from fixture.Application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


# Test1
def test_buy_prod(app):
    app.session.login(username="standard_user", password="secret_sauce")
    app.Product.put_in_basket()
    app.Product.buy(basket(first_name="пнаропаопро", last_name="апрапрапрпа", postal_code="апорапопао"))
    app.session.logout()


# Test2
def test_empty_form(app):
    app.session.login(username="standard_user", password="secret_sauce")
    app.Product.put_in_basket()
    app.Product.buy(basket(first_name=" ", last_name=" ", postal_code=" "))
    app.session.logout()
