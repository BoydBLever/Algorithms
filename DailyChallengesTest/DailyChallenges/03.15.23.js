var isCompleteTree = function (root) {
    if (!root) return true;

    let queue = [root];
    let foundNull = false;

    while (queue.length > 0) {
        let currentNode = queue.shift();

        if (currentNode === null) {
            foundNull = true;
        } else {
            if (foundNull) return false;

            queue.push(currentNode.left);
            queue.push(currentNode.right);
        }
    }

    return true;
};

// https://leetcode.com/problems/check-completeness-of-a-binary-tree/description/