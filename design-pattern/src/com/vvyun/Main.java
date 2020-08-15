package com.vvyun;

import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        mergeSortedArray(new int[] { 1 }, new int[] { 1 });
    }

    /**
     * @param A: sorted integer array A
     * @param B: sorted integer array B
     * @return: A new sorted integer array
     */
    public static int[] mergeSortedArray(int[] A, int[] B) {
        // write your code here
        int[] c = new int[A.length + B.length];
        int tmpa = 0;
        int tmpb = 0;
        for (int i = 0; i < c.length; i++) {
            if (tmpa == A.length) {
                c[i] = B[tmpb];
                tmpb++;
                continue;
            }
            if (tmpb == B.length) {
                c[i] = A[tmpa];
                tmpa++;
                continue;
            }
            if (A[tmpa] >= B[tmpb]) {
                c[i] = B[tmpb];
                tmpb++;
            } else {
                c[i] = A[tmpa];
                tmpa++;
            }
        }
        return c;
    }

    /**
     * @param str:    An array of char
     * @param offset: An integer
     * @return: nothing
     */
    public void rotateString(char[] str, int offset) {
        // write your code here
        offset = offset % str.length;
        char[] tmp = new char[str.length];
        for (int i = 0; i < tmp.length; i++) {
            if (i < offset) {
                tmp[i] = str[str.length - offset + i];
            } else {
                tmp[i] = str[i - offset];
            }
        }
        for (int i = 0; i < tmp.length; i++) {
            str[i] = tmp[i];
        }
    }

    /**
     * @param n: An integer
     * @return: A list of strings.
     */
    public List<String> fizzBuzz(int n) {
        // write your code here
        List<String> res = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            String append = "";
            if (i % 3 == 0) {
                append += "fizz";
            }
            if (i % 5 == 0) {
                append += "".equals(append) ? "buzz" : " buzz";
            }
            append.trim();
            append = "".equals(append) ? i + "" : append;
            res.add(append);
        }
        return res;
    }

    /**
     * @param nums:   The integer array.
     * @param target: Target to find.
     * @return: The first position of target. Position starts from 0.
     */
    public int binarySearch(int[] nums, int target) {
        // write your code here
        int tmp = nums.length;
        tmp = tmp / 2;
        int comp = -1;
        while (tmp != 0) {
            if (nums[tmp] == target) {
                comp = tmp;
                tmp--;
            } else if (nums[tmp] > target) {
                tmp = tmp / 2;
            } else if (nums[tmp] < target) {
                tmp = tmp + tmp / 2;
            }
        }
        return comp;
    }

    // @param nestedList a list of NestedInteger
    // @return a list of integer
    public static List<Integer> flatten(List<NestedInteger> nestedList) {
        // Write your code here
        List<Integer> res = new ArrayList<>();
        // List<NestedInteger> tmp = new ArrayList<>();
        for (NestedInteger nestedInteger : nestedList) {
            if(nestedInteger.isInteger()){
                res.add(nestedInteger.getInteger());
            }else{
                nestedInteger.getList();
                // tmp
            }
        }

        return res;
    }

    public interface NestedInteger {

        // @return true if this NestedInteger holds a single integer,
        // rather than a nested list.
        public boolean isInteger();

        // @return the single integer that this NestedInteger holds,
        // if it holds a single integer
        // Return null if this NestedInteger holds a nested list
        public Integer getInteger();

        // @return the nested list that this NestedInteger holds,
        // if it holds a nested list
        // Return null if this NestedInteger holds a single integer
        public List<NestedInteger> getList();
    }
}