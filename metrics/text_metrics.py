import nltk
from rouge_score import rouge_scorer
import sacrebleu

# Автозагрузка необходимых пакетов
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)

def compute_bleu(references, candidates):
    # токенизация
    ref_tokens = [[nltk.word_tokenize(ref)] for ref in references]  # список списков
    cand_tokens = [nltk.word_tokenize(cand) for cand in candidates]
    # считаем BLEU по корпусу
    return nltk.translate.bleu_score.corpus_bleu(ref_tokens, cand_tokens) * 100

def compute_rouge(references, candidates):
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)
    scores = [scorer.score(ref, cand) for ref, cand in zip(references, candidates)]
    avg_scores = {k: sum(s[k].fmeasure for s in scores) / len(scores) for k in scores[0]}
    return avg_scores
