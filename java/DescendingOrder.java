import java.util.*;



/*
 Your task is to make a function that can take any non-negative integer as a argument 
and return it with its digits in descending order. 
Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 21445 Output: 54421

Input: 145263 Output: 654321

Input: 1254859723 Output: 9875543221

 */

/**
 * 存在一个问题：
 * codewars测试的结果应该有一个9875543221，但这个结果已经超过int的范围，所以会报错
 * 但codewars中并没有报错，直接通过
 * 由于题目中规定返回的是int，所以这个地方暂且忽略
 */


public class DescendingOrder {
    public static int sortDesc(final int num) {
        String [] strings = String.valueOf(num).split("");
        
        Arrays.sort(strings,Collections.reverseOrder());

        return Integer.parseInt(String.join("", strings));
    }

    public static void main(String[] args) {
        System.out.println(sortDesc(21445));
        System.out.println(sortDesc(145263));
        System.out.println(sortDesc(125485972));
    }
  }