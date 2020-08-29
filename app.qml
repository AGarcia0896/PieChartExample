import Charts 1.0
import QtQuick 2.13
import QtQuick.Window 2.13

Window {
    title: "Python - QML"
    width: 640
    height: 480
    visible: true

    Item {
        width: 300
        height: 200

        PieChart {
            id: chartA
            width: 100
            height: 100
            color: "red"
            anchors.centerIn: parent
        }

        MouseArea {
            anchors.fill: parent
            onClicked: { chartA.color = "blue" }
        }

        Text {
            anchors {
                bottom: parent.bottom
                horizontalCenter: parent.horizontalCenter
                bottomMargin: 20
            }
            text: "Click anywhere to change the chart color"
        }
    }
}
