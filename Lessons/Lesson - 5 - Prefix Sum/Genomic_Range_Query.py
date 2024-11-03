"""



"""


def solution(S, P, Q):
    # Length of the DNA sequence
    N = len(S)

    # Prefix sums for the impact factors
    # Each index of the array holds the count of A,C,G,T at that index
    prefix_counts = [[0] * (N + 1) for _ in range(4)]

    # Mapping nucleotides to their respective indices in prefix_counts
    nucleotide_to_index = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

    # Fill in the prefix_counts
    for i in range(N):
        # Update the counts for each nucleotide
        for j in range(4):
            prefix_counts[j][i + 1] = prefix_counts[j][i]
        nucleotide_index = nucleotide_to_index[S[i]]
        prefix_counts[nucleotide_index][i + 1] += 1

    # Process the queries
    results = []
    for k in range(len(P)):
        start = P[k]
        end = Q[k]

        # Check the counts for A, C, G, T in the range start to end
        for j in range(4):
            if prefix_counts[j][end + 1] - prefix_counts[j][start] > 0:
                results.append(j + 1)  # impact factor is j + 1
                break

    return results

## or

def solution(S, P, Q):
    # Length of the DNA sequence
    N = len(S)

    # Prefix sums for the impact factors
    # Each index of the array holds the count of A,C,G,T at that index
    prefix_counts = [[0] * (N + 1) for _ in range(4)]

    # Mapping nucleotides to their respective indices in prefix_counts
    nucleotide_to_index = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

    # Fill in the prefix_counts
    for i in range(N):
        # Update the counts for each nucleotide
        for j in range(4):
            prefix_counts[j][i + 1] = prefix_counts[j][i]
        nucleotide_index = nucleotide_to_index[S[i]]
        prefix_counts[nucleotide_index][i + 1] += 1

    # Process the queries
    results = []
    for k in range(len(P)):
        start = P[k]
        end = Q[k]

        # Check the counts for A, C, G, T in the range start to end
        for j in range(4):
            if prefix_counts[j][end + 1] - prefix_counts[j][start] > 0:
                results.append(j + 1)  # impact factor is j + 1
                break

    return results

## or


def solution(S, P, Q):
    arr2 = []
    for i,j in zip(P,Q):
        if "A" in S[i:j+1]:
            arr2.append(1)
        elif "C" in S[i:j+1]:
            arr2.append(2)
        elif "G" in S[i:j+1]:
            arr2.append(3)
        elif "T" in S[i:j+1]:
            arr2.append(4)
        else:
            return S[i:j+1]
    return arr2
