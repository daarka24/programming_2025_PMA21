from matrixCalculator import MatrixCalculator

if __name__ == "__main__":
    calc = MatrixCalculator("matrix1.txt", "matrix2.txt", "matrix_log.txt")
    calc.run_all()
    print("Results logged in matrix_log.txt")
