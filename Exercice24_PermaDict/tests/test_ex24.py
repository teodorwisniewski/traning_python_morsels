
from Exercice24_PermaDict.Exercice24_PermaDict import PermaDict
import pytest

class TestEx24:

    def test_BasicPart(self):

        locations = PermaDict([('Cos', "Houston"), ('Bla', 1)])
        assert list(locations) == ["Cos","Bla"]
        assert list(locations.values()) == ["Houston",1]
        assert list(locations.items()) == [('Cos', "Houston"), ('Bla', 1)]

    def test_dict_subclass(self):
        locations = PermaDict([('Cos', "Houston"), ('Bla', 1)])
        assert hasattr(locations,"__setitem__")
        assert hasattr(locations,"__getitem__")
        assert hasattr(locations,"force_set")

    def test_raise_exception(self):
        locations = PermaDict([('Cos', "Houston"), ('Bla', 1)])
        with pytest.raises(KeyError) as e_info:
            locations["Cos"] = 33
        assert e_info.value.args[0] == "'Cos' already in dictionary."
        with pytest.raises(KeyError) as update_error:
            locations.update(Cos=55)
        assert update_error.value.args[0] == "'Cos' already in dictionary."

    def test_force_set(self):
        locations = PermaDict({'David': "Boston"})
        locations.force_set('David', "Amsterdam")
        locations.force_set('Asheesh', "Boston")
        locations.force_set('Asheesh', "San Francisco")
        assert dict(locations) ==  {'David': 'Amsterdam', 'Asheesh': 'San Francisco'}

    def test_silent_argument(self):
        locations = PermaDict({'David': "Boston"}, silent=True)
        locations['David'] = "Amsterdam"
        locations['Asheesh'] = "Boston"
        print(dict(locations))
        assert dict(locations) == {'David': 'Boston', 'Asheesh': 'Boston'}

    def test_forced_update(self):
        locations = PermaDict({'David': "Boston"})
        locations.update([('David', 'Amsterdam'), ('Asheesh', 'SF')], force=True)
        assert dict(locations) == {'David': 'Amsterdam', 'Asheesh': 'SF'}
