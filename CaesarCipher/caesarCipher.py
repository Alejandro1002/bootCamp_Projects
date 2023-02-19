# import
from dataFile import alphabet_list

# defining class
class CaesarCipher:

    # attributes
    def __init__(self, cipher, txt, times):
        self.cipher = cipher
        self.txt = txt
        self.times = times
        self.generated_text = ''

    # methods
    # encoding
    def encodingText(self):
        for item in self.txt:
            if item in alphabet_list:
                currentIndex = alphabet_list.index(item)
                newIndex = currentIndex + self.times
                letterFound = alphabet_list[newIndex]
                self.generated_text += letterFound
            else:
                self.generated_text += item

        return self.generated_text

    # decoding
    def decodingText(self):
        for item in self.txt:
            if item in alphabet_list:
                currentIndex = alphabet_list.index(item)
                newIndex = currentIndex - self.times
                letterFound = alphabet_list[newIndex]
                self.generated_text += letterFound

            else:
                self.generated_text += item

        return self.generated_text