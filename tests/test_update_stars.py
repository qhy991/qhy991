import io
import json
import tempfile
import unittest
from datetime import date
from pathlib import Path
from unittest.mock import patch

from scripts.update_stars import Stars, fetch_total_stars, refresh, render_svg, update_asset


def repository(stars=1, owner="qhy991", private=False, **extra):
    return {
        "owner": {"login": owner},
        "private": private,
        "stargazers_count": stars,
        **extra,
    }


def response(repositories):
    return io.BytesIO(json.dumps(repositories).encode())


class UpdateStarsTests(unittest.TestCase):
    @patch("scripts.update_stars.urlopen")
    def test_pagination_includes_more_than_200_repositories(self, open_url):
        open_url.side_effect = [
            response([repository(1)] * 100),
            response([repository(2)] * 100),
            response([repository(7)]),
        ]
        self.assertEqual(fetch_total_stars(), Stars(307, 201))
        self.assertEqual(open_url.call_count, 3)
        self.assertIn("page=3", open_url.call_args.args[0].full_url)

    @patch("scripts.update_stars.urlopen")
    def test_owned_public_forks_and_archived_repositories_count(self, open_url):
        open_url.return_value = response([
            repository(10, fork=True),
            repository(20, archived=True),
            repository(3, owner="QHY991"),
            repository(200, owner="another-owner"),
            repository(100, private=True),
        ])
        self.assertEqual(fetch_total_stars(), Stars(33, 3))

    @patch("scripts.update_stars.urlopen")
    def test_failed_or_malformed_later_page_preserves_asset(self, open_url):
        with tempfile.TemporaryDirectory() as directory:
            asset = Path(directory) / "stars.svg"
            asset.write_text("previous valid asset", encoding="utf-8")
            for failure in [OSError("network unavailable"), response({"message": "bad page"})]:
                with self.subTest(failure=type(failure).__name__):
                    open_url.side_effect = [response([repository()] * 100), failure]
                    with self.assertRaises((OSError, ValueError)):
                        refresh(asset, date(2026, 10, 12))
                    self.assertEqual(asset.read_text(encoding="utf-8"), "previous valid asset")

    def test_identical_counts_and_date_do_not_rewrite_asset(self):
        with tempfile.TemporaryDirectory() as directory:
            asset = Path(directory) / "stars.svg"
            svg = render_svg(Stars(1234, 201), date(2026, 10, 12))
            self.assertTrue(update_asset(asset, svg))
            modified = asset.stat().st_mtime_ns
            self.assertFalse(update_asset(asset, render_svg(Stars(1234, 201), date(2026, 10, 12))))
            self.assertEqual(asset.stat().st_mtime_ns, modified)
            self.assertIn("1,234", asset.read_text(encoding="utf-8"))
            self.assertIn("2026-10-12 UTC", svg)


if __name__ == "__main__":
    unittest.main()
