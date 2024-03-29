# imports libraries/modules for string, threading, and time
import string
import threading
import time

# timer started for program
start_timer = time.perf_counter()

# defined function to count number of times word/character is repeated
def count_occurrences(text_lines, word_counts):
  text_lines = text_lines.strip() # removes leading spaces and trailing whitespace/newline characters
  text_lines = text_lines.lower() # converts words/characters to lowercase to avoid mismatching/errors
  words = text_lines.split(" ") # splits text into individual words/characters
  # iterates/loops through each word in the list of words
  for word in words:
    word = word.translate(word.maketrans("", "", string.punctuation)) # removes punctuation from the words
    if word in word_counts: # checks if word/character is in dictionary and updates count
      word_counts[word] += 1 # increments count of words by 1 if already in word dictionary
    else:
      word_counts[word] = 1 # adds word to dictionary with count of 1 if not already in dictionary

word_counts = dict() # empty dictionary created to store the word/character count

# opens text file to be read by main program
with open("pg69085.txt", "r", errors = "ignore") as f:
  lines = f.readlines()

threads = [] # list created to store the threads

for line in lines: # loops/iterates each line in text file # loops/iterates each line in text file
  t = threading.Thread(target = count_occurrences, args = (line, word_counts)) # creates new thread that calls count_occurrences function with current text line and word_counts dictionary as arguments
  threads.append(t) # adds thread to list of threads
  t.start()

# opens new temporary word_counter.txt file
with open("word_counter.txt", "w") as f:
  for key in sorted(word_counts.keys()): # loops through the sorted keys in the word_counts dictionary that is made
    f.write("{}: {}\n".format(key, word_counts[key])) # writes every word and its occurences next to it as a list in the word_counter.txt file and outputs it in the newly created word_counter text file

# timer ended for program
end_timer = time.perf_counter()

# calculation for elapsed time
elapsed_timer = end_timer - start_timer
print("Program's total time elapsed to execute: {:.2f} seconds".format(elapsed_timer))
