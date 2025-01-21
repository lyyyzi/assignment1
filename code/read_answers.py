'''

Reads answers to queries in the collection file into memory and writes
the data structure to the processed folder.

The program will be run from the root of the repository.

'''

import sys

import os
# Suggestion: keep the answers in a dictionary, using the query ID as the key
answers = {}


def read_answers(collection):
    '''
    Reads the answers in the collection (inside the 'collections' folder).
    '''
    extension = ".txt"  # Assuming text file format
    answers_file = os.path.join('collections', collection + extension)

    if not os.path.exists(answers_file):
        print(f"Error: File {answers_file} not found.")
        sys.exit(1)

    try:
        with open(answers_file, 'r') as file:
            for line in file:
                parts = line.strip().split("\t")  # Assuming tab-separated format
                if len(parts) < 2:
                    continue  # Ignore malformed lines
                
                query_id = parts[0]
                answer_text = parts[1]
                answers[query_id] = answer_text  # Store in dictionary
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)


def write_answers(collection):
    '''
    Writes the data structure to the processed folder
    '''
    # TODO: fill in the rest
    processed_file = os.path.join('processed', collection + "_processed.txt")

    # Ensure the directory exists
    os.makedirs('processed', exist_ok=True)

    try:
        with open(processed_file, 'w') as file:
            for query_id, answer in answers.items():
                file.write(f"{query_id}\t{answer}\n")
        print("SUCCESS")  # Print only if all went well
    except Exception as e:
        print(f"Error writing file: {e}")
        sys.exit(1)



    
if __name__ == "__main__":
    '''
    main() function
    '''
    # TODO: read the collection name from command line
    # TODO: check for invalid parameters
    # TODO: print 'SUCCESS' to STDOUT if all went well

    if len(sys.argv) != 2:
        print("Usage: python your_script.py <collection_name>")
        sys.exit(1)

    collection_name = sys.argv[1]

    read_answers(collection_name)
    write_answers(collection_name)

    exit(0)
    
