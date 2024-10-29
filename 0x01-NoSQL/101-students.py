#!/usr/bin/env python3
"""How to sort a retured data"""


def top_students(mongo_collection):
    """Returns all students sorted by average score."""
    pipeline = [
        {
            "$project": {
                "name": 1,
                "averageScore": {"$avg": "$topics.score"},
            }
        },
        {"$sort": {"averageScore": -1}},
    ]

    return list(mongo_collection.aggregate(pipeline))
