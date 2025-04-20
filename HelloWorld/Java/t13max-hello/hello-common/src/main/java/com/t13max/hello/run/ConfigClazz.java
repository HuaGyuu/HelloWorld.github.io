package com.t13max.hello.run;


import com.t13max.hello.config.BaseConfig;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

/**
 * 指定配置类的注解
 *
 * @Author t13max
 * @Date 18:15 2024/8/23
 */
@Target(ElementType.TYPE)
@Retention(RetentionPolicy.RUNTIME)
public @interface ConfigClazz {

    Class<? extends BaseConfig> configClazz();
}
