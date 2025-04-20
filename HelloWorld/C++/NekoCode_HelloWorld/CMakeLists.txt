cmake_minimum_required(VERSION 3.16)

project(NekoCode_HelloWorld LANGUAGES CXX)

set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(USE_WINDOW ON CACHE BOOL "'Hello World' with GUI")

find_package(QT NAMES Qt6 Qt5 REQUIRED COMPONENTS Core Gui)
find_package(Qt${QT_VERSION_MAJOR} REQUIRED COMPONENTS Core Gui Widgets)

add_executable(NekoCode_HelloWorld
  main.cpp
  helloworldwindow.cpp
  helloworldwindow.h
)

target_link_libraries(NekoCode_HelloWorld Qt${QT_VERSION_MAJOR}::Core Qt${QT_VERSION_MAJOR}::Gui Qt${QT_VERSION_MAJOR}::Widgets)

if(USE_WINDOW)
    target_compile_definitions(NekoCode_HelloWorld PRIVATE _HELLOWORLD_)
endif()

include(GNUInstallDirs)
install(TARGETS NekoCode_HelloWorld
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)
