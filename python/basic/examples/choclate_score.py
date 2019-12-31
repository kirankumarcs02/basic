n = 6
scores = [4, 6, 4, 5, 6, 2]
candies = []

# for i in xrange(n):
#     x = int(input())
#     scores.append(x)

for i in range(n):
    if i == 0:
        candies.append(1)
    elif scores[i] > scores[i - 1]:
        candies.append(candies[-1] + 1)
    elif scores[i] < scores[i - 1]:
        if candies[i - 1] == 1:
            candies[i - 1] = 2
            candies.append(1)
            j = i - 2
            while j >= 0:
                if scores[j] > scores[j + 1] and candies[j] <= candies[j + 1]:
                    candies[j] = candies[j + 1] + 1
                else:
                    break
                j -= 1

        else:
            candies.append(1)
    else:
        candies.append(1)
# print
print(candies)
print(sum(candies))