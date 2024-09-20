#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
all_door_options = (1,2,3)  # tuple
my_door_choice = 1  # 1,2,3
i_won = 0
reps = 100000
for i in range(reps):
    secret_winning_door = np.random.choice(all_door_options)
    all_door_options_list = list(all_door_options)
    # take the secret_winning_door, so we don't show it as a "goat" losing door
    all_door_options_list.remove(secret_winning_door)
    try:
        # if my_door_choice was secret_winning_door then it's already removed
        all_door_options_list.remove(my_door_choice)
    except:
        pass
    # show a "goat" losing door and remove it
    goat_door_reveal = np.random.choice(all_door_options_list)
    all_door_options_list.remove(goat_door_reveal)

    # put the secret_winning_door back in if it wasn't our choice
    # we previously removed it, so it would be shown as a  "goat" losing door
    if secret_winning_door != my_door_choice:
        all_door_options_list.append(secret_winning_door)
    # if secret_winning_door was our choice then all that's left in the list is a "goat" losing door
    # if secret_winning_door wasn't our choice then it's all that will be left in the list

    # swap strategy
    my_door_choice = all_door_options_list[0]

    if my_door_choice == secret_winning_door:
        i_won += 1

i_won/reps


# In[2]:


import numpy as np

# Set up
reps = 100000  # Number of simulations
wins = 0  # Count of wins

for i in range(reps):
    # Randomly choose the winning door (1, 2, or 3)
    winning_door = np.random.choice([1, 2, 3])
    
    # You always pick door 1 initially
    my_choice = 1
    
    # Host opens a door that is not your choice and not the winning door
    # Since you picked door 1, the only other doors are 2 and 3.
    # If the winning door is door 1, the host randomly opens door 2 or 3.
    # If the winning door is door 2, the host opens door 3 (and vice versa).
    
    if winning_door == 1:
        # Host opens either door 2 or 3 (both are goats)
        revealed_door = np.random.choice([2, 3])
    else:
        # Host opens the other door that is not the winner
        revealed_door = 6 - 1 - winning_door  # This is just the other non-winning door
    
    # You switch to the remaining unopened door
    switched_choice = 6 - 1 - revealed_door  # The remaining door after switching

    # Check if you win by switching
    if switched_choice == winning_door:
        wins += 1

# Calculate and print the win rate
win_rate = wins / reps
print(f"Win rate by switching: {win_rate}")


# In[3]:


import numpy as np

# Number of simulations
reps = 100000
wins = 0

for i in range(reps):
    # Randomly pick the winning door (1, 2, or 3)
    winning_door = np.random.choice([1, 2, 3])
    
    # You always choose door 1
    my_choice = 1
    
    # You switch to the other door (which will be different from door 1)
    # If door 1 is the winning door, you lose by switching
    # If door 1 is not the winning door, you win by switching
    if my_choice != winning_door:
        wins += 1

# Calculate the probability of winning by switching
win_rate = wins / reps
print(f"Win rate by switching: {win_rate}")


# In[1]:


# Markov Chains and Text Generation
from IPython.display import YouTubeVideo
YouTubeVideo('56mGTszb_iM', width = 550)


# Question 6
# 
# 1.) In my opinion, ChatGPT was very helpful when it came to answering my questions. When a code was provided, it explained in detail what each line did in the context of that code, 
# and when I asked follow up questions to further explain it more in depth, it was able to do in a clear way.
# 
# 2.) As long as I knew what to ask, I think that it wasn't frustrating to use ChatGPT to figure things out. 
# If I asked specific questions, the chatbot was able to answer in a concise way.
# 
# 3.)Overall I think ChatBots are a useful tool to help understand codes. 
# They explain every code functions in an easy to understand way, and are able to explain what each line does in the context of that code. 
# However, when I'm trying to figure out why a code is not working, the chatbot is unhelpful because I couldn't pinpoint what was causing the error.
# Therefore I ended up asking vague questions, and ChatGPT couldn't pinpoint the errors. 
# As long as you don't ask broad questions, then ChatBots are a powerful tool to use.

