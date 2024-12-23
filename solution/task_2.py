def play(words: list[str]) -> list[int]:
    errors = []  
    used_words = set()  
    
    for i in range(len(words)):
        word = words[i]
        if word in used_words or (i > 0 and words[i - 1][-1] != word[0]):
            errors.append(i + 1)
            
        else:
            used_words.add(word)
    
    return errors

words = input("Введите слова через пробел: ").lower().split()
result = play(words)
print(f"Номера слов с ошибками: {result}")
