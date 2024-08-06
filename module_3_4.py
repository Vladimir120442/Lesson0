def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        j = i.upper()
        if j in root_word.upper():
            same_words.append(i)
        elif root_word.upper() in j:
            same_words.append(i)
    return same_words


res1 = print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
res2 = print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))



