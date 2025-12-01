from math import floor

class Computer:

    def __init__(self, a, b, c, program):
        self.a = a
        self.originalA = a
        self.b = b
        self.originalB = b
        self.c = c
        self.originalC = c
        self.program = program
        self.pointer = 0
        self.jumped = False
        self.output = []

    def __repr__(self):
        return 'A: {}, B: {}, C: {}, Program: {}, Pointer: {}, Jumped: {}, Output: {}]'.format(self.a, self.b, self.c, self.program, self.pointer, self.jumped, self.output)

    def __eq__(self, other):
        return (self.a == other.b) & \
               (self.b == other.b) & \
               (self.c == other.c) & \
               (self.program == other.program) & \
               (self.pointer == other.pointer) & \
               (self.jumped == other.jumped) & \
               (self.output == other.output)

    def __hash__(self):
        return hash((self.a, self.b, self.c, self.program, self.pointer, self.jumped, self.output))

    def reset(self):
        self.a = self.originalA
        self.b = self.originalB
        self.c = self.originalC
        self.pointer = 0
        self.jumped = False
        self.output = []


    def performInstruction(self, opcode, operand):
        if opcode == 0:
            self.adv(operand)
        elif opcode == 1:
            self.bxl(operand)
        elif opcode == 2:
            self.bst(operand)
        elif opcode == 3:
            self.jnz(operand)
        elif opcode == 4:
            self.bxc()
        elif opcode == 5:
            self.out(operand)
        elif opcode == 6:
            self.bdv(operand)
        else:
            self.cdv(operand)
        if self.jumped:
            self.jumped = False
        else:
            self.pointer += 2

    def getComboOperand(self, operand):
        if operand <= 3:
            return operand
        if operand == 4:
            return self.a
        if operand == 5:
            return self.b
        if operand == 6:
            return self.c
        return None

    def adv(self, operand):
        self.a = floor(self.a / pow(2, self.getComboOperand(operand)))

    def bxl(self, operand):
        self.b = self.b ^ operand

    def bst(self, operand):
        self.b = self.getComboOperand(operand) % 8

    def jnz(self, operand):
        if self.a != 0:
            self.pointer = operand
            self.jumped = True

    def bxc(self):
        self.b = self.b ^ self.c

    def out(self, operand):
        self.output.append(str(self.getComboOperand(operand) % 8))

    def bdv(self, operand):
        self.b = floor(self.a / pow(2, self.getComboOperand(operand)))

    def cdv(self, operand):
        self.c = floor(self.a / pow(2, self.getComboOperand(operand)))

    def run(self):
        while self.pointer < len(self.program):
            self.performInstruction(self.program[self.pointer], self.program[self.pointer + 1])
        return self.output