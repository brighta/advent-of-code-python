from math import floor


class Monkey:

    def __init__(self, items, operation_symbol, operation_value, test_value, true_monkey, false_monkey):
        self.count = 0
        self.lowest_common_multiplier = 0
        self.items = [int(item) for item in items]
        self.operation_symbol = operation_symbol
        self.operation_value = operation_value
        self.test_value = int(test_value)
        self.true_monkey = int(true_monkey)
        self.false_monkey = int(false_monkey)

    def __repr__(self):
        string = "Monkey #:" + "\n"
        string += "  Starting items: " + ", ".join([str(item) for item in self.items]) + "\n"
        string += "  Operation: new = old " + self.operation_symbol + " " + self.operation_value + "\n"
        string += "  Test: divisible by " + str(self.test_value) + "\n"
        string += "    If true: throw to monkey " + str(self.true_monkey) + "\n"
        string += "    If false: throw to monkey " + str(self.false_monkey) + "\n"
        return string

    def get_test_value(self):
        return self.test_value

    def set_lowest_common_multiplier(self, lowest_common_multiplier):
        self.lowest_common_multiplier = lowest_common_multiplier

    def perform_operations(self, monkeys, worry_reduces):
        while len(self.items) != 0:
            item = self.items.pop(0)
            if self.operation_value == "old":
                value = item
            else:
                value = int(self.operation_value)
            if self.operation_symbol == "+":
                item += value
            else:
                item *= value
            if worry_reduces:
                item = floor(item / 3)
            else:
                item = item % self.lowest_common_multiplier
            if item % self.test_value == 0:
                monkey = self.true_monkey
            else:
                monkey = self.false_monkey
            monkeys[monkey].add_item(item)
            self.count += 1
        return monkeys

    def add_item(self, item):
        self.items.append(item)

    def get_count(self):
        return self.count
