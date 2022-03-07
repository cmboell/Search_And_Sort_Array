"""
Assignment: Search and Sort Array Assignment
Program: sort_and_search_array.py
Author: Colby Boell
Last date modified: 03/07/2022

The purpose of this program is to use functions to sort and search an array.
"""
# import array
import array as arr


# function for searching array
def search_array(the_arr, search_num):
    # convert the array into a normal list, so we can search for the index
    b = the_arr.tolist()
    # declare default index
    index = -1
    # try statement to test code
    try:
        index = b.index(search_num)
    except ValueError:
        index = index
    # use a return statement since we are looking for an index number which is a new variable we need
    # to return
    return index


# since we are searching for the index of a certain number we return the index (location number is in the array)
def sort_array(an_arr):
    # turning array into a regular list
    c = an_arr.tolist()
    # sort function
    c.sort()
    # used a return statement because we created a new list variable to sort the array
    # then return it sorted
    return c


if __name__ == '__main__':
    # creating the array
    a = arr.array('i', [6, 12, 7, 13, 4, 1, 8])
    # statements that call and print result of search array
    print('Searching array for 1,12, and 56 (Return -1 if not found)')
    print(search_array(a, 1))
    print(search_array(a, 12))
    print(search_array(a, 56))

    # calling sort array and printing it
    print('Sorted Array\n', sort_array(a))

"""
Results:
Searching array for 1,12, and 56 (Return -1 if not found
5
1
-1
Sorted Array
 [1, 4, 6, 7, 8, 12, 13]
"""
