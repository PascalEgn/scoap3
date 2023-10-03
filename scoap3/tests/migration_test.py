import pytest

from scoap3.articles.models import Article
from scoap3.tasks import migrate_legacy_records

pytestmark = pytest.mark.django_db


class TestMigration:
    def test_authors(self):
        migrate_legacy_records("./tests", [0, 1], True, "44233.json")
        for article in Article.objects.all():
            print(article)

        assert False
