def stats(numbers):
    """ Return the mean and variance of set of numbers """

    # Average
    total = 0
    count = 0

    for number in numbers:
        total += number
        count += 1

    average = total / count

    # Variance
    variance_summation = 0

    for number in numbers:
        variance_summation += (number - average) ** 2

    variance_summation /= count

    return average, variance_summation
