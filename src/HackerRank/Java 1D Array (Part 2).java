/**
 * https://www.hackerrank.com/challenges/java-1d-array/problem
 * Using stack or recursion
 */
//1. Solution using stack
public static boolean canWin(int leap, int[] game) {
    Stack<Integer> stack = new Stack<>();
    int n = game.length;
    Boolean[] visited = new Boolean[n];
    Arrays.fill(visited, Boolean.FALSE);
    Integer i;

    stack.push(0);
    while (!stack.empty()) {
        i = stack.pop();
        if (i == n - 1 | i + leap > n - 1) {
            return true;
        }

        if (game[i+1] == 0 && !visited[i+1]) {
            stack.push(i+1);
            visited[i+1] = true;
        }

        if (game[i+leap] == 0 && !visited[i+leap]) {
            stack.push(i+leap);
            visited[i+leap] = true;
        }

        if (i > 0 && game[i-1] == 0 && !visited[i-1]) {
            stack.push(i-1);
            visited[i-1] = true;
        }
    }
    return false;
}

//2. Solution using recursion
public static boolean canWin(int leap, int[] game) {
    return isSolvable(leap, game, 0);
}

private static boolean isSolvable(int leap, int[] game, int i) {
    // Base Cases
    if (i >= game.length) {
        return true;
    } else if (i < 0 || game[i] == 1) {
        return false;
    }
            
    game[i] = 1; // marks as visited

    // Recursive Cases
    return isSolvable(leap, game, i + leap) || 
           isSolvable(leap, game, i + 1) || 
           isSolvable(leap, game, i - 1);
}
