# mood_analyzer.py
"""
Rule based mood analyzer for short text snippets.

This class starts with very simple logic:
  - Preprocess the text
  - Look for positive and negative words
  - Compute a numeric score
  - Convert that score into a mood label
"""

from typing import List, Dict, Tuple, Optional

from dataset import POSITIVE_WORDS, NEGATIVE_WORDS


class MoodAnalyzer:
    """
    A very simple, rule based mood classifier.
    """

    def __init__(
        self,
        positive_words: Optional[List[str]] = None,
        negative_words: Optional[List[str]] = None,
    ) -> None:
        # Use the default lists from dataset.py if none are provided.
        positive_words = positive_words if positive_words is not None else POSITIVE_WORDS
        negative_words = negative_words if negative_words is not None else NEGATIVE_WORDS

        # Store as sets for faster lookup.
        self.positive_words = set(w.lower() for w in positive_words)
        self.negative_words = set(w.lower() for w in negative_words)

    # ---------------------------------------------------------------------
    # Preprocessing
    # ---------------------------------------------------------------------

    def preprocess(self, text: str) -> List[str]:
        """
        Convert raw text into a list of normalized tokens.

        Improvements included:
          - Lowercasing
          - Removing punctuation while preserving emojis
          - Normalizing repeated characters ("soooo" -> "soo")
          - Splitting common emoji/emoticon tokens
        """
        import re

        text = text.strip().lower()

        # Normalize repeated characters (e.g., soooo -> soo)
        text = re.sub(r"(.)\1{2,}", r"\1\1", text)

        # Map common emoticons to tokens
        emoticon_map = {
            ":)": "smile",
            ":-)": "smile",
            ":(": "frown",
            ":-(": "frown",
            ";)": "wink",
            ":D": "laugh",
            "😂": "laugh",
            "🥲": "sad",
            "🤩": "excited",
            "👽": "weird",
            "😡": "angry",
            "😏": "smirk",
            "🥳": "celebrate",
        }

        # Replace emoticons with text tokens before stripping punctuation.
        for emoticon, replacement in emoticon_map.items():
            text = text.replace(emoticon, f" {replacement} ")

        # Drop most punctuation (preserve word boundaries and emojis already mapped)
        text = re.sub(r"[^a-z0-9\s]", " ", text)

        tokens = [tok for tok in text.split() if tok]
        return tokens

    # ---------------------------------------------------------------------
    # Scoring logic
    # ---------------------------------------------------------------------

    def score_text(self, text: str) -> int:
        """
        Compute a numeric "mood score" for the given text.

        - Positive words increase the score (weighted by strength).
        - Negative words decrease the score (weighted by strength).
        - Handles simple negation ("not", "never", "no", "n't").
        - Uses counted frequency and word weights.
        """
        tokens = self.preprocess(text)

        score = 0
        next_negated = False

        # small weight boost for strong sentiment words
        strong_positive = {"love", "amazing", "awesome", "excited", "celebrate"}
        strong_negative = {"hate", "terrible", "awful", "angry", "sad"}

        for idx, token in enumerate(tokens):
            if token in {"not", "never", "no", "n't"}:
                next_negated = True
                continue

            if token in self.positive_words or token in self.negative_words:
                if token in self.positive_words:
                    base = 1
                else:
                    base = -1

                if token in strong_positive:
                    base *= 2
                if token in strong_negative:
                    base *= 2

                if next_negated:
                    base *= -1
                    next_negated = False

                score += base
                continue

            # Some token combos in case of direct relation like "not happy"
            if idx + 1 < len(tokens):
                next_token = tokens[idx + 1]
                if token in {"not", "never", "no", "n't"} and next_token in self.positive_words:
                    score -= 1
                    next_negated = False
                elif token in {"not", "never", "no", "n't"} and next_token in self.negative_words:
                    score += 1
                    next_negated = False

        return score

    # ---------------------------------------------------------------------
    # Label prediction
    # ---------------------------------------------------------------------

    def predict_label(self, text: str) -> str:
        """
        Turn the numeric score for a piece of text into a mood label.

        - score >= 2   -> "positive"
        - score <= -2  -> "negative"
        - score == 0   -> "neutral"
        - score == 1 or -1 -> "mixed"
        """
        score = self.score_text(text)

        if score >= 2:
            return "positive"
        if score <= -2:
            return "negative"
        if score == 0:
            return "neutral"
        return "mixed"

    # ---------------------------------------------------------------------
    # Explanations (optional but recommended)
    # ---------------------------------------------------------------------

    def explain(self, text: str) -> str:
        """
        Return a short string explaining why the model chose a label.

        Reports:
          - numeric score
          - positive terms found
          - negative terms found
          - whether any negations were applied
        """
        tokens = self.preprocess(text)

        positive_hits: List[str] = []
        negative_hits: List[str] = []
        score = 0
        next_negated = False

        strong_positive = {"love", "amazing", "awesome", "excited", "celebrate"}
        strong_negative = {"hate", "terrible", "awful", "angry", "sad"}

        for token in tokens:
            if token in {"not", "never", "no", "n't"}:
                next_negated = True
                continue

            if token in self.positive_words:
                weight = 2 if token in strong_positive else 1
                impact = -weight if next_negated else weight
                score += impact
                positive_hits.append(token)
                next_negated = False
                continue

            if token in self.negative_words:
                weight = 2 if token in strong_negative else 1
                impact = +weight if next_negated else -weight
                score += impact
                negative_hits.append(token)
                next_negated = False
                continue

        return (
            f"Score = {score} "
            f"(positive hits: {sorted(set(positive_hits)) or '[]'}; "
            f"negative hits: {sorted(set(negative_hits)) or '[]'}; "
            f"negation active: {next_negated})"
        )
