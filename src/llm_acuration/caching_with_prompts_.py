# -*- coding: utf-8 -*-
"""Caching with prompts .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/159m81ffy2yCkpsndlaXeqdr0-97zu9NW
"""

# Install chromadb
!pip install chromadb

!pip install sentence_transformers

import json


class PromptCacher:
    def __init__(self, cache_file='prompts_and_answers.json'):
        """
        Initializes the PromptCacher class with a cache file.

        Args:
            cache_file (str): The filename to use for caching prompts and answers.
        """
        self.cache_file = cache_file
        self.cache = self.load_cache()

    def load_cache(self):
        """
        Loads cached prompts and answers from a JSON file.

        Returns:
            dict: The cached prompts and answers.
        """
        try:
            with open(self.cache_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_cache(self):
        """
        Saves the cached prompts and answers to a JSON file.
        """
        with open(self.cache_file, 'w') as file:
            json.dump(self.cache, file, indent=2)

    def get_answer(self, prompt):
        """
        Retrieves an answer from cache if available, otherwise prompts the user for an answer.

        Args:
            prompt (str): The prompt for which to retrieve an answer.

        Returns:
            str: The answer corresponding to the prompt.
        """
        if prompt in self.cache:
            return self.cache[prompt]
        else:
            answer = input(f"Prompt: {prompt}\nEnter answer: ")
            self.cache[prompt] = answer
            self.save_cache()
            return answer


def main():
    """
    Main function to interact with the PromptCacher class.
    """
    prompt_cacher = PromptCacher()

    while True:
        user_prompt = input("Enter a prompt (type 'exit' to end): ")
        if user_prompt.lower() == 'exit':
            break

        answer = prompt_cacher.get_answer(user_prompt)
        print(f"Answer: {answer}")


if __name__ == "__main__":
    main()

