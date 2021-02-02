from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List
import subprocess
import os
import random
import platform 
from .TXTIngestor import TxtIngestor

class PDFIngestor(IngestorInterface):
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        txt = './pdfInText.txt'
        if platform.system() == 'Windows':
            cmd = r"""{} "{}" "{}" """.format("pdftotext_windows -layout -nopgbrk", path, txt)
        else:
            cmd = r"""{} "{}" "{}" """.format("./pdftotext_Linux -layout -nopgbrk", path, txt) 
        subprocess.call(cmd, shell=True, stderr=subprocess.STDOUT)
        quotes = TxtIngestor.parse(txt)
        os.remove(txt)
        return quotes
