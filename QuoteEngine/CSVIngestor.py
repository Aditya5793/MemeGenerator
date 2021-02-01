from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List
import pandas as pd


class CSVIngestor(IngestorInterface):

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        df = pd.read_csv(path, header=0)
        return [QuoteModel(row['body'], row['author'])
                for index, row in df.iterrows()]

        '''for index, row in df.iterrows():
            qt = QuoteModel(row['body'], row['author'])
            quotes.append(qt)

        return quotes '''
