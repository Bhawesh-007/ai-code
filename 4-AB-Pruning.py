import math

def alpha_beta(node, depth, alpha, beta, maximizing_player):
    # Terminal node
    if depth == 0 or "children" not in node:
        return node["value"]

    if maximizing_player:
        value = -math.inf
        for child in node["children"]:
            value = max(value, alpha_beta(child, depth - 1, alpha, beta, False))
            alpha = max(alpha, value)
            # Beta Pruning
            if alpha >= beta:
                break
        return value
    else:
        value = math.inf
        for child in node["children"]:
            value = min(value, alpha_beta(child, depth - 1, alpha, beta, True))
            beta = min(beta, value)
            # Alpha Pruning
            if beta <= alpha:
                break
        return value

# Example Game Tree
tree = {
    "children": [
        {
            "children": [
                {"value": 3},
                {"value": 5}
            ]
        },
        {
            "children": [
                {"value": 6},
                {"value": 9}
            ]
        }
    ]
}

best_value = alpha_beta(tree, 2, -math.inf, math.inf, True)
print("Optimal Value:", best_value)