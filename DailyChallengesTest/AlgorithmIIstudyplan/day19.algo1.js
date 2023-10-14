var rangeBitwiseAnd = function(left, right) {
    let shift = 0;
    while (left < right) {
        left >>= 1;
        right >>= 1;
        shift++;
    }
    return left << shift;
};

// In this problem, we are given a range [left, right], and we need to find the bitwise AND of all numbers in this range.

// We can solve this problem by first observing that the bitwise AND operation is such that the result will have a 1 in any bit position where all the numbers being ANDed have a 1, and 0 otherwise.

// So, for any two numbers i and j, if i < j, then the bitwise AND of all numbers in the range [i, j] must have a 0 in the bit position where the most significant bit of i and j differ, because the range includes both i and j, which have different values in that bit position.

// Therefore, if we keep shifting the bits of left and right to the right until they are equal, we can find the common prefix of all the numbers in the range. Then, we shift the common prefix to the left by the number of bits that we shifted to the right, to get the final result.

// We start by initializing a variable shift to 0, and then we keep shifting both left and right to the right by 1 until left is no longer less than right. For each shift, we increment shift by 1.

// After the loop, we shift left to the left by shift bits, and return the result. This gives us the bitwise AND of all the numbers in the range.
