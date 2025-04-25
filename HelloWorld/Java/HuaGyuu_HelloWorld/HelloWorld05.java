public class HelloWorld05 {
    public static void main(String[] args) throws InterruptedException {
        // new 一个对象调用方法
        new Hello().hello();
    }
}

class Hello {
    // 没用的东西
    private String hello;
    private String world;
    // 有用的东西
    private int index = 0;
    private char[] arr = new char[11];

    public void hello() throws InterruptedException {
        // 没到最后就一直循环
        while (index < 11) {
            // 从 a 开始
            char ch = 'a';
            while (true) {
                // 空格特殊对待
                if (index == 5) {
                    arr[index] = ' ';
                    break;
                }
                arr[index] = ch++;
                // 不停输出数组
                for (int i = 0; i <= index; i++) {
                    System.out.print(arr[i]);
                }
                System.out.println();
                Thread.sleep(200);
                // 到相应的位终止
                if ("hello world".charAt(index) == ch - 1) break;
            }
            index++;
        }
    }
}
