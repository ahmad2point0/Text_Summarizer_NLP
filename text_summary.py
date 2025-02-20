import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
from collections import Counter

def extractive_summarizer(rawdocs, compression_ratio=0.3):
    """Extractive summarization using NLP-based sentence ranking"""
    nlp = spacy.load("en_core_web_lg")
    doc = nlp(rawdocs)
    
    words = [token.text.lower() for token in doc if token.text.lower() not in STOP_WORDS and token.text.lower() not in punctuation and len(token.text) > 1]
    word_freq = Counter(words)
    max_freq = max(word_freq.values()) if word_freq else 1
    word_freq = {word: freq / max_freq for word, freq in word_freq.items()}

    sent_tokens = list(doc.sents)
    sent_scores = {}

    for sent in sent_tokens:
        for word in sent:
            if word.text.lower() in word_freq:
                sent_scores[sent] = sent_scores.get(sent, 0) + word_freq[word.text.lower()]
        
        sent_scores[sent] /= len(sent)

    select_len = max(1, int(len(sent_tokens) * compression_ratio))
    summary_sentences = nlargest(select_len, sent_scores, key=sent_scores.get)
    
    summary = " ".join([sent.text for sent in summary_sentences])
    return summary ,rawdocs ,len(summary.split(" ")),len(rawdocs.split(" "))
