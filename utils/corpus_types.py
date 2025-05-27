from typing import Dict, List, Set, Tuple

DocID = int
Token = str
Tokens = List[str]
DocFreq = int
Freq = int
Idf = float
TfIdf = float

Corpus = List[Dict[str, str]]
"""Data structure for XML corpus"""


TokenizedCorpus = List[Dict[str, Tokens]]
"""Data structure for toknized corpus"""


DocTokenFreq = Tuple[DocID, Token, Freq]
"""The frequency of a word in a doc*
Tuple of DocID, Token, Frequency"""

FreqList = List[DocTokenFreq]
"""List of all frequencies of words in a doc"""

TokenFreqDictByDocs = Dict[DocID, Dict[Token, Freq]]
"""To count the number of docs in wich the token appears"""

TokenAndDocID = Tuple[Token, DocID]
"""(Token, DocID)"""

TokensAndDocIDsSet = Set[TokenAndDocID]
"""Set(Token, DocID)"""

IdfDict = Dict[Token, Idf]
"""Idf value of the token"""

TokenTfIdf = Tuple[DocID, Token, TfIdf]
"""Tuple of DocID, Token and TfIdf"""

TokenPositionII = Dict[Token, Dict[DocID, List[int]]]

DateII = List[Tuple[int, List[DocID]]]

ImageII = Dict[bool, List[DocID]]
