import re
import sys


class Assembler(object):
    instructions = {
        'and': {'[a] [a]': '0x00', '[a] a': '0x01'},
        'or': {'[a] [a]': '0x02', '[a] a': '0x03'},
        'xor': {'[a] [a]': '0x04', '[a] a': '0x05'},
        'not': {'[a]': '0x06'},
        'mov': {'[a] [a]': '0x07', '[a] a': '0x08'},
        'random': {'[a]': '0x09'},
        'add': {'[a] [a]': '0x0a', '[a] a': '0x0b'},
        'sub': {'[a] [a]': '0x0c', '[a] a': '0x0d'},
        'jmp': {'[a]': '0x0e', 'a': '0x0f'},
        'jz': {'[a] [a]': '0x10', '[a] a': '0x11', 'a [a]': '0x12', 'a a': '0x13'},
        'jeq': {'[a] [a] [a]': '0x14', 'a [a] [a]': '0x15', '[a] [a] a': '0x16', 'a [a] a': '0x17'},
        'jls': {'[a] [a] [a]': '0x18', 'a [a] [a]': '0x19', '[a] [a] a': '0x1a', 'a [a] a': '0x1b'},
        'jgt': {'[a] [a] [a]': '0x1c', 'a [a] [a]': '0x1d', '[a] [a] a': '0x1e', 'a [a] a': '0x1f'},
        'halt': {'': '0xff'},
        'aprint': {'[a]': '0x20', 'a': '0x21'},
        'dprint': {'[a]': '0x22', 'a': '0x23'}
    }

    output = []

    def parse_instruction(self, line_num, instruction, arguments):
        args = re.sub('\d+', 'a', arguments)
        args = re.sub('\s{2,}', ' ', args)
        try:
            variant = instruction[args]
        except KeyError:
            raise Exception("Invalid arguments for instruction on line {0}.".format(line_num))

        return "{0} {1}".format(variant, ' '.join(['{0:#04x}'.format(int(x)) for x in re.findall('\d+', arguments)]))

    def compile_line(self, line_num, line):
        line = line.strip()
        if line == '':
            return

        tokens = line.split(' ')
        try:
            instruction = self.instructions[tokens[0].lower()]
        except KeyError:
            raise Exception("Unrecognized instruction '{0}' on line {1}.".format(tokens[0], line_num))

        self.output.append(self.parse_instruction(line_num, instruction, ' '.join(tokens[1:])))

    def compile(self, lines):
        try:
            for line_num, line in enumerate(lines):
                self.compile_line(line_num, line)
        except Exception as e:
            print("Compilation error.", e)

        return self.output


def main(argv):
    with open(argv[0]) as ass_file:
        [print(line) for line in (Assembler()).compile(ass_file.read().splitlines())]


if __name__ == "__main__":
    main(sys.argv[1:])