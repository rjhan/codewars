import java.util.*;
import java.util.stream.Collectors;



/*
Create a function taking a positive integer as its parameter and returning a string containing the Roman Numeral representation of that integer.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

Example:

solution(1000) # should return 'M'
Help:

Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000
Remember that there can't be more than 3 identical symbols in a row.

More about roman numerals - http://en.wikipedia.org/wiki/Roman_numerals

*/

public class RomanNumeralsEncoder{
    
    public static String solution(int n){

        Map<Integer,String> map = new HashMap<Integer,String>();

        map.put(1, "I");
        map.put(4, "IV");
        map.put(9, "IX");
        map.put(5, "V");
        map.put(10, "X");
        map.put(40, "XL");
        map.put(50, "L");
        map.put(90, "XC");
        map.put(100, "C");
        map.put(400, "CD");
        map.put(500, "D");
        map.put(900, "CM");
        map.put(1000, "M");

        String roman_numerals = "";

        List<Integer> list = map.keySet().stream().sorted(Comparator.reverseOrder()).collect(Collectors.toList());

        for (Integer key : list) {
            while (n>=key) {
                roman_numerals+=map.get(key);
                n-=key;
            }
        }
        
        return roman_numerals;
    }

    public static void main(String[] args) {
        System.out.print(solution(1889));
    }
}