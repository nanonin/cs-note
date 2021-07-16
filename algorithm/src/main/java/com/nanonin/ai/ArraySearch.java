package com.nanonin.ai;

import java.util.Arrays;

public class ArraySearch {

    public static void main(String[] args) {
        int[] array = new int[]{1, 8, 5, 67, 3};
        new ArraySearch().qSort(array, 0, array.length - 1);
        System.out.println(Arrays.toString(array));
    }

    public void qSort(int[] array, int start, int end) {
        if (start >= end) return;
        int mid = array[end];
        int l = start;
        int r = end - 1;
        while (l < r) {
            while (l < r && array[l] < mid) l++;
            while (l < r && array[r] >= mid) r--;
            if (l < r) swap(array, l, r);
        }
        if (array[l] > mid) {
            swap(array, l, end);
        } else {
            l++;
        }
        qSort(array, start, l - 1);
        qSort(array, l + 1, end);

    }

    private void swap(int[] array, int a, int b) {
        int tmp = array[a];
        array[a] = array[b];
        array[b] = tmp;
    }

}
