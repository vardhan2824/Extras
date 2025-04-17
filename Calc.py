import re
import math

class BODMASCalculator:
    def __init__(self):
        self.operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
            '^': lambda x, y: x ** y,
        }
        self.precedence = {'^': 4, '*': 3, '/': 3, '+': 2, '-': 2}
    
    def evaluate_expression(self, expression):
        # Remove all whitespace
        expression = expression.replace(' ', '')
        
        # Validate expression characters
        if not self._validate_expression(expression):
            return None, "Invalid characters in expression"
        
        try:
            # Convert expression to tokens
            tokens = self._tokenize(expression)
            
            # Convert infix to postfix notation
            postfix = self._infix_to_postfix(tokens)
            
            # Evaluate postfix expression
            result = self._evaluate_postfix(postfix)
            
            return result, None
        except (ValueError, ZeroDivisionError, OverflowError, IndexError) as e:
            return None, str(e)
    
    def _validate_expression(self, expr):
        # Check for invalid characters
        valid_chars = re.compile(r'^[\d+\-*/().^]+$')
        return bool(valid_chars.match(expr))
    
    def _tokenize(self, expression):
        # Tokenize the expression into numbers, operators, and parentheses
        token_pattern = re.compile(r'(\d+\.?\d*|\.\d+|[+\-*/()^])')
        tokens = []
        for token in token_pattern.finditer(expression):
            token = token.group()
            if token in self.operations or token in '()':
                tokens.append(token)
            else:
                try:
                    # Try to convert to float (handles both integers and decimals)
                    tokens.append(float(token))
                except ValueError:
                    raise ValueError(f"Invalid number: {token}")
        
        # Handle unary minus operators
        tokens = self._handle_unary_minus(tokens)
        return tokens
    
    def _handle_unary_minus(self, tokens):
        # Convert unary minuses to negative numbers
        processed = []
        for i, token in enumerate(tokens):
            if token == '-':
                if i == 0 or tokens[i-1] == '(' or tokens[i-1] in self.operations:
                    # This is a unary minus, combine with next number
                    if i+1 < len(tokens) and isinstance(tokens[i+1], (int, float)):
                        processed.append(-tokens[i+1])
                        tokens[i+1] = None  # Mark next token to skip
                    else:
                        raise ValueError("Invalid use of unary minus")
                else:
                    processed.append(token)
            elif token is not None:
                processed.append(token)
        return processed
    
    def _infix_to_postfix(self, tokens):
        output = []
        operator_stack = []
        
        for token in tokens:
            if isinstance(token, (int, float)):
                output.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                # Pop until matching '(' is found
                while operator_stack and operator_stack[-1] != '(':
                    output.append(operator_stack.pop())
                if not operator_stack:
                    raise ValueError("Mismatched parentheses")
                operator_stack.pop()  # Remove the '('
            else:  # It's an operator
                while (operator_stack and operator_stack[-1] != '(' and
                       self.precedence[operator_stack[-1]] >= self.precedence[token]):
                    output.append(operator_stack.pop())
                operator_stack.append(token)
        
        # Pop remaining operators
        while operator_stack:
            if operator_stack[-1] == '(':
                raise ValueError("Mismatched parentheses")
            output.append(operator_stack.pop())
        
        return output
    
    def _evaluate_postfix(self, postfix):
        stack = []
        
        for token in postfix:
            if isinstance(token, (int, float)):
                stack.append(token)
            else:  # It's an operator
                if len(stack) < 2:
                    raise ValueError("Invalid expression - not enough operands")
                y = stack.pop()
                x = stack.pop()
                
                try:
                    result = self.operations[token](x, y)
                    stack.append(result)
                except ZeroDivisionError:
                    raise ZeroDivisionError("Division by zero")
                except OverflowError:
                    raise OverflowError("Result too large")
        
        if len(stack) != 1:
            raise ValueError("Invalid expression")
        
        return stack[0]
    
    def calculate_with_error_recovery(self):
        print("BODMAS Calculator (Enter 'quit' to exit)")
        previous_result = None
        
        while True:
            expression = input("\nEnter expression: ").strip()
            
            if expression.lower() in ('quit', 'exit', 'q'):
                break
            
            if not expression:
                continue
            
            # Allow users to reference previous result with 'ans'
            if previous_result is not None:
                expression = expression.replace('ans', str(previous_result))
            
            result, error = self.evaluate_expression(expression)
            
            if error:
                print(f"Error: {error}")
                # Try to find where the error might have occurred
                if "Mismatched parentheses" in error:
                    print("Please check your parentheses pairs")
                elif "Division by zero" in error:
                    print("Cannot divide by zero")
                elif "Invalid number" in error:
                    print("Please check your numeric values")
                elif "not enough operands" in error:
                    print("Please check your operator placement")
                else:
                    print("Please check your expression syntax")
                
                # Offer to continue with corrected expression
                continue_option = input("Would you like to try again? (y/n): ").lower()
                if continue_option != 'y':
                    break
            else:
                print(f"Result: {result}")
                previous_result = result


if __name__ == "__main__":
    calculator = BODMASCalculator()
    calculator.calculate_with_error_recovery()
