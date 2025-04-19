#include "helloworldwindow.h"
#include <QLabel>
#include <QLayout>
#include <QFont>

HelloWorldWindow::HelloWorldWindow(QWidget *parent)
    : QWidget{parent}
{
    this->setUp();
}

void HelloWorldWindow::setUp()
{
    QHBoxLayout* layout = new QHBoxLayout();

    label = new QLabel(this);
    label->setText("Hello World");
    label->setAlignment(Qt::AlignCenter);

    QFont font = label->font();
    font.setFamily("Segoe Print");
    font.setPointSize(35);
    font.setBold(true);

    label->setFont(font);

    this->setLayout(layout);
    this->setFixedSize(800,600);

    layout->addWidget(label);
}
