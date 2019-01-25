from django.test import TestCase

class SpeakerDetailGet(TestCase):
    def setUp(self):
        self.resp = self.client.get('/palestrantes/grace-hoper/')


    def test_get(self):
        """Get should return status 200"""
        self.assertEqual(200, self.resp.status_code)


    def test_template(self):
        self.assertTemplateUsed(self.resp, 'core/speaker_detail.html')


    def test_html(self):
        contents = [
            'Grace Hopper',
            'Programadora e almirante',
            'http://hbn.link/hopper-pic',
            'http://hbn.link/hopper-site',
        ]

        for expected in contents:
            with self.subTest():
                self.assertContains(self.resp, expected)