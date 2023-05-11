import pytest
from DZ17Loichenko.code_13DZ import Art_gallery, Renaissance, Realism, Modernism


@pytest.mark.smoke
def test_renaissance(renaissance):
    assert isinstance(renaissance, Art_gallery)
    assert renaissance.name == "Secret Supper"
    assert renaissance.artist == 'Leonardo da Vinci'
    assert renaissance.size == '460 см × 880 см'
    assert renaissance.technique == 'tempers'

@pytest.mark.smoke
def test_realism(realism):
    assert isinstance(realism, Art_gallery)
    assert realism.name == "Potato Pickers"
    assert realism.artist == 'Jean-Francois'
    assert realism.size == '83,8 см * 111,8 см.'
    assert realism.technique == 'oil paints on canvas.'

@pytest.mark.regression
def test_modernism(modernism):
    assert isinstance(modernism, Art_gallery)
    assert modernism.name == "The Night"
    assert modernism.artist == 'Modigliani'
    assert modernism.size == '65.4 см x 81.3 см'
    assert modernism.technique == 'oil paints on canvas.'
    assert modernism.ticket_count == 0
    modernism.show()
    assert modernism.ticket_count == 1
    modernism.show()
    assert modernism.ticket_count == 2
    modernism.show()
    assert modernism.ticket_count == 3
    assert modernism.discount == "You have discount ticket"


@pytest.mark.parametrize("artist_name", ["Leonardo da Vinci","Jean-Francois", "Modigliani"])
def test_set_artist(art_gallery, artist_name):
    assert art_gallery.artist == artist_name