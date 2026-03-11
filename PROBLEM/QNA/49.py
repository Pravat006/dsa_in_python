'''
49. Reverse Words in a Sentence
Reverse the order of words in a sentence (not characters), preserving spaces.

Input: "hello world how are you"
Output: "you are how world hello"
'''
input_string = "Reverse the list of words"
words = input_string.split()
reversed_words = words[::-1]  
output_string = " ".join(reversed_words)
print(output_string) 
