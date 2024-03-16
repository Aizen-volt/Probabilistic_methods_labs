class Combinations:
    @staticmethod
    def generate(elements: list, r: int) -> list[list]:
        result = []

        combination = [0] * r
        Combinations.__generate_helper(elements, r, 0, combination, result)

        return result

    @staticmethod
    def __generate_helper(elements: list, r: int, index: int, combination: list, result: list[list]) -> None:
        if index == r:
            result.append(combination[:])
            return

        for i in range(len(elements)):
            combination[index] = elements[i]
            Combinations.__generate_helper(elements[i + 1:], r, index + 1, combination, result)
