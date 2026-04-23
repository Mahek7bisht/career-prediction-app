# Optional advanced file (not required but for structure)

def similarity_score(a, b):
    return len(set(a.split()) & set(b.split()))