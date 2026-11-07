def mean(numbers):
    return sum(numbers) / len(numbers)


def maximum(numbers):
    return max(numbers)


def minimum(numbers):
    return min(numbers)


if __name__ == "__main__":
    marks = [85, 90, 78, 95]
    print("Mean:", mean(marks))
    print("Maximum:", maximum(marks))
    print("Minimum:", minimum(marks))
