import spacy
import re
from collections import Counter
from heapq import nlargest
from spacy.lang.en.stop_words import STOP_WORDS

def clean_text(text):
    """Remove special characters, citation references, and unnecessary whitespace."""
    text = re.sub(r"\[\d+\]", "", text)  # Remove citation references like [17]
    text = re.sub(r"\[\w\]", "", text)  # Remove citation references like [e]
    text = re.sub(r"[^a-zA-Z0-9\s.,]", "", text)  # Keep periods for sentence segmentation
    text = re.sub(r"\s+", " ", text).strip()  # Remove extra spaces
    return text

def summarizer(rawdocs, compression_ratio=0.3):
    """Extractive summarization using NLP-based sentence ranking."""
    nlp = spacy.load("en_core_web_lg")
    
    cleaned_text = clean_text(rawdocs)  # Clean text before processing
    doc = nlp(cleaned_text)
    
    # Extract words, ignoring stopwords and punctuation
    words = [token.lemma_.lower() for token in doc if token.text.lower() not in STOP_WORDS and token.is_alpha]
    
    # Compute word frequency
    word_freq = Counter(words)
    max_freq = max(word_freq.values()) if word_freq else 1
    word_freq = {word: freq / max_freq for word, freq in word_freq.items()}
    
    # Sentence scoring
    sent_tokens = list(doc.sents)
    sent_scores = {sent: sum(word_freq.get(word.lemma_.lower(), 0) for word in sent) for sent in sent_tokens}
    
    # Normalize sentence scores
    for sent in sent_scores:
        sent_scores[sent] /= max(1, len(sent))

    # Select top-ranked sentences
    select_len = max(1, int(len(sent_tokens) * compression_ratio))
    summary_sentences = nlargest(select_len, sent_scores, key=sent_scores.get)
    
    summary = " ".join([sent.text for sent in summary_sentences])
    return summary, rawdocs, len(summary.split()), len(rawdocs.split())

