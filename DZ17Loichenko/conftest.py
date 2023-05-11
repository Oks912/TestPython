import pytest
from DZ17Loichenko.code_13DZ import Art_gallery, Renaissance, Realism, Modernism


@pytest.fixture(scope='module')
def renaissance():
    return Renaissance()

@pytest.fixture(scope='module')
def realism():
    return Realism()

@pytest.fixture(scope='module')
def modernism():
    return Modernism()


@pytest.fixture(scope='module', params=[Renaissance(), Realism(), Modernism()])
def art_gallery(request):
    return request.param


