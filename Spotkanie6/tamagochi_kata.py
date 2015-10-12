import pytest

@pytest.fixture
def kiki():
    return Tamagochi()


def test_tamagochi_feed(kiki):
    hunger_level = kiki.get_hunger()
    kiki.feed()
    assert kiki.get_hunger() < hunger_level

def test_tamagochi_decrease_hunger_on_each_feed(kiki):
    hunger_level = kiki.get_hunger()
    kiki.feed()
    hunger_level2 = kiki.get_hunger()
    assert hunger_level2 < hunger_level
    kiki.feed()
    assert kiki.get_hunger() < hunger_level2

def test_tamagochi_increase_fatigue(kiki):
    fatigue_level = kiki.get_fatigue()
    kiki.feed()
    assert kiki.get_fatigue() > fatigue_level

class Tamagochi:

    def __init__(self):
        self.hunger_level = 42
        self.fatigue_level = 0

    def feed(self):
        self.hunger_level -= 1
        self.fatigue_level += 1

    def get_hunger(self):
        return self.hunger_level

    def get_fatigue(self):
        return self.fatigue_level