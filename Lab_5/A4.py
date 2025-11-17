import sys

original_stdout = sys.stdout

with open('genedata.0.txt', 'w', encoding='utf-8') as f:
    sys.stdout = f

    print("Lukashevich Vlad")
    print("Генетический поиск")

    # def coder_chains(some_chains):
    #     proto = list(some_chains)
    #
    #     new_chain = []
    #     i = 0
    #
    #     while i < len(proto) - 1:
    #         first_el = proto[i]
    #         second_el = proto[i + 1]
    #         count = 0
    #         ending = (i != len(proto) - 2)
    #
    #         if first_el != second_el and ending:
    #             new_chain.append(first_el)
    #         elif first_el == second_el and ending:
    #             for j in range(i, len(proto) - 1):
    #                 if first_el == proto[j]:
    #                     count += 1
    #                 else:
    #                     if count >= 3 and count <= 9:
    #                         new_chain.append(str(count))
    #                         new_chain.append(first_el)
    #                         i += count
    #                     elif count == 2:
    #                         new_chain.append(first_el)
    #                     count = 0
    #         elif first_el != second_el and not ending:
    #             new_chain.append(first_el)
    #             new_chain.append(second_el)
    #         i += 1
    #     s = "".join(new_chain)
    #     return s


    def decoder_chains(some_coded_chain):
        proto = list(some_coded_chain)
        new_chain = []
        i = 0

        while i < len(proto):
            current_el = proto[i]

            if current_el.isdigit() and int(current_el) >= 3 and int(current_el) <= 9:
                count = int(current_el)
                next_el = proto[i + 1] if i + 1 < len(proto) else None

                if next_el:
                    for j in range(count):
                        new_chain.append(next_el)
                    i += 2
                else:
                    new_chain.append(current_el)
                    i += 1
            else:
                new_chain.append(current_el)
                i += 1

        s = "".join(new_chain)
        return s

    with open("sequences.0.txt", "r") as file:
        text = file.read().replace("\n", "\t").split("\t")
        text.pop(-1)
        i = 0
        protein = []
        creature = []
        chains = []
        while len(text) > i + 1:
            protein.append(text[i])
            creature.append(text[i + 1])
            chains.append(text[i + 2])
            i += 3

    proteins_chains = dict(zip(protein, chains))


    def search(some_part_protein, some_chain):
        decoded_chain = decoder_chains(some_chain)
        if some_part_protein in decoded_chain:
            return True
        else:
            return False

    def diff(first_chain, second_chain):
        decoded_first = decoder_chains(first_chain)
        decoded_second = decoder_chains(second_chain)

        difference_count = 0
        if len(decoded_first) != len(decoded_second):
            difference_count += abs(len(decoded_first) - len(decoded_second))
            if len(decoded_first) > len(decoded_second):
                i = 0
                while i < len(decoded_second):
                    if decoded_first[i] != decoded_second[i]:
                        difference_count += 1
                    i += 1
            else:
                i = 0
                while i < len(decoded_first):
                    if decoded_first[i] != decoded_second[i]:
                        difference_count += 1
                    i += 1
        else:
            i = 0
            while i < len(decoded_first):
                if decoded_first[i] != decoded_second[i]:
                    difference_count += 1
                i += 1

        return difference_count


    def mode(chain):
        decoded_chain = decoder_chains(chain)
        d = {}
        for key in decoded_chain:
            d[key] = d.get(key, 0) + 1
        l = []
        for k, v in d.items():
            l.append((v, k))
        l.sort(reverse=True)
        card = l[0]
        print(card[1], "\t\t\t", card[0])


    with open("commands.0.txt", "r") as file:
        print("-" * 60)
        count_command = 0
        for line in file:
            command = line.replace("\n", "").split("\t")

            if command[0] == "search":
                count_command += 1
                dec = decoder_chains(command[1])
                print(f"{(count_command):03d}\tsearch\t{dec}")
                print("{:<12}    {:>15}".format("organism", "protein"))

                found = False
                i = 0
                while i < len(protein):
                    if search(decoder_chains(command[1]), chains[i]):
                        print("{:<12}    {:<25}".format(creature[i], protein[i]))
                        found = True
                    i += 1

                if not found:
                    print("NOT FOUND")
                print("-" * 60)

            if command[0] == "diff":
                count_command += 1
                print(f"{(count_command):03d}\tdiff\t{command[1]}\t{command[2]}")
                print("amino-acids difference:")
                print(diff(proteins_chains[command[1]], proteins_chains[command[2]]))
                print("-" * 60)
            if command[0] == "mode":
                count_command += 1
                print(f"{(count_command):03d}\tmode\t{command[1]}")
                print("amino-acids occurs:")
                mode(proteins_chains[command[1]])
                print("-" * 60)

    sys.stdout = original_stdout