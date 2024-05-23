import re

class MyString:
    def __init__(self, value=''):
        if not isinstance(value, str):
            print(ValueError("The value must be a string."))
        self.value = value

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        # Replace multiple consecutive spaces with a single space
        cleaned_string = re.sub(' +', ' ', self.value)
        # Add a period to the end of the string if it doesn't already have one
        if not cleaned_string.endswith('.'):
            cleaned_string += '.'
        # Split the string into a list of sentences based on punctuation marks
        sentences = cleaned_string.split('.|?|!')
        # Remove empty strings from the list
        sentences = [sentence for sentence in sentences if sentence]
        return len(sentences)