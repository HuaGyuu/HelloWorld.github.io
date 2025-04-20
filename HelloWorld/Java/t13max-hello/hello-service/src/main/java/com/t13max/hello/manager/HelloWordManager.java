package com.t13max.hello.manager;

import com.t13max.hello.log.Log;

/**
 * hello word 管理器
 *
 * @Author: t13max
 * @Since: 8:14 2025/4/20
 */
public class HelloWordManager extends ManagerBase {

    /**
     * 获取实例
     *
     * @Author: t13max
     * @Since: 8:16 2025/4/20
     */
    public static HelloWordManager inst() {
        return inst(HelloWordManager.class);
    }

    @Override
    protected void onShutdown() {
        Log.HELLO.info("HelloWordManager onShutdown!!!");
    }

    @Override
    protected void init() {
        Log.HELLO.info("HelloWordManager init!!!");
    }

    public void printHelloWord() {
        Log.HELLO.info("Hello Word!!!");
    }
}
