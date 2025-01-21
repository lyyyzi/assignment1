'''

Prints the *answers* to a query, as in the collection file, but read from 
a processed file. 
Answers are document IDs and should be printed one per line.

The program will be run from the root of the repository.

'''

import sys

# Suggestion: keep the answers in a dictionary, using the query ID as the key
answers = {}

def read_answers(collection):
    '''
    Reads a processed collection (inside the 'processed' folder).
    '''
    answers_file = './processed/' + collection + extension

    # TODO: fill in the rest


def retrieve_answers_to_query(queryID):
    '''
    Returns the answers to a query given its id
    '''

    # TODO: check for errors

    return answers[queryID]

if __name__ == "__main__":
    '''
    main() function
    '''
    # TODO: read the collection name from command line
    # TODO: read query ID from command line
    # TODO: check for invalid parameters
    # TODO: print the query answers to STDOUT
    exit(0)