def lex_sort(word_list, ordering):
    # Determine ordering
    if len(ordering) > 1:
        # Reverse ordering
        if ordering[0] > ordering[1]:
            return sorted(word_list, reverse=True)
    return sorted(word_list)


if __name__ == "__main__":
    list1 = lex_sort(['acb', 'abc', 'bca'], 'abc')
    list2 = lex_sort(['acb', 'abc', 'bca'], 'cba')
    list3 = lex_sort(['aaa', 'aa', ''], 'a')
    list4 = lex_sort(['acb', 'abc', 'bca', 'abca', 'aabc', 'acbc'], 'abc')
    list5 = lex_sort(['acb', 'abc', 'bca', 'abca', 'aabc', 'acbc'], 'cba')

    print list1
    print list2
    print list3
    print list4
    print list5
