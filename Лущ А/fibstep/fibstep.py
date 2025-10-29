def fibonacci(arr, step):
    if step == 0:
        return arr
    arr.append(arr[-1] + arr[-2])
    return fibonacci(arr, step - 1)


def main():
    with open("input_step.txt", "r", encoding="utf-8") as f:
        a, b = map(float, f.read().strip().split(","))

    with open("steps.txt", "r", encoding="utf-8") as f:
        steps = int(f.read().strip())

    result = fibonacci([a, b], steps - 2)

    with open("output_step.txt", "w", encoding="utf-8") as f:
        f.write(",".join(map(str, result)))


if __name__ == "__main__":
    main()
