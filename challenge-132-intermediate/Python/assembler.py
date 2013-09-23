

class Assembler(object):
    instructions = {
        'and': {
            'variants': [
                {
                    'byte_code': '0x00',
                    'format': '[register] [register]'
                },
                {
                    'byte_code': '0x01',
                    'format': '[register] variable'
                }
            ]
        }
    }

    output = []

    def compile_line(self, line):
        line = line.strip()
        if line == '':
            pass

        tokens = line.split(' ')
        try:
            instruction = self.instructions[tokens[0].lower()]
        except KeyError:
            raise Exception("Unrecognized instruction {0}".format(tokens[0]))

        print(instruction)

        pass

    def compile(self, lines):
        try:
            for line in lines:
                self.compile_line(line)
        except Exception as e:
            print("Compilation error.", e)

        return self.output


def main():
    inp = open("test.asm").read().splitlines()
    a = Assembler()
    a.compile(inp)


if __name__ == "__main__":
    main()