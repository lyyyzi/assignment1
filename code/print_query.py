'''

Prints the *contents* of a query, as in the collection file, but read from 
a processed file.

The program will be run from the root of the repository.

'''

import sys

# Suggestion: keep the quries in a dictionary, using the ID as the key
queries = {}

def read_queries(collection):
    '''
    Reads a processed collection (inside the 'processed' folder).
    '''
    queries_file = './processed/' + collection + extension

    # TODO: fill in the rest


def retrieve_query(queryID):
    '''
    Returns a query given its id
    '''

    # TODO: check for errors
    
    return queries[queryID]


if __name__ == "__main__":
    '''
    main() function
    '''
    # TODO: read the collection name from command line
    # TODO: read query ID from command line
    # TODO: check for invalid parameters
    # TODO: print the query to STDOUT
    
    exit(0)