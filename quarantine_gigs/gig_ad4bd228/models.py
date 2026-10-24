from faq_engine import extract_questions, cluster_questions, calculate_coverage

def test_extract_questions():
    notes = "What is France?\nWhat is Italy?"
    questions = extract_questions(notes)
    assert len(questions) == 2

def test_cluster_questions():
    notes = "What is the capital of France?\nWhat is the capital of Italy?\nWhat is the capital of Spain?\nWhat is the capital of France?"
    questions = extract_questions(notes)
    clusters = cluster_questions(questions)
    assert len(clusters) == 3

def test_deduplicate_questions():
    ...

def test_calculate_coverage():
    ...