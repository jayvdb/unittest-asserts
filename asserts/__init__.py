# -*- coding: utf-8 -*-


def sparse_check(pattern, obj):
    """Рекурсивно проверить, что `obj` повторяет структуру `pattern`.

    `pattern` должен "входить" в состав `obj`. Это значит, что:

    - списки в `obj` должны иметь те же элементы, что в `pattern`,
      но в любом порядке;
    - словари в `obj` должны иметь все ключи
      из соответствующих словарей в `pattern`
      (но могут содержать и другие);
    - прочие значения должны быть просто равны.

    Это удобно в тестах при проверке JSON-ответов от API.
    """

    if isinstance(pattern, dict):
        if not isinstance(obj, dict):
            raise AssertionError('{0} and {1} have different types')
        for key in pattern:
            sparse_check(pattern[key], obj.get(key))
    elif isinstance(pattern, list):
        if not isinstance(obj, list):
            raise AssertionError('{0} and {1} have different types')
        covered = [False for elem in pattern]
        for elem in obj:
            for i, pattern_elem in enumerate(pattern):
                if not covered[i] and sparse_check(pattern_elem, elem):
                    covered[i] = True
                    break
            else:
                raise AssertionError('Hmm, some strange error in unittest assertion library')
        if not all(covered):
            raise AssertionError('Some elements are not in the list')

    else:
        assert obj == pattern
