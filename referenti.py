
referenti = []

def ref2str(ref):
    return ' '.join([ref['ime'], ref['prezime'], ref['username'],ref['password']])
    
def str2ref(line):
    if line[-1] == '\n':
        line = line[:-1]
    ime, prezime, username, password = line.split(' | ')
    ref = {
        'ime': ime,
        'prezime': prezime,
        'username': username,
        'password': password
    }
    return ref


def loadRefs():
    for line in open('referenti.txt', 'r').readlines():
        if len(line) > 1:
            ref = str2ref(line)
            referenti.append(ref)
            
def login(username, password):
    for ref in referenti:
        if ref['username'] == username and ref['password'] == password:
            return True
    return False

def main():
    print()
    loadRefs()
    for ref in referenti:
        print(ref2str(ref))
        
    username = input("Korisnicko ime >> ")
    password = input("Sifra >> ")
    if login(username, password):
        print("uspesno")
    else: 
        print("Neuspesno")
    
if __name__ == "__main__":
    main()

