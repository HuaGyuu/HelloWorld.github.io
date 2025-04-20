package com.t13max.hello;

import com.t13max.hello.config.HelloConfig;
import com.t13max.hello.manager.HelloWordManager;
import com.t13max.hello.run.Application;
import com.t13max.hello.run.ConfigClazz;
import org.yaml.snakeyaml.Yaml;


/**
 * @Author: t13max
 * @Since: 8:10 2025/4/20
 */
@ConfigClazz(configClazz = HelloConfig.class)
public class AppMainHello {

    public static void main(String[] args) throws Exception{

        Application.run(AppMainHello.class, args);

        HelloWordManager.inst().printHelloWord();

    }
}