# Question 7.
# 
# Since joining this course, my thoughts on AI-driven assistance tools in the context of learning statistics is that it can be very useful.
# It is able to provide different codes, optimize them, and explain what they do while not doing the work for you. 
# In no way it is perfect, the user is required to have a basic understanding of what they are trying to achieve and how to do it.
# Otherwise if an error occurs in the code, the AI tool may not be able to help since they may not always find what causes the error.

# Question 8.
# 
# 4.) In conclusion, skills such as learning and adaptability, communication, coding, and data analysis are essential to have if I want a career in statistics. Particularly, coding and data analysis are crucial skill sets to have because without them, I would be very limited on what I can do. Now if I want to also pursue a PhD in statistics, I would also need other skill sets such as: mathematical foundation, statistical theory, research skills, computational statistics, machine learning, domain knowledge, interdisciplinary collaboration, communication, critical thinking, and networking. A good way to acquire them would be to first start taking the required math courses to build my mathematical foundation, and take supplementary courses in other fields of study to better apply statistical knowledge. But above else, I should take the necessary statistical courses because it will help me build foundational knowledge and help acquire the necessary skill sets.
# 
# 5.)While ChatGPT was helpful in pointing me in the right direction to take in my studies, I felt that the advice it gave me was very generalized and vague. If I wanted to have more in-depth knowledge on which direction to take in my studies and career, I would talk to an expert who already has experience because they could give me a more detailed answer that will suit uniquely to me and my goals.

# Question 9.
# 
# Yes.

# Here’s a summary of our interactions, based on your queries about the Monty Hall problem and the coding involved:
# 
# ---
# 
# ### **Interaction Summary: Monty Hall Simulation**
# 
# We explored the Monty Hall problem through a series of Python code implementations. The Monty Hall problem is a well-known probability puzzle based on a game show where a contestant picks one of three doors. Behind one door is a prize, while the others hide goats. After the contestant makes a choice, the host reveals a goat behind one of the remaining doors and offers the contestant the chance to switch to the other unopened door. The puzzle demonstrates that switching doors provides a higher probability of winning.
# 
# **Key steps in our discussion:**
# 
# 1. **Original Code Review:**
#    - You provided a Python simulation of the Monty Hall problem using NumPy to simulate 100,000 trials. The initial code was well-structured but a bit complex, involving steps where the host revealed a losing door and the contestant switched to the remaining door.
#    - The code then checked if the contestant's new choice (after switching) matched the door with the prize, recording the win rate.
# 
# 2. **Simplification Request:**
#    - You asked for a simpler version of the Monty Hall code, and I provided a cleaned-up version that streamlined the logic while still following the core mechanics of the game.
#    - This simplified version removed unnecessary steps like converting the tuple to a list and handling exceptions, focusing more on simulating the key moments of the game: picking a door, revealing a losing door, and switching.
# 
# 3. **Further Simplification:**
#    - You requested an even more basic version of the code, and I provided a minimalistic approach. In this version, we eliminated the step where the host reveals a goat door, and instead focused only on the key fact that if the contestant's initial choice wasn’t the winning door, switching would lead to a win.
#    - This helped clarify the central idea: switching doors leads to a 2/3 chance of winning.
# 
# ---
# 
# Would you like me to add anything more to this summary or clarify specific parts?
# 
# https://chatgpt.com/share/66e9baa5-7d58-8011-ab4f-be156d535d7c

# Sure! Here's a summary of our interactions about the Markov chain:
# 
# 1. You shared a Python code snippet for a **Markovian chatbot**. The code builds two key structures:
#    - `word_used`: A dictionary that keeps track of how many times each word appears in the input text.
#    - `next_word`: A dictionary that records what word(s) commonly follow each word and counts how often each follow-up word appears.
# 
# 2. I explained how the code works:
#    - It loops through a list of words and updates both dictionaries based on word sequences.
#    - For each word, it checks what comes after it and updates the `next_word` dictionary to store the frequency of transitions between words.
#    - The structure is useful for generating text based on word patterns in a Markov chain model.
# 
# 3. I also explained how **Markov chains** work:
#    - A Markov chain chatbot can generate responses by selecting the next word based on the probabilities of word transitions observed in the input text. The chatbot continues generating a sequence of words by following these transition probabilities.
# 
# Would you like more clarification or detail on any part of this?
# 
# https://chatgpt.com/share/66eb85a4-1284-8011-9ed5-7057e47215f8

