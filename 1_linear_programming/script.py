from scipy.optimize import linprog

# У нас функция p = 9*x_1 + 2*x_2 + 4*x_3 + 7*x_4
# но так как linprog решает только задачи МИНИМИЗАЦИИ (sic!), то
# будем делать фокус с умножением на -1 и минимизацией отрицательной функции
# по модулю получится как раз максимизация 

profit_factors = [-9, -2, -4, -7]

# Матрица из левых частей в системе неравенств
left_ineq = [
    [1, 0, 2, 1],
    [0, 1, 3, 2],
    [4, 2, 0, 4],
]

# Вектор из значений в правой части неравенства
right_ineq = [180, 210, 800]

# Интервалы, которые могут принимать неизвестные x_1 - x_4 
bnd  = [(0, float('inf')), 
        (0, float('inf')), 
        (0, float('inf')),
        (0, float('inf'))
] 

# В туториале используют method='revised simplex' но SciPy выдаёт предупреждение, что 
# он будет depreceated в будущих версиях
optimized_solution = linprog(c=profit_factors, A_ub=left_ineq, b_ub=right_ineq, bounds=bnd, method='highs')
quantities = tuple(map(int, optimized_solution.x))
max_profit = -1 * optimized_solution.fun

print('quantities of clothes for max profit:', quantities)
print('max profit:', max_profit)