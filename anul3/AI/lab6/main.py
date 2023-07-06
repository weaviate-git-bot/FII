import random
import nltk

# nltk.download('wordnet')
# nltk.download('omw-1.4')
from nltk.corpus import wordnet
from rdflib import Graph

from typing import Tuple, List

class Ontology:
    NOT_EXTEND = False
    QUESTIONS = [
        "Cine este in relatia '{r}' cu '{c2}'?",
        "In ce relatie sunt '{c1}' si '{c2}'?",
        "'{c1}' este in relatia '{r}' cu ce concept?",
    ]

    def __init__(self, file_name) -> None:
        self.graph = Graph()
        self.graph.parse(file_name)
        self.c1_r_c2 = list()
    
    def get_synonyms(self, word) -> set:
        synonyms = set()
        syns = wordnet.synsets(word)
        if len(syns) < 1:
            return set([word])

        for syn in syns:
            for l in syn.lemmas():
                synonyms.add(l.name())
            break
        return synonyms

    def output_triplets(self, file_name) -> None:
        with open(file_name, 'w') as f:
            for s, o, p in self.graph:
                if not all([str(x).startswith("http") for x in [s,o]]):
                    continue

                if not all([str(x).split('#')[-1].isalpha() for x in [s,o,p]]):
                    continue
                
                __temp_c1rc2 = [str(x).split('#')[-1] for x in [s,o,p]]
                self.c1_r_c2.append(__temp_c1rc2)
                f.write(' - '.join(__temp_c1rc2) + '\n')

    def __extend_question(self, group: List[str]) -> List[str]:
        if Ontology.NOT_EXTEND is True:
            return group

        for i in range(3):
            should_update = random.randint(0,1)
            if should_update == 0:
                continue
            
            old = group[i]
            group[i] = random.choice(list(self.get_synonyms(group[i])))
            print(f"Extended question {old} with word: {group[i]}")

        return group

    def __verify_user_answer(self, user_answer: str, answer: str) -> bool:
        if Ontology.NOT_EXTEND is True:
            return user_answer.lower() == answer.lower()

        user_answer = user_answer.lower()

        for word in list(self.get_synonyms(answer)):
            if user_answer == word.lower():
                return True
            
        return False

    def ask_question(self) -> Tuple[str, str]:
        group_position = random.randint(0, len(self.c1_r_c2))
        
        group = self.__extend_question(self.c1_r_c2[group_position])
        
        answer_value = random.randint(0, 2)
        answer = group[answer_value]

        return self.QUESTIONS[answer_value].format(**{
            0: {'r': group[1], 'c2': group[2]},
            1: {'c1': group[0], 'c2': group[2]},
            2: {'r': group[1], 'c1': group[0]},
        }[answer_value]), answer        

    def play_a_game(self) -> None:
        try:
            while True:
                question, answer = self.ask_question()
                print(question)

                user_answer = input("[>] Answer: ")
                if self.__verify_user_answer(user_answer, answer):
                    print("Correct!")
                else:
                    print("Wrong! Correct answer is: " + answer)

                
        except KeyboardInterrupt:
            print("Game over!")
            pass
        
ont = Ontology('food.rdf')
ont.output_triplets('triplets.txt')
print('Finished dumping triplets')
ont.play_a_game()

# synonyms = set()



# for word in wordnet.synsets("dog")[0].lemmas():
#     synonyms.add(word.name())

# print(synonyms)

# g = Graph()
# g.parse("food.rdf")

# print(len(g))
# # prints: 2

# import pprint
# for stmt in g:
#     pprint.pprint(stmt) 