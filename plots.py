#!pip matplolib
#!pip install selenium install label-studio matplotlib

import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from io import BytesIO

# Обработка текстовых сообщений
def checking_message(user_input):
    # Проверяем корректность введенной функции
    try:
        buf = plot_function(user_input)
        return buf
    except Exception as e:
        return (f'Ошибка при построении графика: {str(e)}')


def plot_function(query, x_range=(-10, 10), num_points=100):
    # удаляем саму команду
    function_str = query.replace('/plots', '')

    # Определяем переменную
    x = sp.symbols('x')
    
    # Преобразуем строку в математическое выражение
    function = sp.sympify(function_str)
    
    # Создаем массив значений x
    x_vals = np.linspace(x_range[0], x_range[1], num_points)
    
    # Вычисляем значения функции
    y_vals = [function.evalf(subs={x: val}) for val in x_vals]
    
    # Строим график
    plt.figure(figsize=(10, 5))
    plt.plot(x_vals, y_vals, label=str(function), color='blue')
    plt.title(f'График функции: {function_str}')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.axhline(0, color='black', lw=0.5, ls='--')
    plt.axvline(0, color='black', lw=0.5, ls='--')
    plt.grid()
    plt.legend()
    plt.show()

    # Сохраняем график в байтовый поток
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    return buf

    


    

