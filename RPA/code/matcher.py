"""Compatibility module for the relation matcher.

The original supplementary material misspelled this file as ``mather.py``.
Keep the public import used by main.py and run_experiments.py stable here.
"""

from mather import (
    embedding_similarity,
    jaccard_similarity,
    levenshtein_similarity,
    match_relation,
    string_similarity,
)

__all__ = [
    "embedding_similarity",
    "jaccard_similarity",
    "levenshtein_similarity",
    "match_relation",
    "string_similarity",
]
