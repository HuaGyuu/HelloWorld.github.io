public class HelloWorld06 {
    public static void main(String[] args) {
        // new 一个对象
        Hello hello = new Hello("Hello World");

        // 创建写线程 t1
        Thread t1 = new Thread(() -> {
            hello.write();
        });

        // 创建写线程 t2
        Thread t2 = new Thread(() -> {
            hello.write();
        });

        // 创建读线程 t3
        Thread t3 = new Thread(() -> {
            hello.read();
        });

        // 启动线程
        t1.start();
        t2.start();
        t3.start();

    }
}

class Hello {
    // 最终结果
    private volatile String hello;
    // 计数器
    private volatile int counter;
    // 目标字符串
    private volatile String s1;
    // 结果字符串
    private volatile String s2;

    public Hello(String s) {
        this.s1 = s;
        s2 = "";
        counter = 0;
    }

    public void write() {
        // 获取字符串的长度
        int length = s1.length();

        // 循环添加字符
        while (counter < length) {
            // 同步代码块，保证线程安全
            synchronized (this) {
                // 再次判断条件 ，避免 counter 多加
                if (counter < length) {
                    s2 += s1.charAt(counter++);
                }
            }
        }

        synchronized (this) {
            // 赋值给最终结果
            hello = s2;
            this.notifyAll();
        }

    }

    public void read() {
        synchronized (this) {
            while (hello == null) {
                try {
                    // 没有结果就等待
                    this.wait();
                } catch (InterruptedException e) {
                    throw new RuntimeException(e);
                }
            }
        }

        System.out.println(hello);
    }
}
