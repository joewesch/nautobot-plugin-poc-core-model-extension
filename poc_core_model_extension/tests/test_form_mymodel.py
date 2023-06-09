"""Test mymodel forms."""
from django.test import TestCase

from poc_core_model_extension import forms


class MyModelTest(TestCase):
    """Test MyModel forms."""

    def test_specifying_all_fields_success(self):
        form = forms.MyModelForm(
            data={
                "name": "Development",
                "slug": "development",
                "description": "Development Testing",
            }
        )
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_specifying_only_required_success(self):
        form = forms.MyModelForm(
            data={
                "name": "Development",
                "slug": "development",
            }
        )
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_validate_name_mymodel_is_required(self):
        form = forms.MyModelForm(data={"slug": "development"})
        self.assertFalse(form.is_valid())
        self.assertIn("This field is required.", form.errors["name"])

    def test_validate_slug_is_required(self):
        form = forms.MyModelForm(data={"name": "Development"})
        self.assertFalse(form.is_valid())
        self.assertIn("This field is required.", form.errors["slug"])
