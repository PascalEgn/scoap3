import math

from django.core.files.storage import storages
from django.core.management.base import BaseCommand, CommandParser

from scoap3.tasks import migrate_legacy_records


class Command(BaseCommand):
    help = "Load records into scoap3"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "--path",
            type=str,
            required=True,
            help="Directory of the legacy_records version",
        )

        parser.add_argument(
            "--batch-size",
            type=int,
            default=1000,
            required=False,
            help="Batchsize to migrate per task.",
        )

        parser.add_argument(
            "--migrate-files",
            type=bool,
            default=True,
            required=False,
            help="Should the ArticleFiles entries get created?",
        )

        parser.add_argument(
            "--filename",
            type=str,
            default=None,
            required=False,
            help="Filename of specific file to migrate.",
        )

    def handle(self, *args, **options):
        storage = storages["legacy-records"]
        amount_total = len(storage.listdir(options["path"])[1])
        self.stdout.write(f"Found {amount_total} files")
        for idx in range(math.ceil(amount_total / options["batch_size"])):
            lower_index = int(idx) * options["batch_size"]
            upper_index = min(
                int(idx) * options["batch_size"] + options["batch_size"], amount_total
            )
            index_range = [lower_index, upper_index]
            self.stdout.write(f"Sending task with index range {index_range}")
            migrate_legacy_records.delay(
                options["path"],
                index_range,
                options["migrate_files"],
                options["filename"],
            )
