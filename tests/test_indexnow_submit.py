import importlib.util
from pathlib import Path
import tempfile
import unittest

SPEC = importlib.util.spec_from_file_location("indexnow_submit", Path(__file__).parents[1] / "scripts" / "indexnow_submit.py")
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(MODULE)


class IndexNowSubmitTests(unittest.TestCase):
    def test_accepts_only_canonical_content_urls(self):
        self.assertEqual(MODULE.canonical_url("https://nikgo.com/pages/articles/example.html"), "https://nikgo.com/pages/articles/example.html")
        self.assertIsNone(MODULE.canonical_url("http://nikgo.com/pages/articles/example.html"))
        self.assertIsNone(MODULE.canonical_url("https://www.nikgo.com/pages/articles/example.html"))
        self.assertIsNone(MODULE.canonical_url("https://nikgo.com/pages/articles/example.md"))
        self.assertIsNone(MODULE.canonical_url("https://nikgo.com/404.html"))
        self.assertIsNone(MODULE.canonical_url("https://nikgo.com/pages/articles/example.html?preview=true"))

    def test_reader_deduplicates_and_rejects_invalid_urls(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "urls.txt"
            source.write_text("# reviewed\nhttps://nikgo.com/a.html\nhttps://nikgo.com/a.html\nhttps://nikgo.com/a.png\n", encoding="utf-8")
            self.assertEqual(MODULE.read_urls(source), (["https://nikgo.com/a.html"], ["https://nikgo.com/a.png"]))

    def test_dry_run_never_requires_key_or_network(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "urls.txt"
            source.write_text("https://nikgo.com/a.html\n", encoding="utf-8")
            self.assertEqual(MODULE.main(["--dry-run", str(source)]), 0)
