import re
import sympy as sp

def solve_equation(equation_str):
    """Решает линейные и квадратные уравнения."""
    try:
        x = sp.symbols('x')
        # Преобразуем строку в выражение sympy
        equation = sp.sympify(equation_str)
        
        # Решаем уравнение
        solutions = sp.solve(equation, x)
        return solutions
    except Exception as e:
        return f"Ошибка при решении уравнения: {e}"

def extract_equation(query):
    """Извлекает уравнение из текстового запроса."""

    # Регулярное выражение для поиска уравнений
    equation_pattern = f'([-+]?\d*\*?x?\s*[-+*/=^]\s*\d+|\d+\s*[-+*/=^]\s*\d*\*?x?)'
 
    # Ищем уравнение в запросе
    matches = re.findall(equation_pattern, query.replace(" ", ""))
    print(matches)
    
    if matches:
      #if matches[1] == '=0':
        return matches[0]  # Берем первое найденное уравнение
    return None

def main(query):
    """Основная функция для обработки запроса и решения уравнения."""
    equation_str = extract_equation(query)
    print(equation_str)
    
    if equation_str:
        solution = solve_equation(equation_str)
        return f"Решение уравнения '{equation_str}': {solution}"
    else:
        return "Уравнение не найдено в запросе."