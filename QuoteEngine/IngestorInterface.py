from abc import ABCMeta, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABCMeta):

    extensions = ['txt', 'csv', 'pdf', 'docx']

    @classmethod
    def can_ingest(cls, file_extension):
        return file_extension in cls.extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass
