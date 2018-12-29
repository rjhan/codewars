import java.util.*;
/*
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:

var result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
// result should == "apples, pears\ngrapes\nbananas"
*/


public class StripComments {

	public static String stripComments(String text, String[] commentSymbols) {
        List<String> list = new ArrayList<>();
        for (String s : text.split("\n")) {
            for (String var : commentSymbols) {
                if(s.contains(var)){
                    s = s.substring(0, s.indexOf(var));
                }  
            }
            
            list.add(("A"+s).trim().substring(1));
        }
		return String.join("\n", list);
    }
    
    public static void main(String[] args) {
        System.out.println(stripComments("apples, pears # and bananas\n     grapes\nbananas !apples", new String[] { "#", "!" }));
        // System.out.println(stripComments("a #b\nc\nd $e f g", new String[] { "#", "$" }));
    }
	
}