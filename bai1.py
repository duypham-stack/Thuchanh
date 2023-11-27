import numpy as np


def solve_linear_equations(coefficients, constants):
    A = np.array(coefficients)
    b = np.array(constants)

    try:
        x = np.linalg.solve(A, b)
        return x
    except np.linalg.LinAlgError:
        return None


def get_coefficients():
    coefficients = []
    for i in range(n):
        row = []
        for j in range(n):
            entry = float(input(f"Nhập hệ số a{i + 1}{j + 1}: "))
            row.append(entry)
        coefficients.append(row)
    return coefficients


def get_constants():
    constants = []
    for i in range(n):
        entry = float(input(f"Nhập hằng số b{i + 1}: "))
        constants.append(entry)
    return constants


def print_solution(solution):
    if solution is None:
        print("Hệ phương trình không có nghiệm.")
    else:
        print("Nghiệm của hệ phương trình là:")
        for i, x in enumerate(solution):
            print(f"x{i + 1} = {x}")


# Nhập số phương trình và số ẩn
n = int(input("Nhập số phương trình và số ẩn (n): "))

# Nhập ma trận hệ số
coefficients = get_coefficients()

# Nhập vector hằng số
constants = get_constants()

# Giải phương trình
solution = solve_linear_equations(coefficients, constants)

# In kết quả
print_solution(solution)