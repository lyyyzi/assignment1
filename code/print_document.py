'''

Prints the *contents* of a document, as in the corpus, but read from 
a processed file.

The program will be run from the root of the repository.

'''

import sys

# Suggestion: keep the documents in a dictionary, using the ID as the key
documents = {}

def read_documents(collection):
    '''
    Reads a processed collection (inside the 'processed' folder).
    '''
    corpus_file = './processed/' + collection + extension

    # TODO: fill in the rest


def retrieve_document(docID):
    '''
    Returns a document given its id
    '''

    # TODO: check for errors
    
    return documents[docID]


if __name__ == "__main__":
    '''
    main() function
    '''
    # TODO: read the collection name from command line
    # TODO: read document ID from command line
    # TODO: check for invalid parameters
    # TODO: print the document to STDOUT

    exit(0)