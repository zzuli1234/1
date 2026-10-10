"""Compatibility module for the KG query executor.

The original supplementary material misspelled this file as
``query_exexutor.py`` while callers import ``query_executor``.
"""

from query_exexutor import aggregate_answers, query_kg

__all__ = ["aggregate_answers", "query_kg"]
