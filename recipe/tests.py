from django.test import TestCase
from .models import Category, Recipe

class CategoryModelTest(TestCase):
    def test_category_creation(self):
        category = Category.objects.create(name="Desserts")
        self.assertEqual(category.name, "Desserts")
        self.assertEqual(str(category), "Desserts")
    
    def test_category_iter(self):
        category = Category.objects.create(name="Desserts")
        self.assertEqual(list(category), ["Desserts"])

class RecipeModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Desserts")
    
    def test_recipe_creation(self):
        recipe = Recipe.objects.create(
            title="Chocolate Cake",
            description="Delicious cake",
            instructions="Mix and bake",
            ingredients="Flour, sugar, cocoa",
            category=self.category
        )
        self.assertEqual(recipe.title, "Chocolate Cake")
        self.assertEqual(recipe.description, "Delicious cake")
        self.assertEqual(recipe.instructions, "Mix and bake")
        self.assertEqual(recipe.ingredients, "Flour, sugar, cocoa")
        self.assertEqual(recipe.category, self.category)
        self.assertTrue(recipe.created_at)
        self.assertTrue(recipe.updated_at)
        self.assertEqual(str(recipe), "Chocolate Cake")