def fibonacci(arr, limit):

    next_val = arr[-1] + arr[-2]
    if next_val > limit:
        return arr
    arr.append(next_val)
    return fibonacci(arr, limit)


def main():

    with open("input_limit.txt", "r", encoding="utf-8") as f:
        a, b = map(float, f.read().strip().split(","))

    with open("limit.txt", "r", encoding="utf-8") as f:
        limit = float(f.read().strip())

    result = fibonacci([a, b], limit)

    with open("output_limit.txt", "w", encoding="utf-8") as f:
        f.write(",".join(map(str, result)))


if __name__ == "__main__":
    main()
