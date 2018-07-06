
class Token(object):
    def __init__(self, t_type, t_value):
        self.type = t_type
        self.value = t_value

    def __repr__(self):
        return "Token({}, {})".format(self.type, self.value)

class Interpreter(object):
    def __init__(self, input_expr):
        self.expr = input_expr.replace(" ","")
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

        if target == "-":
            self.expr_pos += 1
            return Token("SUB", target)

        raise Exception("Cannot recognize {}".format(target))

    def expression(self):
        LEFT_FOUND = False
        OPERATOR_FOUND = False
        RIGHT_FOUND = False

        left_token = None
        operator_token = None
        right_token = None

        while True:
            next_token = self.get_next_token()
            #print("next_token = {}".format(next_token))

            if next_token.type == "EOF":
                if (not LEFT_FOUND) or (not OPERATOR_FOUND) or (not RIGHT_FOUND):
                    raise Exception("End but not find all needed tokens!")
                else:
                    break

            if next_token.type == "INTEGER":
                if not LEFT_FOUND:
                    LEFT_FOUND = True
                    left_token = next_token
                elif LEFT_FOUND and not OPERATOR_FOUND:
                    left_token.value = left_token.value * 10 + next_token.value
                elif OPERATOR_FOUND and not RIGHT_FOUND:
                    RIGHT_FOUND = True
                    right_token = next_token
                elif RIGHT_FOUND:
                    right_token.value = right_token.value * 10 + next_token.value
            elif next_token.type == "ADD" or next_token.type == "SUB":
                OPERATOR_FOUND = True
                operator_token = next_token

        if operator_token.type == "ADD":
            return left_token.value + right_token.value
        else:
            return left_token.value - right_token.value


if __name__ == '__main__':
    expression = input("Plz input the expr ==> ")
    it = Interpreter(expression)
    print("\n The answoer is {}".format(it.expression()))
