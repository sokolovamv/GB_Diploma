import spacy

# Загрузка модели NLP
nlp = spacy.load("en_core_web_sm")

def extract_parameters(text):
    """Извлекает параметры a, d и n из текстового запроса."""
    doc = nlp(text)
    a, d, n = None, None, None

    for token in doc:
        if token.text.lower() == 'первый' and token.nbor().text.lower() == 'член':
            try:
                a = float(token.nbor(2).text)
            except ValueError:
                print(f"Ошибка: '{token.nbor(2).text}' не является числом.")
        elif token.text.lower() == 'разность':
            try:
                d = float(token.nbor(1).text)
            except ValueError:
                print(f"Ошибка: '{token.nbor(1).text}' не является числом.")
        elif token.text.lower() == 'найти':
            try:
                n = int(token.nbor(1).text)
            except ValueError:
                print(f"Ошибка: '{token.nbor(1).text}' не является целым числом.")
    
    return a, d, n

def nth_term(a, d, n):
    """Вычисляет n-й член арифметической прогрессии."""
    try:
        return a + (n - 1) * d
    except TypeError:
        print("Ошибка: Параметры a, d и n должны быть числами.")

def sum_of_n_terms(a, d, n):
    """Вычисляет сумму первых n членов арифметической прогрессии."""
    try:
        return (n / 2) * (2 * a + (n - 1) * d)
    except TypeError:
        print("Ошибка: Параметры a, d и n должны быть числами.")

def main(user_input):
    a, d, n = extract_parameters(user_input)

    if a is not None and d is not None and n is not None:
        nth = nth_term(a, d, n)
        sum_n = sum_of_n_terms(a, d, n)
        return f"{n}-й член арифметической прогрессии: {nth}, Сумма первых {n} членов арифметической прогрессии: {sum_n}"
    else:
        print("Не удалось извлечь параметры. Пожалуйста, убедитесь, что ваш запрос корректен.")

