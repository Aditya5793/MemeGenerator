from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List


class TxtIngestor(IngestorInterface):

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        quotes = []

        with open(path, 'r') as txt:
            contents = txt.readlines()

            for line in contents:
                ln = line.split('-')
                quotes.append(QuoteModel(ln[0].strip(), ln[1].strip()))

        return quotes
