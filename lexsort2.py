import random


def ternary_quicksort(word_list, ordering):
    # If word_list is empty or single word, return as is
    if len(word_list) < 2:
        return word_list
    else:
        # Choose random pivot for quicksort and group together words based on pivot
        pivot = random.choice(word_list)
        smaller = [i for i in word_list if i < pivot]
        equal = [i for i in word_list if i == pivot]
        larger = [i for i in word_list if i > pivot]
        if ordering == 'standard':
            return ternary_quicksort(smaller, 'standard') + equal + ternary_quicksort(larger, 'standard')
        elif ordering == 'reverse':
            return ternary_quicksort(larger, 'reverse') + equal + ternary_quicksort(smaller, 'reverse')


def lex_sort(word_list, ordering):
    # Determine ordering
    if len(ordering) > 1:
        # Reverse ordering
        if ordering[0] > ordering[1]:
            return ternary_quicksort(word_list, 'reverse')
    return ternary_quicksort(word_list, 'standard')

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
