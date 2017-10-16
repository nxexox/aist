from collections import Counter

def mixer(array):
    result = []
    mode, mode_count = Counter(array).most_common(1)[0]

    if len(array) // 2 + 1 > mode_count:
        reverse = False

        print('Ок, этот массив можно перемешать, соблюдая условие')

        while array:

            if not reverse:
                result.append(array.pop())

            elif reverse:
                result.append(array.pop(0))

            reverse = not reverse

    else:

        print('Этот массив бесполезно перемешивать, условие не будет соблюдено')

        return array

    return result


if __name__ == '__main__':
    print(mixer([1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2]))
    print(mixer([1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8]))
    print(mixer([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4]))
    print(mixer([1, 1, 1, 1, 2]))
    print(mixer([9, 8, 7, 6, 5, 4, 3, 2, 1]))
