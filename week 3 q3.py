vowels = ['a', 'e', 'i', 'o', 'u']# the vowel list
def vowel_remover(text, newText=''):
    if text == '': #if text equal to nothing print nothing/space
        print(newText)
    if text[0] not in vowels: #if the start of the text not in vowels list, then continue onwards with the rest of the text
        newText += text[0]
    print(vowel_remover(text[1:], newText))#print the text at position 1 to the end

vowel_remover('beautiful')
