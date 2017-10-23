from scipy import stats

# Consider these two arrays
x = [2, 1, 3, 4, 5, 6, 7, 8]
y = [2, 1, 13, 14, 1, 2, 3, 4]

# They are not strongly correlated
coefficient, _ = stats.pearsonr(x, y)
print(coefficient)


# Here is a function to compute scaled correlation between two variables
def scaled_correlation(a, b, scale):
    sum_correlations = 0
    count = 0
    for i in range(len(a)//scale):
        r, _ = stats.pearsonr(
            a[i * scale: (i + 1) * scale],
            b[i * scale: (i + 1) * scale]
        )
        sum_correlations += r
        count += 1
    return sum_correlations/count


# At this shorter scale correlation is strong
print(scaled_correlation(x, y, 4))

# And when the scale is even shorter, each individual segment is perfectly correlated
# and so is thus the overall correlation
print(scaled_correlation(x, y, 2))
