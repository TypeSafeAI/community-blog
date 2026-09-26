from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


def luminance(value):
    channels = [int(value[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    channels = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in channels]
    return sum(c * w for c, w in zip(channels, (0.2126, 0.7152, 0.0722)))


class FocusTests(unittest.TestCase):
    def test_focus_uses_the_surface_text_color(self):
        source = (ROOT / 'index.html').read_text()
        ring = re.search(r'a:focus-visible\s*\{([^}]+)\}', source)
        self.assertIsNotNone(ring)
        self.assertIn('outline: 3px solid currentColor', ring.group(1))
        self.assertIn('a { color: inherit;', source)
        hero = re.search(r'\.hero\s*\{([^}]+)\}', source).group(1)
        self.assertIn('color: #ffffff', hero)
        self.assertIn('background: #14213d', hero)
        for foreground, background in [('#ffffff', '#14213d'), ('#14213d', '#ffffff'), ('#14213d', '#f5f7fb')]:
            light, dark = sorted((luminance(foreground), luminance(background)), reverse=True)
            self.assertGreaterEqual((light + 0.05) / (dark + 0.05), 3)


if __name__ == '__main__':
    unittest.main()
