import java.util.Arrays;
import java.util.HashSet;
import java.util.stream.Stream;

/* 
Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive alphabetic characters and 
numeric digits that occur more than once in the input string. 
The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice 
*/


public class CountingDuplicates {

    //利用Java8 中的stream，过滤出重复元素
  public static int duplicateCount1(String text) {

    String t = text.toLowerCase();

    HashSet<String> set = new HashSet<>(Arrays.asList(t.split("")));
 
    long l = set.stream()
        .filter(s->t.replace(s, "").length()<t.length()-1).count();

    return (int)l;

  }

  //常规解法：每次判断首字母是否重复，如果重复则将这个字母替换掉。并将重复数字+1
  public static int duplicateCount(String text){

    int duplicateCount = 0;
    text = text.toLowerCase();

    while(text.length()>0){
        String first = text.substring(0, 1);

        text = text.substring(1);

        if (text.contains(first)) {
            duplicateCount++;
            text = text.replace(first, "");
        }
    }

    return duplicateCount;
  }


  public static void main(String[] args) {

      System.out.println(duplicateCount("abcde")+"=>0");
      System.out.println(duplicateCount("aabbcde")+"=>2");
      System.out.println(duplicateCount("aabBcde")+"=>2");
      System.out.println(duplicateCount("abcdea")+"=>1");
      System.out.println(duplicateCount("indivisibility")+"=>1");
      System.out.println(duplicateCount("Indivisibilities")+"=>2");
      System.out.println(duplicateCount("aA11")+"=>2");
      System.out.println(duplicateCount("ABBA")+"=>2");
  }
}