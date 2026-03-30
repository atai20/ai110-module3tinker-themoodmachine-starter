"""
Shared data for the Mood Machine lab.

This file defines:
  - POSITIVE_WORDS: starter list of positive words
  - NEGATIVE_WORDS: starter list of negative words
  - SAMPLE_POSTS: short example posts for evaluation and training
  - TRUE_LABELS: human labels for each post in SAMPLE_POSTS



Use Copilot to help you inspect the dataset.
Reference the file or a selection when asking questions.
Focus on understanding relationships between SAMPLE_POSTS and TRUE_LABELS.
If Copilot's explanation feels generic, add more context or reason through it yourself.



"""

# ---------------------------------------------------------------------
# Starter word lists
# ---------------------------------------------------------------------

POSITIVE_WORDS = [
    "happy",
    "great",
    "good",
    "love",
    "excited",
    "awesome",
    "fun",
    "chill",
    "relaxed",
    "amazing",
]

NEGATIVE_WORDS = [
    "sad",
    "bad",
    "terrible",
    "awful",
    "angry",
    "upset",
    "tired",
    "stressed",
    "hate",
    "boring",
]

# ---------------------------------------------------------------------
# Starter labeled dataset
# ---------------------------------------------------------------------

# Short example posts written as if they were social media updates or messages.
SAMPLE_POSTS = [
    "I love this class so much",
    "Today was a terrible day",
    "Feeling tired but kind of hopeful",
    "This is fine",
    "So excited for the weekend",
    "I am not happy about this",

    "Yo wassup my bro",
    "Ure feeling me?",
    "Where are you?🫃",
    "Where are we going?😏",
    "Amazing!!!🤩",
    "No aliens here👽",

    # Additional examples
    "Lowkey I am sad but also excited for tomorrow 😂",
    "No cap, this is the best day ever 🥳",
    "I absolutely hate getting stuck in traffic 😡",
    "Highkey stressed but still okay",
    "I love it, no complaints at all!",
    "I'm tired, but no big deal."
]

# Human labels for each post above.
# Allowed labels in the starter:
#   - "positive"
#   - "negative"
#   - "neutral"
#   - "mixed"
TRUE_LABELS = [

    "positive",  # "I love this class so much"
    "negative",  # "Today was a terrible day"
    "mixed",     # "Feeling tired but kind of hopeful"
    "neutral",   # "This is fine"
    "positive",  # "So excited for the weekend"
    "negative",  # "I am not happy about this"

    "positive", # "Yo wassup my bro",
    "neutral", # "Ure feeling me?",
    "neutral", # "Where are you?🫃",
    "positive", # "Where are we going?😏",
    "positive", # "Amazing!!!🤩",
    "negative", # "No aliens here👽"

    "mixed",    # "Lowkey I am sad but also excited for tomorrow 😂"
    "positive", # "No cap, this is the best day ever 🥳"
    "negative", # "I absolutely hate getting stuck in traffic 😡"
    "mixed",    # "Highkey stressed but still okay"
    "positive", # "I love it, no complaints at all!"
    "mixed"     # "I'm tired, but no big deal."
]

# TODO: Add 5-10 more posts and labels.
#
# Requirements:
#   - For every new post you add to SAMPLE_POSTS, you must add one
#     matching label to TRUE_LABELS.
#   - SAMPLE_POSTS and TRUE_LABELS must always have the same length.
#   - Include a variety of language styles, such as:
#       * Slang ("lowkey", "highkey", "no cap")
#       * Emojis (":)", ":(", "🥲", "😂", "💀")
#       * Sarcasm ("I absolutely love getting stuck in traffic")
#       * Ambiguous or mixed feelings
#
# Tips:
#   - Try to create some examples that are hard to label even for you.
#   - Make a note of any examples that you and a friend might disagree on.
#     Those "edge cases" are interesting to inspect for both the rule based
#     and ML models.
#
# Example of how you might extend the lists:
#
# SAMPLE_POSTS.append("Lowkey stressed but kind of proud of myself")
# TRUE_LABELS.append("mixed")
#
# Remember to keep them aligned:
#   len(SAMPLE_POSTS) == len(TRUE_LABELS)
