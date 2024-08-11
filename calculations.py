import spacy
import sympy as sp

# Загрузка модели spaCy
nlp = spacy.load("en_core_web_sm")

# Функция для обработки математических выражений
def evaluate_expression(expression):
    try:
        # Используем sympy для решения выражений
        result = sp.sympify(expression)
        return result
    except Exception as e:
        return f"Ошибка при вычислении: {str(e)}"

# Функция для обработки ввода пользователя
def process_input(user_input):
    # Применяем NLP для извлечения математического выражения
    doc = nlp(user_input)
    expression = ""
    
    for token in doc:
        # Ищем числовые выражения и знаки операций
        if token.is_digit or token.text in "+-*/()":
            expression += token.text
    
    if expression:
        result = evaluate_expression(expression)
        return f"Результат: {result}"
    else:
        return "Не удалось распознать математическое выражение."

