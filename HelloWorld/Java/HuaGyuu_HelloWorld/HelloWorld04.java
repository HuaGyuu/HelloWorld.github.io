public class HelloWorld04 {
    // l 计数和 o 计数
    static int lSum = 0;
    static int oSum = 0;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // 输入 Hello World 的随机组合
        String hello = sc.nextLine();
        // 转成 字符数组
        char[] arr1 = hello.toCharArray();
        // 用于存放 映射的数字
        int[] arr2 = new int[arr1.length];
        // 将字符映射为数字
        for (int i = 0; i < arr1.length; i++) {
            // 映射方法
            arr2[i] = charToInt(arr1, i);
        }
        // 插入排序
        // 外层从 i = 0 开始依次往后
        for (int i = 1; i < arr2.length; i++) {
            // 内层从 j = i 开始依次往前
            for (int j = i; j > 0; j--) {
                // 如果前面的值小于 j 处的值，就交换
                if (arr2[j] < arr2[j - 1]) {
                    int temp = arr2[j];
                    arr2[j] = arr2[j - 1];
                    arr2[j - 1] = temp;
                }else break; // 否则退出循环
            }
        }
        // 将数字映射为字符
        for (int i = 0; i < arr2.length; i++) {
            // 映射方法
            arr1[i] = intToChar(arr2, i);
        }
        // 输出字符数组
        for (char c : arr1) {
            System.out.print(c);
        }
    }

    public static int charToInt(char[] arr, int i) {
        // 用 switch 简单实现
        switch (arr[i]) {
            case 'H':
                return 0;
            case 'e':
                return 1;
            case 'l':
                switch (lSum++) {
                    case 0:
                        return 2;
                    case 1:
                        return 3;
                    case 2:
                        return 9;
                }
            case 'o':
                switch (oSum++) {
                    case 0:
                        return 4;
                    case 1:
                        return 7;
                }
            case ' ':
                return 5;
            case 'W':
                return 6;
            case 'r':
                return 8;
            case 'd':
                return 10;
        }
        return 0;
    }

    public static char intToChar(int[] arr, int i) {
        switch (arr[i]) {
            case 0:
                return 'H';
            case 1:
                return 'e';
            case 2:
            case 3:
            case 9:
                return 'l';
            case 4:
            case 7:
                return 'o';
            case 5:
                return ' ';
            case 6:
                return 'W';
            case 8:
                return 'r';
            case 10:
                return 'd';
        }
        return 0;
    }
}
