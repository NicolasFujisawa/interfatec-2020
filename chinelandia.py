def solution():
    number_of_pairs = int(input())
    pairs = []
    freq_left = {}
    freq_right = {}

    for i in range(0, number_of_pairs):
        pairs.append(parse_input(input()))

    for pair in pairs:
        if pair['left_pair'] in freq_left:
            freq_left[pair['left_pair']] += 1
        else:
            freq_left[pair['left_pair']] = 1

        if pair['right_pair'] in freq_right:
            freq_right[pair['right_pair']] += 1
        else:
            freq_right[pair['right_pair']] = 1

    output(freq_right, freq_left)


def parse_input(pair):
    left_pair, right_pair = pair.split(" ")

    return {'left_pair': left_pair, 'right_pair': right_pair}


def invert_sorting(foot_initial):
    if foot_initial == "E":
        return 0
    else:
        return 1


def output(freq_right, freq_left):
    output_list = []

    for k, v in freq_right.items():
        if v > 1:
            output_list.append([k, "D", v-1])
    for k, v in freq_left.items():
        if v > 1:
            output_list.append([k, "E", v-1])

    if not output_list:
        print("SEM TROCAS DESTA VEZ")
    else:
        for output in sorted(output_list, key=lambda output: (int(output[0]), invert_sorting(output[1]))):
            print("{} {} {}".format(output[0], output[1], output[2]))


solution()
