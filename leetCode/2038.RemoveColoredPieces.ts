function winnerOfGame(colors: string): boolean {
    let aStreaks: number[] = [], bStreaks: number[] = [];
    let count = 1;

    // Count consecutive streaks of 'A's and 'B's
    for (let i = 1; i < colors.length; i++) {
        if (colors[i] === colors[i - 1]) {
            count++;
        } else {
            if (colors[i - 1] === 'A' && count >= 3) {
                aStreaks.push(count);
            } else if (colors[i - 1] === 'B' && count >= 3) {
                bStreaks.push(count);
            }
            count = 1;
        }
    }
    if (colors[colors.length - 1] === 'A' && count >= 3) {
        aStreaks.push(count);
    } else if (colors[colors.length - 1] === 'B' && count >= 3) {
        bStreaks.push(count);
    }

    // Calculate moves for Alice and Bob
    let aliceMoves = aStreaks.reduce((acc, val) => acc + val - 2, 0);
    let bobMoves = bStreaks.reduce((acc, val) => acc + val - 2, 0);

    // If Alice has more moves, she has a chance to win
    return aliceMoves > bobMoves;
}

// Test cases:
console.log(winnerOfGame("AAABABB"));  // true
console.log(winnerOfGame("AA"));       // false
