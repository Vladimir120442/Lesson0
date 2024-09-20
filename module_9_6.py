def all_variants(text):
    dl = len(text)
    for i in range(dl):
        for j in range(i + 1, dl + 1):
            yield text[i:j]


result = all_variants('Я_смог!')
for i in result:
    print(i)
