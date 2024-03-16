class Permutations:
    @staticmethod
    def generate(elements: list) -> list[list]:
        num_elements = len(elements)
        cycle_index = [0] * num_elements

        result = [elements[:]]

        i = 0
        while i < num_elements:
            if cycle_index[i] < i:
                if i % 2 == 0:
                    elements[0], elements[i] = elements[i], elements[0]
                else:
                    elements[cycle_index[i]], elements[i] = elements[i], elements[cycle_index[i]]
                result.append(elements[:])

                cycle_index[i] += 1
                i = 0
            else:
                cycle_index[i] = 0
                i += 1
        return result
