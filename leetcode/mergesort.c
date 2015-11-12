#include <stdlib.h>
#include <stdio.h>


int mergeSort(int* nums, int len);
int* merge(int* nums1, int len1, int* nums2, int len2);

int main()
{
    int a[] = {79, 1, 77, 74, 62, 8, 14, 54, 92, 42, 16, 82, 56, 34, 91, 11, 6, 83, 19, 98, 26, 37, 69, 31, 2, 39, 27, 67, 72, 5, 9, 55, 61, 20, 63, 94, 78, 71, 48, 80, 22, 58, 45, 4, 97, 23, 15, 3, 99, 60, 95, 12, 30, 10, 47, 18, 13, 50, 29, 64, 40, 51, 96, 46, 0, 36, 85, 17, 59, 33, 68, 86, 88, 32, 7, 35, 52, 70, 57, 87, 93, 66, 89, 76, 21, 90, 65, 24, 44, 81, 53, 43, 28, 73, 38, 49, 25, 41, 75, 84};
    int *res;
    int i;
    for (i = 0; i < 10000; ++i)
    {
        res = mergeSort(a, 100);
    }
    /*
    for (i = 0; i < 100; ++i)
    {
        printf("%d ", res[i]);
    }
    printf("\n");
    */
}

int mergeSort(int* nums, int len)
{
    int mp;
    int *l, *r;
    if (len == 1)
        return nums;
    mp = (len-1)/2;
    l = mergeSort(nums, mp+1);
    r = mergeSort((int*)&nums[mp+1], len-mp-1);
    return merge(l, mp+1, r, len-mp-1);
}

int* merge(int* nums1, int len1, int* nums2, int len2)
{
    int * res;
    int i, j;
    int p;
    i = 0;
    j = 0;
    p = 0;
    res = malloc(4*(len1+len2));
    while (i < len1 && j < len2)
    {
        if (nums1[i] <= nums2[j])
            res[p++] = nums1[i++];
        else
            res[p++] = nums2[j++];
    }
    while (i < len1)
        res[p++] = nums1[i++];
    while (j < len2)
        res[p++] = nums2[j++];
    return res;
}


