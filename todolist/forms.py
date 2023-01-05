# todolist/forms.py 

from django import forms

from todolist.models import TaskList

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = ["name"]
        
    name = forms.CharField(
        label=False,
        widget=forms.TextInput(
            attrs={
                "aria-label": "name",
                "placeholder": "What do you need to do?",
                "class": "form-control form-control-lg inline-block",
            }
        ),
    )

# create tests for form
'''
class TestTaskForm(TestCase):
    def test_form_instance(self):
        """Test that the form has name field"""
        form = TaskForm()
        self.assertIn("name", form.fields)

    def test_is_valid(self):
       form = TaskForm(data={"name": "Book dentist appointment"})

       self.assertTrue(form.is_valid())

    def test_empty_form_invalid(self):
        form = TaskForm(data={"name": None})

        self.assertFalse(form.is_valid())
'''