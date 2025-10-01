from matrix import Matrix

class MatrixCalculator:
    def __init__(self, path_a, path_b, log_file="matrix_log.txt"):
        self.path_a = path_a
        self.path_b = path_b
        self.log_file = log_file

    def _write_matrix(self, f, label, M):
        f.write(label + "\n")
        eps = 1e-12
        for row in M.data:
            out = []
            for x in row:
                v = 0.0 if abs(x) < eps else x
                if v == 0.0:
                    v = 0.0
                out.append("{:.6g}".format(v))
            f.write(" ".join(out) + "\n")

    def _write_section(self, operation, A, B, result):
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write("Operation: {}\n".format(operation))
            self._write_matrix(f, "Matrix A:", A)
            self._write_matrix(f, "Matrix B:", B)
            self._write_matrix(f, "Result:", result)
            f.write("\n")

    def _write_error(self, operation, msg):
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write("Operation: {}\n".format(operation))
            f.write("Error: {}\n\n".format(msg))

    def run_all(self):
        A = Matrix.from_file(self.path_a)
        B = Matrix.from_file(self.path_b)

        try:
            self._write_section("Addition", A, B, A.add(B))
        except Exception as e:
            self._write_error("Addition", str(e))

        try:
            self._write_section("Subtraction", A, B, A.subtract(B))
        except Exception as e:
            self._write_error("Subtraction", str(e))

        try:
            self._write_section("Multiplication", A, B, A.multiply(B))
        except Exception as e:
            self._write_error("Multiplication", str(e))

        try:
            self._write_section("Division", A, B, A.divide(B))
        except Exception as e:
            self._write_error("Division", str(e))
