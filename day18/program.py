from collections import defaultdict


class Program(object):
    def __init__(self, instructions, **initialisation):
        self.instructions = instructions
        self.registers = defaultdict(int, **initialisation)

        self.pc = 0
        self.queue = []
        self.sent_list = []

    def get_value(self, token):
        try:
            return int(token)
        except ValueError:
            return self.registers[token]

    def run_instruction(self, cmd, args):
        if cmd == 'set':
            x, y = args
            self.registers[x] = self.get_value(y)
        elif cmd == 'add':
            x, y = args
            self.registers[x] += self.get_value(y)
        elif cmd == 'mul':
            x, y = args
            self.registers[x] *= self.get_value(y)
        elif cmd == 'mod':
            x, y = args
            self.registers[x] %= self.get_value(y)

        elif cmd == 'jgz':
            x, y = args
            if self.get_value(x) > 0:
                self.pc += self.get_value(y)
            else:
                self.pc += 1
            return True

        elif cmd == 'snd':
            self.sent_list.append(self.get_value(args[0]))
        elif cmd == 'rcv':
            if not self.queue:
                return False
            self.registers[args[0]] = self.queue.pop(0)

        else:
            raise ValueError(cmd)

        self.pc += 1
        return True

    def run_next_instruction(self):
        if not 0 <= self.pc < len(self.instructions):
            return False

        parsed = self.instructions[self.pc].split()
        cmd = parsed[0]
        args = parsed[1:]

        return self.run_instruction(cmd, args)

    def run_until_block(self):
        can_continue = True
        while can_continue:
            can_continue = self.run_next_instruction()

        sent_list = self.sent_list
        self.sent_list = []
        return sent_list
