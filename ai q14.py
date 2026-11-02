def alphabeta(depth, node, maximizing, values,
              alpha, beta, max_depth):
    if depth == max_depth:
        return values[node]

    if maximizing:
        best = float('-inf')

        for child in [node * 2, node * 2 + 1]:
            val = alphabeta(
                depth + 1, child, False, values,
                alpha, beta, max_depth
            )
            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = float('inf')

        for child in [node * 2, node * 2 + 1]:
            val = alphabeta(
                depth + 1, child, True, values,
                alpha, beta, max_depth
            )
            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best

values = [3, 5, 2, 9, 12, 5, 23, 23]

result = alphabeta(
    0, 0, True, values,
    float('-inf'), float('inf'), 3
)

print("Best value:", result)