# Lexicographical-Sort
Code for Qualia Code Challenge

The objective of the assignment was to write a function that could sort an array of strings based on an arbitrary lexicographic ordering.

I did this in two very similar ways. In lexsort.py, I simply determined the lexicographical ordering and called the sorted() method in Python, setting Reverse=True when the ordering was reverse alphabetical. In lexsort2.py, I once again determined the lexicographical ordering, but did the sorting by implementing ternary quicksort instead of calling the native sorted() method.

To determine the lexicographical ordering, I looked at the first and second characters of the ordering string; if the first character was a 'larger' character than the second (like 'c' > 'b'), then the ordering was determined to be reverse alphabetical. Otherwise, the ordering was standard alphabetical. If the ordering string was a single character, then the list was sorted in standard alphabetical order, which is equivalent to sorting by length from shortest to longest.

The time complexity for both are roughly the same, depending on the pivot choice in ternary quicksort. In general, determining the ordering is a constant time operation (looking up and comparing two characters), and sorting is O(|S| * n log n) time, where n is the number of words in the list and |S| is the length of the longest word in the list, as comparison between two strings involves iterating through each string character by character. Thus, the overall time complexity of both programs is O(|S| * n log n). Both methods also take O(n) space.
