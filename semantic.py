import spacy

nlp = spacy.load('en_core_web_md')

# CREATE SPACY DOCUMENTS FOR THE WORDS cat, monkey, AND banana
cat = nlp('cat')
monkey = nlp('monkey')
banana = nlp('banana')

# CALCULATE SIMILARITY SCORE BETWEEN cat AND monkey
similarity_cat_monkey = cat.similarity(monkey)

# CALCULATE SIMILARITY SCORE BETWEEN cat AND banana
similarity_cat_banana = cat.similarity(banana)

# PRINT THE SIMILARITY SCORES
print(f'''Similarities between cat and monkey: {similarity_cat_monkey}
Similarities between cat and banana: {similarity_cat_banana}''')

# CREATE SPACY DOCUMENTS FOR THE PHRASES Bing Gotta Bomb AND Yo Mama So Fat
similarity1 = nlp('Bing Gotta Bomb')
similarity2 = nlp('Yo Mama So Fat')

# CALCULATE SIMILARITY SCORE BETWEEN THE TWO PHRASES
similarities = similarity1.similarity(similarity2)
print(f"Similarities between my two examples: {similarities}")