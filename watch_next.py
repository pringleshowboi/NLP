import spacy

nlp = spacy.load('en_core_web_md')

# FUNCTION TO CALCULATE SIMILARITY SCORE BETWEEN TWO DOCUMENTS
def calculate_similarity(doc1, doc2):
    return doc1.similarity(doc2)

# FUNCTION TO FIND THE MOST SIMILAR MOVIE DESCRIPTION
def find_similar_movie(description):
    movie_descriptions = []
    with open("movies.txt", "r") as file:
        movie_descriptions = file.readlines()
        
# MOVIE DESCRIPTIONS AND TARGET DESCRIPTION USING SPACY
    movie_descriptions = [nlp(desc.strip()) for desc in movie_descriptions]
    target_description = nlp(description)
    
# CALCULATING SIMILARITY SCORES BETWEEN TARGET DESCRIPTION AND MOVIE DESCRIPTIONS
    similarity_scores = [calculate_similarity(target_description, desc) for desc in movie_descriptions]
    
# FINDING INDEX OF THE MOST SIMILAR MOVIE DESCRIPTION
    most_similar_index = max(range(len(similarity_scores)), key=lambda i: similarity_scores[i])
    
# RETURNING THE MOST SIMILAR MOVIE DESCRIPTION
    return movie_descriptions[most_similar_index].text

target_movie_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

# CALLING THE FUNCTION TO FIND THE MOST SIMILAR MOVIE DESCRIPTION
most_similar_movie = find_similar_movie(target_movie_description)

# PRINTING THE MOST SIMILAR MOVIE DESCRIPTION
print(f"Most similar movie: {most_similar_movie}")