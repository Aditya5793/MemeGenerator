from .IngestorInterface import IngestorInterface
from .TXTIngestor import TxtIngestor
from .DocxIngestor import DocxIngestor
from .PDFIngestor import PDFIngestor
from .CSVIngestor import CSVIngestor
from .QuoteModel import QuoteModel


class Ingestor(IngestorInterface):
    @classmethod
    def parse(cls, path):
        print("Ingestor: ", path)
        file_extension = path.split('.')[-1]
        if not cls.can_ingest(file_extension):
            raise ValueError("Unsupported file extension:", file_extension)
        if file_extension == 'txt':
            return TxtIngestor.parse(path)
        if file_extension == 'docx':
            return DocxIngestor.parse(path)
        if file_extension == 'pdf':
            return PDFIngestor.parse(path)
        if file_extension == 'csv':
            return CSVIngestor.parse(path)
