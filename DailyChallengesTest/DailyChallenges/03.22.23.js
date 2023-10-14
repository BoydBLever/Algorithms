var minScore = function(n, roads) {
    roads.sort((a, b) => a[2] - b[2]);
    const dsu = new DSU(n);
    let ans = -1;
    
    for (let i = 0; i < roads.length; i++) {
        const [a, b, distance] = roads[i];
        dsu.union(a, b);
        if (dsu.find(1) == dsu.find(n)) {
            ans = distance;
            break;
        }
    }
    
    return ans;
};

class DSU {
    constructor(n) {
        this.parent = new Array(n + 1).fill(null).map((_, i) => i);
    }
    
    find(x) {
        if (this.parent[x] !== x) {
            this.parent[x] = this.find(this.parent[x]);
        }
        return this.parent[x];
    }
    
    union(x, y) {
        this.parent[this.find(x)] = this.find(y);
    }
}
// https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/