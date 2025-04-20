package com.t13max.hello.log;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

/**
 * @Author: t13max
 * @Since: 8:06 2025/4/20
 */
public class Log {

    public static Logger MANAGER = LogManager.getLogger("MANAGER");
    public static Logger APP = LogManager.getLogger("APP");
    public static Logger HELLO = LogManager.getLogger("HELLO");
}
