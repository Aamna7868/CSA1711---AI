from collections import deque

def is_valid(m_left, c_left, m_right, c_right):
    # Missionaries cannot be outnumbered by cannibals
    if m_left > 0 and m_left < c_left:
        return False

    if m_right > 0 and m_right < c_right:
        return False

    return True


def solve():
    # State = (missionaries_left, cannibals_left, boat_position)
    # Boat position: 0 = left, 1 = right

    initial = (3, 3, 0)
    goal = (0, 0, 1)

    queue = deque([(initial, [initial])])
    visited = {initial}

    # Possible people in the boat
    moves = [
        (1, 0),
        (2, 0),
        (0, 1),
        (0, 2),
        (1, 1)
    ]

    while queue:
        state, path = queue.popleft()

        if state == goal:
            print("Solution:")
            for s in path:
                print(s)
            return

        m_left, c_left, boat = state
        m_right = 3 - m_left
        c_right = 3 - c_left

        for m, c in moves:

            if boat == 0:       # Boat moves left -> right
                new_m_left = m_left - m
                new_c_left = c_left - c
                new_boat = 1

            else:               # Boat moves right -> left
                new_m_left = m_left + m
                new_c_left = c_left + c
                new_boat = 0

            new_m_right = 3 - new_m_left
            new_c_right = 3 - new_c_left

            # Check valid number of people
            if new_m_left < 0 or new_c_left < 0:
                continue

            if new_m_left > 3 or new_c_left > 3:
                continue

            if not is_valid(
                new_m_left, new_c_left,
                new_m_right, new_c_right
            ):
                continue

            new_state = (new_m_left, new_c_left, new_boat)

            if new_state not in visited:
                visited.add(new_state)
                queue.append(
                    (new_state, path + [new_state])
                )


solve()