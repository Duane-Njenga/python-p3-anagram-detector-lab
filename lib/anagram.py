# your code goes here!

class Anagram:
    def __init__(self, init_word):
        self.init_word = init_word

    def match(self, word_list):
        matched_list = []
        for word in word_list: 

            if(sorted(list(self.init_word)) == sorted(list(word))):  
               matched_list.append(word) 
        return matched_list
            
                         

