# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'glue/qt/ui/histogramwidget.ui'
#
# Created: Wed Jul 31 15:07:24 2013
#      by: pyside-uic 0.2.13 running on glue.external.qt 1.1.0
#
# WARNING! All changes made in this file will be lost!

from glue.external.qt import QtCore, QtGui

class Ui_HistogramWidget(object):
    def setupUi(self, HistogramWidget):
        HistogramWidget.setObjectName("HistogramWidget")
        HistogramWidget.resize(240, 207)
        HistogramWidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        HistogramWidget.setStyleSheet("")
        self.horizontalLayout_6 = QtGui.QHBoxLayout(HistogramWidget)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(-1, -1, -1, 10)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.option_dashboard = QtGui.QWidget(HistogramWidget)
        self.option_dashboard.setObjectName("option_dashboard")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.option_dashboard)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.combo_layout = QtGui.QHBoxLayout()
        self.combo_layout.setSpacing(1)
        self.combo_layout.setObjectName("combo_layout")
        self.attribute_layout = QtGui.QVBoxLayout()
        self.attribute_layout.setSpacing(1)
        self.attribute_layout.setObjectName("attribute_layout")
        self.label_4 = QtGui.QLabel(self.option_dashboard)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.attribute_layout.addWidget(self.label_4)
        self.attributeCombo = QtGui.QComboBox(self.option_dashboard)
        self.attributeCombo.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToMinimumContentsLength)
        self.attributeCombo.setObjectName("attributeCombo")
        self.attribute_layout.addWidget(self.attributeCombo)
        self.combo_layout.addLayout(self.attribute_layout)
        self.verticalLayout_3.addLayout(self.combo_layout)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.binSpinBox = QtGui.QDoubleSpinBox(self.option_dashboard)
        self.binSpinBox.setKeyboardTracking(False)
        self.binSpinBox.setDecimals(0)
        self.binSpinBox.setMinimum(1.0)
        self.binSpinBox.setMaximum(100000.0)
        self.binSpinBox.setSingleStep(3.0)
        self.binSpinBox.setProperty("value", 10.0)
        self.binSpinBox.setObjectName("binSpinBox")
        self.horizontalLayout_5.addWidget(self.binSpinBox)
        self.label = QtGui.QLabel(self.option_dashboard)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 2, -1, 2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtGui.QLabel(self.option_dashboard)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.xmin = QtGui.QLineEdit(self.option_dashboard)
        self.xmin.setMaxLength(18)
        self.xmin.setObjectName("xmin")
        self.horizontalLayout_3.addWidget(self.xmin)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtGui.QLabel(self.option_dashboard)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.xmax = QtGui.QLineEdit(self.option_dashboard)
        self.xmax.setMaxLength(18)
        self.xmax.setObjectName("xmax")
        self.horizontalLayout_2.addWidget(self.xmax)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.normalized_box = QtGui.QCheckBox(self.option_dashboard)
        self.normalized_box.setObjectName("normalized_box")
        self.verticalLayout.addWidget(self.normalized_box)
        self.autoscale_box = QtGui.QCheckBox(self.option_dashboard)
        self.autoscale_box.setChecked(True)
        self.autoscale_box.setObjectName("autoscale_box")
        self.verticalLayout.addWidget(self.autoscale_box)
        self.cumulative_box = QtGui.QCheckBox(self.option_dashboard)
        self.cumulative_box.setObjectName("cumulative_box")
        self.verticalLayout.addWidget(self.cumulative_box)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.xlog_box = QtGui.QCheckBox(self.option_dashboard)
        self.xlog_box.setObjectName("xlog_box")
        self.verticalLayout_2.addWidget(self.xlog_box)
        self.ylog_box = QtGui.QCheckBox(self.option_dashboard)
        self.ylog_box.setObjectName("ylog_box")
        self.verticalLayout_2.addWidget(self.ylog_box)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_5.addWidget(self.option_dashboard)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)

        self.retranslateUi(HistogramWidget)
        QtCore.QMetaObject.connectSlotsByName(HistogramWidget)

    def retranslateUi(self, HistogramWidget):
        HistogramWidget.setWindowTitle(QtGui.QApplication.translate("HistogramWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("HistogramWidget", "Attribute", None, QtGui.QApplication.UnicodeUTF8))
        self.attributeCombo.setToolTip(QtGui.QApplication.translate("HistogramWidget", "Select an attribute", None, QtGui.QApplication.UnicodeUTF8))
        self.binSpinBox.setToolTip(QtGui.QApplication.translate("HistogramWidget", "Define the histogram bin width", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("HistogramWidget", "Number of bins", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("HistogramWidget", "Min", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("HistogramWidget", "Max", None, QtGui.QApplication.UnicodeUTF8))
        self.normalized_box.setText(QtGui.QApplication.translate("HistogramWidget", "Normalized", None, QtGui.QApplication.UnicodeUTF8))
        self.autoscale_box.setText(QtGui.QApplication.translate("HistogramWidget", "Autoscale y axis", None, QtGui.QApplication.UnicodeUTF8))
        self.cumulative_box.setText(QtGui.QApplication.translate("HistogramWidget", "Cumulative", None, QtGui.QApplication.UnicodeUTF8))
        self.xlog_box.setText(QtGui.QApplication.translate("HistogramWidget", "x log", None, QtGui.QApplication.UnicodeUTF8))
        self.ylog_box.setText(QtGui.QApplication.translate("HistogramWidget", "y log", None, QtGui.QApplication.UnicodeUTF8))

