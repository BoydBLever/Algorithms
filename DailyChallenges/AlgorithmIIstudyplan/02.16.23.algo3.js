// https://leetcode.com/problems/word-search/submissions/900164927/?envType=study-plan&id=algorithm-ii
var exist = function(board, word) {
    const m = board.length;
    const n = board[0].length;
    const visited = new Array(m);
    for (let i = 0; i < m; i++) {
        visited[i] = new Array(n).fill(false);
    }
    const dfs = (i, j, index) => {
        if (index === word.length) {
            return true;
        }
        if (i < 0 || i >= m || j < 0 || j >= n || visited[i][j] || board[i][j] !== word[index]) {
            return false;
        }
        visited[i][j] = true;
        const result = dfs(i + 1, j, index + 1) || dfs(i - 1, j, index + 1) || dfs(i, j + 1, index + 1) || dfs(i, j - 1, index + 1);
        visited[i][j] = false;
        return result;
    };
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (dfs(i, j, 0)) {
                return true;
            }
        }
    }
    return false;
};
