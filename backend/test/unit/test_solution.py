import pytest
import unittest.mock as mock
from src.controllers.recipecontroller import RecipeController

# add your test case implementation here
@pytest.fixture
@mock.patch('src.controllers.recipecontroller.RecipeController.load_recipes', autospec=True)
def sut(mockedLoadRecipes):
    mockedDao = mock.MagicMock()
    mockedLoadRecipes.return_value = []
    sut = RecipeController(mockedDao)

    return sut

@pytest.mark.unit
class TestGetReceipe:
    @pytest.mark.parametrize('mockedReturn, expected', [
        ({}, None),
        ({"first": 0.09, "second": 0.09},  None),
    ])
    @mock.patch('src.controllers.recipecontroller.RecipeController.get_readiness_of_recipes', autospec=True)
    def test_returning_none(self, mockedGetRoR, sut, mockedReturn, expected):
        mockedDiet = mock.MagicMock()
        mockedDiet.name = ""
        mockedGetRoR.return_value = mockedReturn

        resultReadiness = sut.get_recipe(mockedDiet, False)
        assert resultReadiness == expected

    @pytest.mark.parametrize('mockedReturn, expected', [
        ({"first": 0.09, "second": 0.11}, "second"),
    ])
    @mock.patch('src.controllers.recipecontroller.RecipeController.get_readiness_of_recipes', autospec=True)
    @mock.patch('src.controllers.recipecontroller.random.randint', autospec=True)
    def test_with_only_one_valid(self, mockedRandom, mockedGetRoR, sut, mockedReturn, expected):
        mockedDiet = mock.MagicMock()
        mockedDiet.name = ""
        mockedRandom.return_value = 0
        mockedGetRoR.return_value = mockedReturn

        resultReadiness = sut.get_recipe(mockedDiet, True)
        assert resultReadiness == expected

    @pytest.mark.parametrize('mockedReturn, expected', [
        ({"first": 0.10, "second": 0.11}, "second"),
    ])
    @mock.patch('src.controllers.recipecontroller.RecipeController.get_readiness_of_recipes', autospec=True)
    @mock.patch('src.controllers.recipecontroller.random.randint', autospec=True)
    def test_take_best_true(self, mockedRandom, mockedGetRoR, sut, mockedReturn, expected):
        mockedDiet = mock.MagicMock()
        mockedDiet.name = ""
        mockedRandom.return_value = 1
        mockedGetRoR.return_value = mockedReturn

        resultReadiness = sut.get_recipe(mockedDiet, True)
        assert resultReadiness == expected

    @pytest.mark.parametrize('mockedReturn, expected', [
        ({"first": 0.10, "second": 0.11}, "first"),
    ])
    @mock.patch('src.controllers.recipecontroller.RecipeController.get_readiness_of_recipes', autospec=True)
    @mock.patch('src.controllers.recipecontroller.random.randint', autospec=True)
    def test_take_best_false(self, mockedRandom, mockedGetRoR, sut, mockedReturn, expected):
        mockedDiet = mock.MagicMock()
        mockedDiet.name = ""
        mockedRandom.return_value = 1
        mockedGetRoR.return_value = mockedReturn

        resultReadiness = sut.get_recipe(mockedDiet, False)
        assert resultReadiness == expected