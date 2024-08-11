import sympy as sp

def solve_inequality(query):
    # удаляем команду
    inequality_str = query.replace('/inequalities', '').strip()

    # Определяем переменную
    x = sp.symbols('x')

    try:
        # Преобразуем строку в математическое неравенство
        inequality = sp.sympify(inequality_str)
        
        # Проверяем, является ли выражение неравенством
        if not isinstance(inequality, sp.Rel):
            raise ValueError("Введенное выражение не является неравенством.")

        # Решаем неравенство
        solution = sp.solve_univariate_inequality(inequality, x)

        return f'{solution}'

    except (sp.SympifyError, ValueError) as e:
        return f'Ошибка: {str(e)}. Пожалуйста, введите корректное неравенство.'
    except Exception as e:
        return f'Неизвестная ошибка: {str(e)}. Пожалуйста, проверьте введенные данные.'


