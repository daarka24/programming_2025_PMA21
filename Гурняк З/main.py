from vectorCalculator import VectorCalculator

if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output.txt"

    v1, v2 = VectorCalculator.read_vectors(input_file)
    calc = VectorCalculator(v1, v2)
    results = calc.compute_all()
    VectorCalculator.write_results(output_file, results)