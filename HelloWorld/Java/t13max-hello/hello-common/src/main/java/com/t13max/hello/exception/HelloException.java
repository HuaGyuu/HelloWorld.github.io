package com.t13max.hello.exception;

/**
 * @Author: t13max
 * @Since: 8:03 2025/4/20
 */
public class HelloException extends RuntimeException{

    public HelloException() {
    }

    public HelloException(String message) {
        super(message);
    }

    public HelloException(String message, Throwable cause) {
        super(message, cause);
    }

    public HelloException(Throwable cause) {
        super(cause);
    }

    public HelloException(String message, Throwable cause, boolean enableSuppression, boolean writableStackTrace) {
        super(message, cause, enableSuppression, writableStackTrace);
    }
}
