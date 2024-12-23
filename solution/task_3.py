import random
from collections import defaultdict

def learn(dataset: list[str]) -> dict:
    transitions = defaultdict(list)

    for sentence in dataset:
        words = sentence.split()  
        for i in range(len(words) - 1):
            current_word = words[i]
            next_word = words[i + 1]
            transitions[current_word].append(next_word)
    
    return dict(transitions)

def generate(state: dict, length: int = 10) -> str:

    if not state:
        return ""
    
    current_word = random.choice(list(state.keys()))
    result = [current_word]

    for _ in range(length - 1):
        if current_word in state and state[current_word]:
            next_word = random.choice(state[current_word])
            result.append(next_word)
            current_word = next_word
        else:
            break

    return " ".join(result)

data = input("Введите текст для обучения (несколько предложений через точку или каждое с новой строки):\n")
dataset = [sentence.strip().lower() for sentence in data.replace("\n", ".").split(".") if sentence.strip()]
state = learn(dataset)
length = int(input("Введите желаемую длину генерируемого текста (в словах): "))
generated_text = generate(state, length=length)
print("Сгенерированный текст:", generated_text)
