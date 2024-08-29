#!/usr/bin/env python3

def return_evens(num_list):
    return [num for num in num_list if num % 2 == 0]
    # for num in num_list:
    #     if num % 2 == 0:
    #         print(num)
    #         return num_list
        # else:
        #     return []
    pass

def make_exclamation(sentence_list):
    return [sentence + '!' for sentence in sentence_list]
    pass