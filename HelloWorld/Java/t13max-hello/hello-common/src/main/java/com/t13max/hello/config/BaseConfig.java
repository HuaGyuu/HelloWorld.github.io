package com.t13max.hello.config;


import com.t13max.hello.consts.CoreConst;
import com.t13max.hello.exception.HelloException;
import com.t13max.hello.run.Application;
import com.t13max.hello.run.ConfigClazz;
import lombok.AccessLevel;
import lombok.Getter;
import lombok.Setter;
import org.yaml.snakeyaml.Yaml;

import java.util.HashMap;
import java.util.Map;

/**
 * 配置基类
 *
 * @author: t13max
 * @since: 17:47 2024/5/23
 */
@Setter
@Getter
public class BaseConfig {

    //实例名 理论上全局唯一 实例功能+id
    private String instanceName;

    //业务名
    private String serviceName;

    //实例id
    private int instanceId;

    //配置类类型
    private Class<?> appConfig;

    private boolean print;

    //Sqlite数据文件
    private String dbFile;

    //netty设置
    //private final NettyConfig netty = new NettyConfig();

    //Action
    //private final ActionConfig action = new ActionConfig();

    //rpc配置
    //private RpcConfig rpc;

    //Redis相关配置
    //private RedisConfig redis = new RedisConfig();

    //数据库配置
    //private DataConfig dataConfig = new DataConfig();

    //杂项
    private final Map<String, Object> sundryMap = new HashMap<>();

    /**
     * 校验数据
     *
     * @Author t13max
     * @Date 18:59 2024/5/23
     */
    public boolean check() {
        return true;
    }

    /**
     * 加载配置文件
     * 包级别 禁止外部调用
     *
     * @Author t13max
     * @Date 17:58 2024/5/23
     */
    public static BaseConfig loadConfig(Class<?> clazz) {

        ConfigClazz annotation = clazz.getAnnotation(ConfigClazz.class);

        Class<? extends BaseConfig> configClazz = BaseConfig.class;
        if (annotation != null) {
            configClazz = annotation.configClazz();
        }

        Yaml yaml = new Yaml();

        BaseConfig config = yaml.loadAs(Application.class.getClassLoader().getResourceAsStream(CoreConst.CONFIG_NAME), configClazz);

        config.setAppConfig(configClazz);

        //校验配置
        if (!config.check()) {
            throw new HelloException("配置文件校验异常");
        }
        return config;
    }
}
