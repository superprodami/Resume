import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout,
    QFileDialog, QComboBox, QLineEdit, QMessageBox, QHBoxLayout
)

import main_script  # 假设你把原来的脚本保存为 main_script.py


class StreamConverterUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("直存码流转PS工具")
        self.resize(500, 300)

        layout = QVBoxLayout()

        # 文件选择
        self.file_label = QLabel("选择文件:")
        self.file_path = QLineEdit()
        self.file_btn = QPushButton("浏览")
        self.file_btn.clicked.connect(self.choose_file)
        file_layout = QHBoxLayout()
        file_layout.addWidget(self.file_label)
        file_layout.addWidget(self.file_path)
        file_layout.addWidget(self.file_btn)

        # system_format 下拉
        self.system_format = QComboBox()
        self.system_format.addItems([
            "0x0: RAW", "0x1: HIK", "0x2: PS", "0x3: TS", "0x4: RTP",
            "0x5: MP4_BACK", "0x6: ASF", "0x7: AVI", "0x8: GB_PS",
            "0x9: HLS_TS", "0xa: FLV", "0xb: MP4_FRONT", "0xc: MP4_FRAG",
            "0xd: RTMP", "0xe: MP4_PRE_INDEX", "0x8001: DHAV"
        ])

        # video_format 下拉
        self.video_format = QComboBox()
        self.video_format.addItems([
            "0x0001: HIK264", "0x0002: MPEG2", "0x0003: MPEG4", "0x0004: MJPEG",
            "0x0005: H265", "0x0006: SVAC", "0x0100: H264", "0x0110: SVC264"
        ])

        # audio_format 下拉
        self.audio_format = QComboBox()
        self.audio_format.addItems([
            "0x1000: ADPCM", "0x2000: MPEG", "0x2001: AAC", "0x2002: AAC_LD",
            "0x3002: OPUS", "0x7110: G711U", "0x7111: G711A", "0x7001: PCM",
            "0x7221: G7221", "0x7231: G7231", "0x7261: G726A", "0x7260: G726_32",
            "0x7262: G726_16", "0x7290: G729", "0x0000: None"
        ])

        # 其他参数输入
        self.audio_chan = QLineEdit("1")  # 默认单声道
        self.audio_sr = QLineEdit("8000")  # 默认采样率
        self.audio_bps = QLineEdit("16000")  # 默认位样率

        # 转换按钮
        self.start_btn = QPushButton("开始转换")
        self.start_btn.clicked.connect(self.start_convert)

        layout.addLayout(file_layout)
        layout.addWidget(QLabel("System Format:"))
        layout.addWidget(self.system_format)
        layout.addWidget(QLabel("Video Format:"))
        layout.addWidget(self.video_format)
        layout.addWidget(QLabel("Audio Format:"))
        layout.addWidget(self.audio_format)
        layout.addWidget(QLabel("音频通道 (1单声道, 2双声道):"))
        layout.addWidget(self.audio_chan)
        layout.addWidget(QLabel("音频采样率:"))
        layout.addWidget(self.audio_sr)
        layout.addWidget(QLabel("音频位样率:"))
        layout.addWidget(self.audio_bps)
        layout.addWidget(self.start_btn)

        self.setLayout(layout)

    def choose_file(self):
        file, _ = QFileDialog.getOpenFileName(self, "选择文件", "", "All Files (*)")
        if file:
            self.file_path.setText(file)

    def start_convert(self):
        filename = self.file_path.text()
        if not filename or not os.path.exists(filename):
            QMessageBox.critical(self, "错误", "请选择有效的文件")
            return

        args = [
            "",  # 占位（sys.argv[0]）
            filename,
            self.system_format.currentText().split(":")[0],
            self.video_format.currentText().split(":")[0],
            self.audio_format.currentText().split(":")[0],
            self.audio_chan.text(),
            self.audio_sr.text(),
            self.audio_bps.text()
        ]

        try:
            main_script.parse_direct_stream(args)
            QMessageBox.information(self, "成功", f"转换完成: {filename}.dump")
        except Exception as e:
            QMessageBox.critical(self, "错误", str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StreamConverterUI()
    window.show()
    sys.exit(app.exec_())
