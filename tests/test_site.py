from html.parser import HTMLParser
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(); self.meta = {}; self.ids = set(); self.links = []; self.scripts = []
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a: self.ids.add(a['id'])
        if tag == 'meta': self.meta[a.get('name', a.get('property', ''))] = a.get('content', '')
        if tag == 'a': self.links.append(a.get('href', ''))
        if tag == 'script': self.scripts.append(a)

class SiteTests(unittest.TestCase):
    def setUp(self):
        self.text = (ROOT / 'index.html').read_text(); self.page = Page(self.text)
    def test_discovery_and_community_identity(self):
        self.assertIn('Unofficial', self.text)
        self.assertIn('unofficial', self.page.meta['description'].lower())
        self.assertEqual(self.page.meta['og:type'], 'website')
        self.assertEqual(self.page.meta['twitter:card'], 'summary')
    def test_no_invented_origin_or_unpublished_image(self):
        self.assertNotIn('og:url', self.page.meta)
        self.assertNotIn('og:image', self.page.meta)
        self.assertNotIn('rel="canonical"', self.text)
        self.assertEqual(self.page.scripts, [])
    def test_article_anchors(self):
        for anchor in ['jev-social', 'typed-contracts', 'tool-boundaries', 'community-notes']:
            self.assertIn(anchor, self.page.ids)
            self.assertIn('#' + anchor, self.page.links)
    def test_jev_social_case_study_uses_current_release(self):
        self.assertIn('The current release starts each socai child with telemetry disabled', ' '.join(self.text.split()))
        self.assertIn('https://github.com/socai-io/jev-social/releases/latest', self.page.links)
        self.assertIn('https://socai-io.github.io/jev-social/recorded-run/', self.page.links)

if __name__ == '__main__': unittest.main()
