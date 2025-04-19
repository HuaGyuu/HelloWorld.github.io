# C++/Qt版本的HelloWorld

#### 推荐运行所需环境：

​	>=**Qt**5.15

​	>=**MSVC**2015 64bit(32bit) （**Qt**跨平台的，**Linux**的**gcc**也是可以滴）

​	>=**CMake** 3.10

---

#### 推荐编译IDE：QtCreator，VisualStudio，VisualStudioCode

（备注：其他IDE也是可以滴，这三个相对简单些）

---

#### 编译及运行过程：

在此文件同级目录下创建 **build** 文件夹

```shell
cmake ..
```

如果是**mingw/gcc**的是**makefile**，在**build**文件夹内运行 **make** 即可

如果是**MSVC**，build文件夹内会生成**sln**项目文件，可以跑去**visualstudio**打开编译运行（编译产生**exe**）

**visual studio code**的**cmake tools**插件可以直接选**build tools**，可以直接编译后运行

---

#### USE_WINDOW （CACHE）变量：

**CMake**中更改**USE_WINDOW**的值可以改变**HelloWorld**的输出方式，默认为**On**即弹窗，**Off**为控制台输出