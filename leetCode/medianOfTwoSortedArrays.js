//per chatGPT
// The median of two sorted arrays can be found by merging the arrays into a single sorted array and then finding the middle element(s). Here's the algorithm to find the median of two sorted arrays:

// Create two pointers, p1 and p2, and initialize them to the start of the two arrays, nums1 and nums2, respectively.
// Create a variable, k, to store the desired position of the median in the merged array. If the total number of elements (m + n) is odd, then k is equal to (m + n + 1) / 2. If the total number of elements is even, then k is equal to (m + n) / 2.
// Loop until p1 and p2 are both less than their respective arrays, and decrement k with each iteration. In each iteration, compare the elements at p1 and p2 and move the pointer of the array with the smaller element to the next position.
// When one of the pointers reaches the end of its array, return the element at the other pointer plus the k - 1th element in the array as the median.
function findMedianSortedArrays(nums1, nums2) {
    let m = nums1.length, n = nums2.length;
    if (m > n) {
        [nums1, nums2, m, n] = [nums2, nums1, n, m];
    }
    let iMin = 0, iMax = m, halfLen = Math.floor((m + n + 1) / 2);
    while (iMin <= iMax) {
        let i = Math.floor((iMin + iMax) / 2);
        let j = halfLen - i;
        if (i < m && nums2[j-1] > nums1[i]) {
            iMin = i + 1;
        } else if (i > 0 && nums1[i-1] > nums2[j]) {
            iMax = i - 1;
        } else {
            let maxLeft;
            if (i === 0) {
                maxLeft = nums2[j-1];
            } else if (j === 0) {
                maxLeft = nums1[i-1];
            } else {
                maxLeft = Math.max(nums1[i-1], nums2[j-1]);
            }
            if ((m + n) % 2 === 1) {
                return maxLeft;
            }
            let minRight;
            if (i === m) {
                minRight = nums2[j];
            } else if (j === n) {
                minRight = nums1[i];
            } else {
                minRight = Math.min(nums1[i], nums2[j]);
            }
            return (maxLeft + minRight) / 2;
        }
    }
}
