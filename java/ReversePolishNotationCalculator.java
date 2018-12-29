import java.util.Stack;

/*
Your job is to create a calculator which evaluates expressions in Reverse Polish notation.

For example expression 5 1 2 + 4 * + 3 - (which is equivalent to 5 + ((1 + 2) * 4) - 3 in normal notation) should evaluate to 14.

For your convenience, the input is formatted such that a space is provided between every token.

Empty expression should evaluate to 0.

Valid operations are +, -, *, /.

You may assume that there won't be exceptional situations (like stack underflow or division by zero).
*/
//java的实现方式暂未搞清原理，这个是排名第一的解法
//结果为14.0，不是14，但也通过了
public class ReversePolishNotationCalculator {

    public static double evaluate(String expr) {
        if (expr.equals("")) {
            return 0;
        }
        
        Stack<Double> stack = new Stack<Double>();
        String[] atoms = expr.split(" ");
        
        for (String atom: atoms) {
            Double a, b;
            switch (atom) {
                case "+": stack.push(stack.pop() + stack.pop()); break;
                case "-": b = stack.pop(); a = stack.pop(); stack.push(a - b); break;
                case "*": stack.push(stack.pop() * stack.pop()); break;
                case "/": b = stack.pop(); a = stack.pop(); stack.push(a / b); break;
                default:
                stack.push(Double.parseDouble(atom));
            }
        }
          
        return stack.pop();
    }

    public static void main(String[] args) {
        System.out.println(evaluate("5 1 2 + 4 * + 3 -"));
    }
    
}