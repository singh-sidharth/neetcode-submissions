class Solution {
    /**
     * @param {string} text1
     * @param {string} text2
     * @return {number}
     */
    longestCommonSubsequence(text1, text2) {
        const dp = Array.from(Array(text1.length+1), () => Array(text2.length+1).fill(0));


        for (let i=text1.length-1; i > -1; i--){
            for (let j = text2.length-1; j>-1; j-- ){
                // matches the character
                if (text1[i] === text2[j]){
                    dp[i][j] = 1 + dp[i+1][j+1];
                }
                // doesn't match
                else {
                    dp[i][j] = Math.max(dp[i+1][j], dp[i][j+1]);
                }
            }
        }

        return dp[0][0];
    }
}
