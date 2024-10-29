#!/usr/bin/env python3
"""Write a Python function that inserts a new document
in a collection based on kwargs:

Prototype: def insert_school(mongo_collection, **kwargs):
mongo_collection will be the pymongo collection object
Returns the new _id
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into the specified MongoDB collection with attributes given as keyword arguments.

    Args:
        mongo_collection: The pymongo collection object to insert the document into.
        **kwargs: Key-value pairs representing the attributes of the document to insert.

    Returns:
        The _id of the newly inserted document.
    """
    args = mongo_collection.insert_one(kwargs)
    return args.inserted_id
