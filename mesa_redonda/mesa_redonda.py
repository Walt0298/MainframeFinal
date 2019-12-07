import numpy as np
import pandas as pd
import itertools as it
import pandas as pd

participants = []


def preprocess():

    dataset = np.loadtxt(
        "mesa_redonda/input/participantes.txt", dtype=str, delimiter='\n')

    transformed_dataset = []

    for sentence in np.nditer(dataset):
        sentence = str(np.array_str(sentence)).replace('.', '').split(' ')

        company1 = sentence[3]
        multiplier = 1 if sentence[4] == 'aumenta' else -1
        idc = float(sentence[6]) * multiplier
        company2 = sentence[12]

        if not company1 in participants:
            participants.append(company1)
        if not company2 in participants:
            participants.append(company2)

        company1_id = participants.index(company1) + 1
        company2_id = participants.index(company2) + 1

        transformed_dataset.append([company1_id, idc, company2_id])

    return transformed_dataset


def build_idc_matrix(dataset):
    idc_matrix = []
    size = len(participants)
    for i in range(size):
        idc_matrix.append([])
        for j in range(size):
            idc = get_idc(dataset, i + 1, j + 1)
            idc_matrix[i].append(idc)

    return idc_matrix


def print_idc_matrix(idc_matrix):
    size = len(idc_matrix)
    head, body = "{:4}".format(""), ""
    for i in range(size):
        head += "{:8}".format(i+1)
    print(head)

    for i in range(size):
        body += "{:8}".format(i+1)
        for j in range(size):
            body += "{:8}".format(idc_matrix[i][j])
        body += "\n"

    print(body)


def more_less_conflictive(idc_matrix):
    sum_idc_list = []
    size = len(idc_matrix)

    for i in range(size):
        sum_idc_list.append(0)
        for j in range(size):
            sum_idc_list[i] += idc_matrix[i][j]
        for j in range(size):
            if j != i:
                sum_idc_list[i] += idc_matrix[j][i]

    return dict(
        more_conflictive=[participants[sum_idc_list.index(
            max(sum_idc_list))], max(sum_idc_list)],
        less_conflictive=[participants[sum_idc_list.index(
            min(sum_idc_list))], min(sum_idc_list)],
    )


def get_idc(dataset, company1_id, company2_id):
    idc = [dataset[i][1]
           for i in range(len(dataset))
           if dataset[i][0] == company1_id
           and dataset[i][2] == company2_id]
    idc = idc[0] if len(idc) > 0 else 0
    return idc


def sort_participants(dataset, k):
    permutations = it.permutations(
        range(1, len(participants) + 1), len(participants))
    permutations = [list(permutation) for permutation in permutations]
    sum_idc_list = []

    for seat_order in permutations:
        sum_idc = 0
        for i in range(1, len(seat_order)):
            idc = get_idc(dataset, seat_order[i - 1], seat_order[i])
            sum_idc += idc
        sum_idc_list.append(sum_idc)

    optimal_order = []

    while k > 0:
        min_idc = min(sum_idc_list)
        index = sum_idc_list.index(min_idc)
        optimal_order.append([permutations[index], min_idc])
        sum_idc_list[index] = float('Inf')
        k -= 1

    return optimal_order


def print_optimal_order(dataset, optimal_order):
    for index in range(1, len(optimal_order)):
        idc = get_idc(dataset, optimal_order[index - 1], optimal_order[index])
        effect = "aumenta" if idc > 0 else "disminuye"
        print("{0} se debe sentar junto a {1} debido a que el IDC {2} en {3} cuando estan juntos".format(
            participants[optimal_order[index - 1] - 1],
            participants[optimal_order[index] - 1],
            effect,
            abs(idc)
        ))


def generate_idc_matrix(m=8, n=8, numfiles=10):

    for numfile in range(1, numfiles + 1):

        random_idc_matrix = []

        for i in range(m):
            random_idc_matrix.append([])
            for j in range(n):
                if i == j:
                    random_idc = 0
                else:
                    random_idc = np.random.randint(
                        low=-100, high=100, size=1)[0]

                random_idc_matrix[i].append(random_idc)

        for i in range(m):
            for j in range(n):
                random_idc_matrix[i][j] = random_idc_matrix[j][i]

        df = pd.DataFrame(random_idc_matrix)
        df.to_csv(
            'mesa_redonda/output/Dataset{0}.csv'.format(numfile), index=None, header=False)


if __name__ == "__main__":

    dataset = preprocess()
    idc_matrix = build_idc_matrix(dataset)
    more_less_conflictive = more_less_conflictive(idc_matrix)
    optimal_order = sort_participants(dataset, 10)
    generate_idc_matrix()

    print(participants)
    print(dataset)
    print_idc_matrix(idc_matrix)
    print(more_less_conflictive)
    print(optimal_order)
    print_optimal_order(dataset, optimal_order[0][0])
