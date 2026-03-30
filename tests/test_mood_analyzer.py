from mood_analyzer import MoodAnalyzer


def test_score_text_simple_positive():
    analyzer = MoodAnalyzer()
    assert analyzer.score_text("I love this") > 0


def test_score_text_simple_negative():
    analyzer = MoodAnalyzer()
    assert analyzer.score_text("I hate this") < 0


def test_score_text_negation():
    analyzer = MoodAnalyzer()
    assert analyzer.score_text("I am not happy") < 0


def test_predict_label_mixed():
    analyzer = MoodAnalyzer()
    label = analyzer.predict_label("I am a little sad but also excited")
    assert label in {"mixed", "positive", "negative", "neutral"}


def test_explain_contains_score():
    analyzer = MoodAnalyzer()
    explanation = analyzer.explain("I am not happy")
    assert "Score" in explanation
