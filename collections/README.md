
**Do not write documentation here -- TAs will not read this file during grading.**

## What is this folder for?

Add your test collections here.

The collection that you create must have three files, with the same name and extensions `.ALL`, `QRY`, and `REL`. The format of each file is described below.


## Simplified CISI collection

The test collection we provide was simplified from the [CISI collection used in a kaggle comptetition](https://www.kaggle.com/datasets/dmaso01dsta/cisi-a-dataset-for-information-retrieval).


### The `.ALL` and `.QRY` files

The documents in the collection are given in the `.ALL` file, while the queries are specified in the `.QRY` file. Both files contain two fields (in this simplified format):
- `.I` contains the ID of the document or query
- `.W` contains the words in the document or query

The IDs must be unique and appear on the same line as the `.I` marker. The words section span the lines between the `.W` marker and the following `.I` or the end of the file. Here is an example:

```
.I 1
.W 
line 1
line 2
.I 2
.W
line 3
line 4
```

Both documents and queries can span multiple lines.

### The `.REL` file

This file indicates which documents are relevant for which queries. The file does not have any fields. Instead, it is a `TSV` file with two columns: the first shows the query ID while the second column shows the document ID. 

If multiple documents are relevant for the same query, that query ID appears on multiple lines, as in the example:

```
3	27
3	39
7	1
9	13
9	27
9	150
...
```

In the example above, documents 27 and 39 are marked as relevant for query 3. Note that document 27 is also relevant for query 9.

#### Integrity constraints

Some queries in the `.QRY` file many not have "answers" in the `.REL` file. Also, some documents in `.ALL` may not be relevant for any query.

In fact, only 76 of the 122 queries in the `CISI` collection appear in the `.REL` file provided.

However, every ID appearing in the `.REL` file must correspond to a query in the corresponding `.QRY` file or to a document in the corresponding `.ALL` file. If your programs detects a violation of this constraint, it must trigger and error.