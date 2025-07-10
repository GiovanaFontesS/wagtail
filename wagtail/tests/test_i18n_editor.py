from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.translation import activate

class TestI18nAdmin(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_superuser(username='admin', email='admin@example.com', password='pass')
        self.client.login(username='admin', password='pass')

    def test_pages_label_ptbr(self):
        activate('pt')
        response = self.client.get(reverse('wagtailadmin_pages:explore_root'))
        self.assertContains(response, "Páginas")

    def test_save_button_translation(self):
        activate('pt')
        response = self.client.get(reverse('wagtailadmin_pages:add', args=('wagtailcore', 'page')))
        self.assertContains(response, "Salvar")

    def test_delete_modal_translation(self):
        activate('pt')
        response = self.client.get(reverse('wagtailadmin_pages:delete', args=(1,)))
        self.assertContains(response, "Excluir")
