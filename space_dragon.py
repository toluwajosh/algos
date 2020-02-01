"""Space Dragon.
Write and algorithm to reverse the order of an array of letters which form a series of words.
"""


def reverse_array_between(string_array, front, rear):
    while rear > front:
        # print(front, rear)
        r_char = string_array[rear]
        f_char = string_array[front]
        string_array[rear] = f_char
        string_array[front] = r_char
        front += 1
        rear -= 1

    return string_array


def reverse_array(string_array):
    front = 0
    rear = len(string_array) - 1
    return reverse_array_between(string_array, front, rear)



def reverse_words_in_array(string_array):
    string_array = reverse_array(string_array)
    prev = 0
    for i in range(len(string_array)):
        if string_array[i]==' ':
            string_array = reverse_array_between(string_array, prev, i-1)
            prev = i+1
    string_array = reverse_array_between(string_array, prev, len(string_array)-1)
    return string_array

if __name__ == "__main__":
    # print(reverse_words_in_array(['p', 'e', 'r', 'f', 'e', 'c', 't', ' ',
    #                                 'm', 'a', 'k', 'e', 's', ' ',
    #                                 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]))
    # print(reverse_words_in_array(['c', ' ',
    #                             'b', ' ',
    #                             'a' ]))
    
    # edge case
    print(reverse_words_in_array(['c', ' ',
                                'a' ]))