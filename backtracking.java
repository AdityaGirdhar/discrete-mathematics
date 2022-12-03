import java.util.Scanner;

public class Solution {
    static boolean find(char[][] arr, String str, int i, int j) {
            if (str.length() < 2) {
                return (str.charAt(0) == arr[i][j]);
            }
            arr[i][j] = '0';
            int[] plusMinus = {-1, 1};
            for (int k : plusMinus) {
                if (i+k < 0 || i+k > arr.length-1) {
                    continue;
                }
                boolean found = false;
                if (arr[i+k][j] == str.charAt(1)) {
                    found = find(arr, str.substring(1), i+k, j);
                }
                if (found) {
                    return true;
                }
            }

            for (int l : plusMinus) {
                if (j+l < 0 || j+l > arr.length-1) {
                    continue;
                }
                boolean found = false;
                if (arr[i][j+l] == str.charAt(1)) {
                    found = find(arr, str.substring(1), i, j+l);
                }
                if (found) {
                    return true;
                }
            }
            return false;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt(); // rows
        int m = scan.nextInt(); // columns
        char[][] arr = new char[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                arr[i][j] = scan.next().charAt(0);
            }
        }
        String str = scan.next();
        boolean found = false;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (arr[i][j] == str.charAt(0)) {
                    found = find(arr.clone(), str, i, j);
                    if (found) {
                        System.out.println("YES");
                        return;
                    }
                }
            }
        }
        System.out.println("NO");
    }
}
