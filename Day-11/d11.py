import re

if __name__ == '__main__':
    # r2 = re.compile(r'[iol]')
    # r3 = re.compile(r'(\w)\1.*(\w)\2')

    password = 'abbceffg'
    m = re.search(r'[iol]', password)
    if not m:
        print('r2-no BAN LETTERS')
    else:
        print(f'r2 {m}')

    m = re.findall(r'(\w)\1.*(\w)\2', password)
    if m:
        print(f'r3 {len(m)}')
    else:
        print('r3-no match')
