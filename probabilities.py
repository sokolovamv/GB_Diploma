import nltk
import ssl
import re
from nltk.tokenize import word_tokenize

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('punkt')

def extract_probability_info(query):
    """Извлекает информацию о вероятностях из текстового запроса."""
    # Пример паттерна для поиска вероятностей
    pattern = r'(\d+)%?'
    matches = re.findall(pattern, query)
    
    if matches:
        return sorted([int(match) for match in matches])
    
    return None

def calculate_probability(events, total_outcomes):
    """Вычисляет вероятность события."""
    if total_outcomes == 0:
        return "Общее количество исходов не может быть нулевым."
    
    probability = events / total_outcomes
    return probability

def main(query):
    """Основная функция для обработки запроса и вычисления вероятности."""
    try:
        probabilities = extract_probability_info(query)
        
        if probabilities and len(probabilities) == 2:
            events, total_outcomes = probabilities
            if events < 0 or total_outcomes < 0:
                return "Количество событий и общее количество исходов должны быть неотрицательными."
            
            probability = calculate_probability(events, total_outcomes)
            return f"Вероятность: {probability:.2f} или {probability * 100:.2f}%"
        else:
            return "Не удалось извлечь данные о вероятностях из запроса."
    
    except ValueError as ve:
        return f"Ошибка преобразования данных: {ve}"
    except Exception as e:
        return f"Произошла ошибка: {e}"

