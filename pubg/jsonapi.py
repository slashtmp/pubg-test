import json

class Document:
    def __init__(self, document: dict) -> None:
        if not _valid_jasonapi(document):
            raise TypeError("Not a valid JSON:API document")

        self._document = document
        self._dataIsList = isinstance(document['data'], list)

    def getType():
        pass

    def getId():
        pass

    def getAttribute(attributeName):
        pass

def _valid_jasonapi(document: dict) -> bool:
    """Return true if the document has a valid jsonapi structure"""

    # Mandatory top level members
    topLevelMembers = [ 'data', 'errors', 'meta']
    
    if(len([ k for k in topLevelMembers if k in document ]) == 0):
        return False
    if( 'data' in document and 'errors' in document):
        return False

    return True

if(__name__ == "__main__"):
    import sys
    for fileName in sys.argv[1:]:
        with open(fileName) as fp:
            doc = json.load(fp)
            if _valid_jasonapi(doc):
                print(f"{fileName} is a valid JSON:API doument.")
            else:
                print(f"{fileName} is NOT a valid JSON:API doument.")