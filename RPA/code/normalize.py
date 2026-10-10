
# normalize.py
import re
import nltk
from nltk.stem import WordNetLemmatizer


lemmatizer = WordNetLemmatizer()


def _tokenize(value: str) -> list[str]:
    """Tokenize locally so importing the project never requires network access."""
    try:
        return nltk.word_tokenize(value)
    except LookupError:
        # NLTK's punkt resources are optional for these simple relation names.
        return re.findall(r"[A-Za-z0-9]+", value)


def _lemmatize(token: str) -> str:
    """Use WordNet when installed, otherwise keep the original token."""
    try:
        return lemmatizer.lemmatize(token)
    except LookupError:
        return token

def normalize_relation(rel: str) -> str:
    """Standardize relation string format."""
    rel = rel.lower()
    rel = re.sub(r'[_/]', ' ', rel)  # replace underscores and slashes with spaces
    rel = re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', rel)  # camelCase to space
    tokens = _tokenize(rel)
    lemmatized = [_lemmatize(token) for token in tokens if token.isalnum()]
    return ' '.join(lemmatized)
