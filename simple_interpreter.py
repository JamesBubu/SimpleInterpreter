
class Token(object):
    def __init__(self, t_type, t_value):
        self.type = t_type
        self.value = t_value

    def __repr__(self):
        return "Token({t}, {v})".format(self.type, self.value)

class Interpreter(object):
    def __init__(self, input_expr):
        self.expr = input_expr
        self.expr_pos = 0

    def get_next_token(self):
        if self.expr_pos >= len(self.expr):
            return Token("EOF", None)

        target = self.expr[self.expr_pos]
        if target.isdigit():
            self.expr_pos += 1
            return Token("INTEGER", int(target))

        if target == "+":
            self.expr_pos += 1
            return Token("ADD", target)

        raise Exception("Cannot recognize {}".format(target))

    def expression(self):
        left_operand = self.get_next_token()
        if left_operand.type != "INTEGER":
            raise Exception("Wrong left operand type {}".format(left_operand.type))

        operator = self.get_next_token()
        if operator.type != "ADD":
            raise Exception("This should be operator")

        right_operand = self.get_next_token()
        if right_operand.type != "INTEGER":
            raise Exception("Wrong right operand type {}".format(right_operand.type))

        eof_operand = self.get_next_token()
        if eof_operand.type != "EOF":
            raise Exception("This should be EOF!")

        return left_operand.value + right_operand.value


if __name__ == '__main__':
    expression = input("Plz input the expr ==> ")
    it = Interpreter(expression)
    print("\n The answoer is {}".format(it.expression()))
