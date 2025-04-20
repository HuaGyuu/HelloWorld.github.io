package com.t13max.hello.manager;




import com.t13max.hello.config.BaseConfig;
import com.t13max.hello.config.SundryKey;
import com.t13max.hello.dag.DAG;
import com.t13max.hello.dag.DAGNode;
import com.t13max.hello.exception.HelloException;
import com.t13max.hello.log.Log;
import com.t13max.hello.run.Application;
import com.t13max.hello.utils.PackageUtil;

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Modifier;
import java.util.Collections;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.concurrent.ConcurrentHashMap;

/**
 * manger基类
 *
 * @author: t13max
 * @since: 14:09 2024/5/23
 */
public abstract class ManagerBase implements Comparable<ManagerBase> {

    //缓存所有manager
    public static volatile Map<String, ManagerBase> instances = new ConcurrentHashMap<>();

    // manager依赖图
    private static final DAG<ManagerBase> dag = new DAG<>();

    static {
        initialize();
    }

    protected static <T extends ManagerBase> T inst(Class<T> clazz) {
        Object inst = instances.get(clazz.getName());
        if (inst == null) {
            throw new HelloException("获取Manager实例时出错：未能找到对应实例，class=" + clazz.getSimpleName());
        }

        return (T) inst;
    }

    /**
     * 自动扫描com.t13max包下的manager并初始化
     *
     * @Author: t13max
     * @Since: 22:34 2024/7/19
     */
    private static void initialize() {

        instances.clear();

        ClassLoader classLoader = null;
        BaseConfig config = Application.config();
        if (config != null) {
            classLoader = (ClassLoader) config.getSundryMap().get(SundryKey.PACK_CLASS_LOADER);
        }

        Set<Class<?>> classSet = PackageUtil.scan("com.t13max", classLoader);

        //创建实例
        initialize(classSet);
    }

    /**
     * 初始化指定类的manager
     * 不是manager自动跳过
     *
     * @Author: t13max
     * @Since: 22:35 2024/7/19
     */
    private static void initialize(Set<Class<?>> classSet) {

        try {

            for (Class<?> clazz : classSet) {
                // 只需要加载ManagerClass注解数据
                if (!ManagerBase.class.isAssignableFrom(clazz) || Modifier.isAbstract(clazz.getModifiers())) {
                    continue;
                }

                // 创建实例
                Object inst = clazz.getDeclaredConstructor().newInstance();
                ManagerBase managerBase = (ManagerBase) inst;
                instances.put(clazz.getName(), managerBase);
            }

            //创建DAGNode
            for (ManagerBase managerBase : instances.values()) {
                final DAGNode<ManagerBase> dg = dag.createNodeIfNotExist(managerBase);
                if (!managerBase.getDependents().isEmpty()) {
                    for (final Class<? extends ManagerBase> key : managerBase.getDependents()) {
                        dg.addPrev(instances.get(key.getName()));
                    }
                }
            }
        } catch (InstantiationException | IllegalAccessException | NoSuchMethodException |
                 InvocationTargetException e) {
            throw new HelloException(e);
        }
    }

    /**
     * 初始化所有的manager
     */
    public static void initAllManagers() {

        dag.walk(n -> {
            ManagerBase managerBase = n.getObj();
            try {
                // 初始化
                managerBase.init();
                Log.MANAGER.debug("模块{}初始化完成.", managerBase.getClass().getName());
            } catch (final Exception ex) {
                Log.MANAGER.error(String.format("模块%s启动失败", managerBase.getClass().getName()), ex);
                throw new HelloException(ex);
            }
        });
    }

    /**
     * 关服
     */
    public static void shutdown() {
        dag.walk(n -> {
            ManagerBase manager = n.getObj();
            try {
                manager.onShutdown();
            } catch (Exception e) {
                Log.MANAGER.info("Manager: {} shutdown failed, error: {}", manager.getClass().getCanonicalName(), e);
            }
        });
    }

    /**
     * 关服时的处理
     */
    protected void onShutdown() {

    }

    /**
     * 返回当前Manager依赖的其他Manger类名
     */
    public List<Class<? extends ManagerBase>> getDependents() {
        return Collections.emptyList();
    }

    protected void init() {

    }

    @Override
    public int compareTo(ManagerBase o) {
        return this.getClass().getName().compareTo(o.getClass().getName());
    }
}
