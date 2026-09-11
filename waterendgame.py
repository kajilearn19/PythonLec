
def smith_waterman(seq1, seq2, match_score=1, mismatch_penalty=-1, gap_penalty=-2):
    m = len(seq1)
    n = len(seq2)

    # Create score matrix filled with 0
    score_matrix = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Variables to store maximum score position
    max_score = 0
    max_i = 0
    max_j = 0

    # Fill score matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if seq1[i - 1] == seq2[j - 1]:
                diagonal_score = score_matrix[i - 1][j - 1] + match_score
            else:
                diagonal_score = score_matrix[i - 1][j - 1] + mismatch_penalty

            up_score = score_matrix[i - 1][j] + gap_penalty
            left_score = score_matrix[i][j - 1] + gap_penalty

            # Smith-Waterman difference: include 0
            score_matrix[i][j] = max(
                0,
                diagonal_score,
                up_score,
                left_score
            )

            # Track maximum score cell
            if score_matrix[i][j] > max_score:
                max_score = score_matrix[i][j]
                max_i = i
                max_j = j

    aligned_seq1 = ""
    aligned_seq2 = ""

    # Start traceback from highest scoring cell
    i = max_i
    j = max_j

    # Traceback until score becomes 0
    while i > 0 and j > 0 and score_matrix[i][j] != 0:

        current_score = score_matrix[i][j]

        if seq1[i - 1] == seq2[j - 1]:
            score = match_score
        else:
            score = mismatch_penalty

        if current_score == score_matrix[i - 1][j - 1] + score:
            aligned_seq1 = seq1[i - 1] + aligned_seq1
            aligned_seq2 = seq2[j - 1] + aligned_seq2
            i -= 1
            j -= 1

        elif current_score == score_matrix[i - 1][j] + gap_penalty:
            aligned_seq1 = seq1[i - 1] + aligned_seq1
            aligned_seq2 = "-" + aligned_seq2
            i -= 1

        else:
            aligned_seq1 = "-" + aligned_seq1
            aligned_seq2 = seq2[j - 1] + aligned_seq2
            j -= 1

    return aligned_seq1, aligned_seq2, max_score, score_matrix


# ---------- Matrix Printing Function ----------

def print_matrix(matrix, seq1, seq2):
    print("      ", end="")

    for char in seq2:
        print(f"{char:4}", end="")
    print()

    for i in range(len(matrix)):
        if i == 0:
            print(" ", end=" ")
        else:
            print(seq1[i - 1], end=" ")

        for j in range(len(matrix[0])):
            print(f"{matrix[i][j]:4}", end="")
        print()


# ---------- Main Program ----------

seq1 = "GATTACA"
seq2 = "GCATGCU"

aligned_seq1, aligned_seq2, score, matrix = smith_waterman(seq1, seq2)

print("Original sequence 1:", seq1)
print("Original sequence 2:", seq2)
print()

print("Best Local Alignment Sequence 1:", aligned_seq1)
print("Best Local Alignment Sequence 2:", aligned_seq2)
print("Maximum Alignment Score:", score)
print()

print("Scoring Matrix:")
print_matrix(matrix, seq1, seq2)
