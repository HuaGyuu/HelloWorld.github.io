package com.t13max.hello.config;

import lombok.Data;

/**
 * @Author: t13max
 * @Since: 8:13 2025/4/20
 */
@Data
public class HelloConfig extends BaseConfig {

    private boolean test;

    private ActionConfig action = new ActionConfig();
}
