from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List
import docx


class DocxIngestor(IngestorInterface):

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        df = docx.Document(path)
        quotes = []
        for para in df.paragraphs:
            if para.text != "":
                parse = para.text.split('-')
                qt = QuoteModel(str(parse[0]).strip(), str(parse[1]).strip())
                quotes.append(qt)
        return quotes
