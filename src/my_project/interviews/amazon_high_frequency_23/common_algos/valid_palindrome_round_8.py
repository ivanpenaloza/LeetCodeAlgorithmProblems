from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:

        # To lowercase
        s = s.lower()

        # Remove non-alphanumeric characters
        s = re.sub(pattern=r'[^a-zA-Z0-9]', repl='', string=s)

        # Determine if s is palindrome or not
        len_s = len(s)

        for i in range(len_s//2):

            if s[i] != s[len_s - 1 - i]:
                return False 
            
        return True 