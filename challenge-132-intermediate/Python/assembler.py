import re

class Assembler(object):
    instructions = {
        'and': {'[a] [a]': '0x00', '[a] a': '0x01'}
    }

    output = []

    def parse_instruction_params(self, line_num, instruction, arguments):
        args = re.sub('\d+', 'a', arguments)
        args = re.sub('\s{2,}', ' ', args)
        try:
            variant = instruction[args]
        except KeyError:
            raise Exception("Invalid arguments for instruction on line {0}.".format(line_num))

        return "{0} {1}".format(variant, ' '.join(['{0:#04x}'.format(int(x)) for x in re.findall('\d+', arguments)]))

        pass

    def compile_line(self, line_num, line):
        line = line.strip()
        if line == '':
            return

        tokens = line.split(' ')
        try:
            instruction = self.instructions[tokens[0].lower()]
        except KeyError:
            raise Exception("Unrecognized instruction '{0}' on line {1}.".format(tokens[0], line_num))

        compiled_line = self.parse_instruction_params(line_num, instruction, ' '.join(tokens[1:]))
        print(compiled_line)
        #print(instruction)

        pass

    def compile(self, lines):
        try:
            for line_num, line in enumerate(lines):
                self.compile_line(line_num, line)
        except Exception as e:
            print("Compilation error.", e)

        return self.output


def main():
    inp = open("test.asm").read().splitlines()
    a = Assembler()
    a.compile(inp)


if __name__ == "__main__":
    main()