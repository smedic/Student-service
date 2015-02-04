from os.path import exists

studenti = []


def str2student(line):
    if line[-1] == '\n':
        line = line[:-1]
    indeks, ime, prezime, roditelj, datum, jmbg, adresa, telefon, email, godina = line.split(' | ')
    stud = {
        'indeks': indeks,
        'ime': ime,
        'prezime': prezime,
        'roditelj': roditelj,
        'datum': datum,
        'jmbg': jmbg,
        'adresa': adresa,
        'telefon': telefon,
        'email': email,
        'godina': godina
    }
    return stud


def student2str(stud):
    return ' '.join([stud['indeks'], stud['ime'], stud['prezime'], stud['roditelj'],
                     stud['datum'], stud['jmbg'], stud['adresa'], stud['telefon'], stud['email'], stud['godina']])


def formatHeader():
    return \
        "Indeks  |Ime       |Prezime     |Ime rod.  |Datum rodj.|JMBG        |Email               |Godine\n" \
        "--------+----------+------------+----------+-----------+------------+--------------------+------"


def formatStudent(stud):
    return "{0:8}|{1:10}|{2:12}|{3:10}|{4:11}|{5:12}|{6:20}|{7:>6}".format(
        stud['indeks'], stud['ime'], stud['prezime'], stud['roditelj'], stud['datum'], stud['jmbg'], stud['email'],
        stud['godina'])


def formatStudents(studList):
    result = ""
    for stud in studList:
        result += formatStudent(stud) + '\n'
    return result


def formatAllStudents():
    return formatStudents(studenti)



def loadStudents():
    print("Load students!")
    checkFile()
    for line in open('studenti.txt', 'r').readlines():
        if len(line) > 1:
            stud = str2student(line)
            studenti.append(stud)


def clearStudents():
    studenti[:] = []

def saveStudents():
    file = open('studenti.txt', 'w')
    for stud in studenti:
        file.write(student2str(stud))
        file.write('\n')
    file.close()


def checkFile():
    if not exists('studenti.txt'):
        open('studenti.txt', 'w').close()


# list operations
def findStudent(indeks):
    for stud in studenti:
        if stud['indeks'] == indeks:
            return stud
    return None


def searchStudents(field, value):
    result = []
    for stud in studenti:
        if stud[field].upper() == value.upper():
            print('NASAO!')
            result.append(stud)
    return result


def addStudent(stud):
    studenti.append(stud)


def updateStudent(index, stud):
    studenti[index] = stud


def advanceStudent(stud):
    stud['godina'] = str(int(stud['godina']) + 1)


def findMin(studList, key, start):
    n = len(studList)
    if n == 0:
        return -1
    if start >= n:
        return -1
    if n - start == 1:
        return start
    min = studList[start]
    minPos = start
    for i in range(start + 1, n):
        if studList[i][key] < min[key]:
            min = studList[i]
            minPos = i
    return minPos


def sort(studList, key, start):
    minPos = findMin(studList, key, start)
    if minPos == -1:
        return
    studList[start], studList[minPos] = studList[minPos], studList[start]
    if start < len(studList) - 1:
        sort(studList, key, start + 1)


def sortStudents(key):
    sort(studenti, key, 0)


def bubbleSort(key):
    for i in range(0, len(studenti)):
        for j in range(0, len(studenti)):
            if studenti[j][key] > studenti[i][key]:
                studenti[i], studenti[j] = studenti[j], studenti[i]


def main():
    loadStudents()
    print(formatHeader())
    print(formatAllStudents())
    searchStudents('ime', "Milojko")

    #studStr = { " SIT | Pera | Peric | Miki | 11.02.1994 | 434343 | 1. novembra 22 | 012 033 333 | peki@gmail.com | 3 "}

    stud = {
        'indeks': 'E3',
        'ime': 'Zoran',
        'prezime': 'Lukic',
        'roditelj': 'Nidza',
        'datum': '22.01.2001',
        'jmbg': '232323232',
        'adresa': 'Vase Stajica 22B',
        'telefon': '021 420 111',
        'email': 'zoki@gmail.com',
        'godina': '3'
    }
    addStudent(stud)
    #sortStudents('godina')
    print("SORTED:")
    clearStudents()
    loadStudents()
    bubbleSort('ime')
    print(formatHeader())
    print(formatAllStudents())
    #saveStudents()


if __name__ == "__main__":
    main()


loadStudents()








