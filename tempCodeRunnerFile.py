def generate_password():
    global passwd
    global match
    lst = [(33, 91), (97, 127)]
    collect_chr = [chr(k) for i, j in lst for k in range(i, j)]
    passwd = ''. join([choice(collect_chr) for l in range(1, 9)])
    rgx = ['\W', '[a-z]', '[A-Z]', '\d']
    match = list(filter(lambda x: re.search(r''+x+'', passwd), rgx))