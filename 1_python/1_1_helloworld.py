args=['gcc', 'hello.c', 'world.c']

match args:
    case 'gcc':
        print('gcc: missing source file(s)')
    case ['gcc', file1, files]:
        print('gcc compile: ' + file1 + " " + files)
    case ['clean']:
        print('clean')
    case _:
        print('invalid command')

for arg in args:
    print(arg)