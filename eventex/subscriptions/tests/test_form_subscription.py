from eventex.subscriptions.forms import SubscriptionForm
from django.test import TestCase


class SubscriptionFormTest(TestCase):
    def xtest_form_has_fields(self):
        """Form must have 4 fields"""
        expected = ['name', 'cpf', 'email', 'phone']
        form = SubscriptionForm()
        self.assertSequenceEqual(expected, list(form.fields))


    def test_cpf_is_digit(self):
        """CPF must only accpet digits."""
        form = self.make_validated_form(cpf='ABCD5678901')
        self.assertFormErrorMessage(form, 'cpf', 'digits')


    def test_cpf_has_11_digits(self):
        """CPF must have 11 digits."""
        form = self.make_validated_form(cpf='1234')
        #self.assertListEqual(['cpf'], list(form.errors))
        self.assertFormErrorMessage(form, 'cpf', 'length')


    def test_name_must_be_capitalized(self):
        """Name must be capitalized."""
        form = self.make_validated_form(name='HENRIQUE bastos')
        self.assertEqual('Henrique Bastos', form.cleaned_data['name'])


    def test_email_is_optional(self):
        """email is optional"""
        form = self.make_validated_form(email='')
        self.assertFalse(form.errors)


    def test_phone_is_optional(self):
        """phone is optional"""
        form = self.make_validated_form(phone='')
        self.assertFalse(form.errors)

    def test_phone_is_empty_and_email_is_invalid(self):
        """phone is empty and email is invalid"""
        form = self.make_validated_form(phone='', email="abc")
        self.assertListEqual(['email', '__all__'], list(form.errors))

    def test_must_inform_email_or_phone(self):
        """email and phone are optional, but one must be informed."""
        form = self.make_validated_form(email='',phone='')
        self.assertListEqual(['__all__'], list(form.errors))


    def assertFormErrorMessage(self, form, field, code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        error_code = errors_list[0].code
        self.assertEqual(code, error_code)


    @classmethod
    def make_validated_form(self, **kwargs):
        valid = dict(name = 'Henrique Bastos', cpf = '12345678901',
        email='henrique@bastos.net', phone='21-996186180')
        data = dict(valid, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form