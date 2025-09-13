import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.layout.BorderPane;
import javafx.stage.Stage;

/**
 * @Author: HuaGyuu
 * @CreateTime: 2025-09-13
 * @Version: 1.0
 */
public class HelloWorld extends Application {
    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage stage) throws Exception {
        // 创建一个标签
        Label label = new Label("Hello World!");
        // 创建布局
        BorderPane pane = new BorderPane(label);
        // 创建场景
        Scene scene = new Scene(pane, 300, 300);
        // 将场景设置到窗口里
        stage.setScene(scene);
        // 设置标题
        stage.setTitle("Hello World");
        // 显示窗口
        stage.show();
    }
}
