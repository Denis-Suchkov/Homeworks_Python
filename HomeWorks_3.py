
# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.

LIST_1 = [1, 2, 3, 3, "A", "I", "A", 1, "P", "0", 0]
LIST_2 = [1, 2, 3, 4, "B", "X", "Y", "Y", "0", 0, 9]


def double_items(work_list: list) -> list:
    return list(set([i for i in work_list if work_list.count(i) > 1]))


def main():
    print(f"{LIST_1} - {double_items(LIST_1)}")
    print(f"{LIST_2} - {double_items(LIST_2)}")


if __name__ == "__main__":
    main()




# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. 
# Не учитывать знаки препинания и регистр символов. 
# За основу возьмите любую статью из википедии или из документации к языку.

from typing import Dict, Any

WORK_TEXT = "But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born " \
            "and I will give you a complete account of the system, and expound the actual teachings of the great " \
            "explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids " \
            "pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure " \
            "rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or " \
            "pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances " \
            "occur in which toil and pain can procure him some great pleasure. To take a trivial example, which of " \
            "us ever undertakes laborious physical exercise, except to obtain some advantage from it? But who has " \
            "any right to find fault with a man who chooses to enjoy a pleasure that has no annoying consequences, " \
            "or one who avoids a pain that produces no resultant pleasure? On the other hand, we denounce with " \
            "righteous indignation and dislike men who are so beguiled and demoralized by the charms of pleasure of " \
            "the moment, so blinded by desire, that they cannot foresee the pain and trouble that are bound to " \
            "ensue; and equal blame belongs to those who fail in their duty through weakness of will, which is the " \
            "same as saying through shrinking from toil and pain. These cases are perfectly simple and easy to " \
            "distinguish. In a free hour, when our power of choice is untrammelled and when nothing prevents our " \
            "being able to do what we like best, every pleasure is to be welcomed and every pain avoided. But in " \
            "certain circumstances and owing to the claims of duty or the obligations of business it will frequently " \
            "occur that pleasures have to be repudiated and annoyances accepted. The wise man therefore always " \
            "holds in these matters to this principle of selection: he rejects pleasures to secure other greater " \
            "pleasures, or else he endures pains to avoid worse pains.But I must explain to you how all this " \
            "mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account " \
            "of the system, and expound the actual teachings of the great explorer of the truth, the master-builder " \
            "of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but " \
            "because those who do not know how to pursue pleasure rationally encounter consequences that are " \
            "extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, " \
            "because it is pain, but because occasionally circumstances occur in which toil and pain can procure " \
            "him some great pleasure. To take a trivial example, which of us ever undertakes laborious physical " \
            "exercise, except to obtain some advantage from it? But who has any right to find fault with a man who " \
            "chooses to enjoy a pleasure that has no annoying consequences, or one who avoids a pain"


FREQUENT_COUNT = 10


def most_frequent_words(text: str, count_words: int) -> dict:

    words_list = text.upper() \
        .replace(".", " ") \
        .replace(",", " ") \
        .replace(";", " ") \
        .replace(":", " ") \
        .replace("!", " ") \
        .replace("?", " ") \
        .replace(" - ", " ") \
        .split()

    words_count = {}
    for w in words_list:
        words_count[w] = words_list.count(w)

    return dict(sorted(words_count.items(), key=lambda item: item[1], reverse=True)[:count_words])


def main():
    for i, w in enumerate(most_frequent_words(WORK_TEXT, FREQUENT_COUNT).items(), 1):
        print(f"{i:2}. {w[0]:<10} - {w[1]}")


if __name__ == "__main__":
    main()




# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.


def pack_backpack(items, max_weight):
    possible_items = []
    for item, weight in items.items():
        if weight <= max_weight:
            possible_items.append(item)
            max_weight -= weight
    return possible_items

items = {'палатка': 6, 'ботинки': 5, 'еда': 4, 'джинсы': 3, 'вода': 2, 'ложка': 1}
max_weight = 10
print(pack_backpack(items, max_weight)) 