# In this chat, we discussed your Markovian chatbot code extension that uses **bigrams** (two-word sequences) instead of individual words to create a more context-aware model. The key components are:
# 
# 1. **`word_used2`**: Tracks how often each bigram appears.
# 2. **`next_word2`**: Records what word typically follows a bigram and how frequently it occurs.
# 
# This bigram-based approach helps generate more coherent responses by considering word pairs, improving transition predictions.
# 
# Let me know if you'd like to go further with this!
# 
# https://chatgpt.com/share/66ebaf79-e368-8011-808e-cf1e1d7d5acb

# Certainly! Here’s a summary of our interactions regarding your code and its extension:
# 
# ### Original Code
# 1. **Purpose**: Your original code snippet counts occurrences of words and tracks the sequences of words in a list.
# 2. **Key Components**:
#    - `word_used`: Tracks how often each word appears.
#    - `next_word`: Tracks how often a word is followed by another word.
# 3. **Improvements Suggested**:
#    - Use `defaultdict` to simplify dictionary initialization and increment operations.
#    - Provided an optimized version using `defaultdict` to make the code more concise and easier to manage.
# 
# ### Extended Code
# 1. **Purpose**: The extended code analyzes word sequences within the context of specific characters extracted from a dataset.
# 2. **Key Components**:
#    - `characters`: A `Counter` object created by transforming the `character` column of a dataset to uppercase and replacing spaces with dots.
#    - `word_used2C`: Tracks two-word sequences for each character and their frequencies.
#    - `next_word2C`: Tracks the word that follows each two-word sequence for each character and how often it follows.
# 3. **Issues & Suggestions**:
#    - **Initialization**: Replaced manual dictionary checks with `defaultdict` for cleaner and more efficient code.
#    - **Simplification**: Provided an optimized version of the code using `defaultdict` to handle nested dictionaries and avoid redundant checks.
# 
# ### Replacing Spaces with Dots
# 1. **Purpose**: Replacing spaces with dots in the character names ensures consistent formatting, avoids potential conflicts, and meets specific formatting requirements of your application or system.
# 2. **Reasons**:
#    - **Data Normalization**: Ensures consistent and uniform format.
#    - **Unique Identification**: Treats names as single entities, avoiding issues with spaces.
#    - **Avoiding Conflicts**: Prevents potential parsing or tokenization issues.
#    - **Custom Format Needs**: Meets the specific requirements of the target system or application.
# 
# This summary encapsulates the key points and improvements discussed regarding your code and its extension. If you need any further details or clarifications, feel free to ask!
# 
# https://chatgpt.com/share/66ebb853-df10-8011-95d6-83abd2c12c86

# Sure! Here's a summary of our chat:
# 
# You asked about the relevance of certain skills (learning and adaptability, communication, coding, and statistics and data analysis) in the modern world, particularly in the data science industry. I explained that these skills are critical for career opportunities in the field, especially for roles like data scientist and statistician. Coding and data analysis are especially fundamental to both roles, as they involve working with large datasets and applying statistical methods or machine learning models.
# 
# You then asked if it was possible to become a statistician or data scientist without coding or doing data analysis. I explained that while it would be difficult, particularly for a data scientist, these skills are essential for both professions. However, there are adjacent fields (e.g., business analyst, project management) that require less technical involvement.
# 
# Finally, you asked what other skills would be valuable if you want to be a statistician and pursue a PhD in statistics. I listed key skill sets such as mathematical foundation, statistical theory, research skills, computational statistics, machine learning, domain knowledge, interdisciplinary collaboration, communication, critical thinking, and networking. These will be important to help you succeed in both a PhD program and your future career as a statistician.
# 
# https://chatgpt.com/share/66ec5d5e-4fd4-8011-b5a7-c7ff568399f8
