def word_frequency(sentence):
    # Remove punctuation and convert to lower case
    sentence = ''.join(ch for ch in sentence if ch.isalnum() or ch.isspace()).lower()
    
    # Split the sentence into words
    words = sentence.split()
    
    # Dictionary to hold the frequency of each word
    frequency_dict = {}
    
    # Count the frequency of each word
    for word in words:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1
    
    return frequency_dict

sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)