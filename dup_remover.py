# Дано: список dict-объектов вида вида {"key": "value"},
# например [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"},
# {}, {}, {"key1": "value1"}, {"key1": "value1"}, {"key2": "value2"}].

# Напишите функцию, которая удаляет дубликаты из этого списка.
# Для примера выше возвращаемое значение может быть равно
# [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {"key2": "value2"}].
# Обязательное условие: функция не должна иметь сложность O(n^2).

import json


def duplicate_remover(initial_list):
    dup_free_set = set()
    dup_free_list = []
    for element in initial_list:
        str_element = json.dumps(element)
        if str_element not in dup_free_set:
            dup_free_set.add(str_element)
            dup_free_list.append(element)
    return dup_free_list

def main():
    duplicate_list = [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"},
        {}, {}, {"key1": "value1"}, {"key1": "value1"}, {"key2": "value2"}]
    dup_free_list = duplicate_remover(duplicate_list)
    print(f"Список без дубликатов: {dup_free_list}")

if __name__ == "__main__":
    main()