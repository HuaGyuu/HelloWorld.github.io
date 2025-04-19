#ifndef HELLOWORLDWINDOW_H
#define HELLOWORLDWINDOW_H

#include <QWidget>
#include <QObject>

class QLabel;
class HelloWorldWindow : public QWidget
{
    Q_OBJECT
public:
    explicit HelloWorldWindow(QWidget *parent = nullptr);
    Q_INVOKABLE void setUp();

private:
    QLabel* label{nullptr};
};

#endif // HELLOWORLDWINDOW_H
