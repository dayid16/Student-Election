from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
import sys

class Window(QWidget):
    '''
    Main window class that'll build all the UI screens for the student election app
    '''

    def __init__(self) -> None:
        '''
        Initialization function and display login screen
        '''

        super().__init__()
        self.setWindowTitle("Final Project 1")
        self.setFixedSize(300, 350)
        self._build_login_ui()

    def _build_login_ui(self) -> None:
        '''
        Builds the login screen UI. It contains a username input box and an error message label
        '''

        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.setContentsMargins(20, 20, 20, 20)

        # Student Election title
        se_title = QLabel("Student Election")
        se_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        se_title.setStyleSheet("font-size: 30px; font-weight: bold;")
        layout.addWidget(se_title)

        # Enter Username title
        user_title = QLabel(f"Enter Your\nUsername (Letters only)")
        user_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        user_title.setStyleSheet("font-size: 25px")
        layout.addWidget(user_title)

        # Enter Username text box
        layout.addSpacing(20)
        self.input_username = QLineEdit()
        self.input_username.setPlaceholderText("e.g. username")
        self.input_username.setStyleSheet("font-size: 15px; padding: 5px;")
        self.input_username.setFixedHeight(40)
        layout.addWidget(self.input_username)

        # Login Error Message
        self.login_error = QLabel("")
        self.login_error.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.login_error.setStyleSheet("color: red; font-size: 15px")
        layout.addWidget(self.login_error)


    def _build_vote_ui(self) -> None:
        '''
        Builds the voting screen UI. It contains radio buttons for each candidate and a submit button.
        '''
        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        # Candidates Title
        candidate_title = QLabel("Candidates")
        candidate_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        candidate_title.setStyleSheet("font-size: 30px; padding: 5px;")
        layout.addWidget(candidate_title)

        # Candidate Radio Buttons
        self.radio_isabella = QRadioButton("Isabella")
        self.radio_genji = QRadioButton("Genji")
        self.radio_hannah = QRadioButton("Hannah")

        for radio in [self.radio_isabella, self.radio_genji, self.radio_hannah]:
            radio.setStyleSheet("font-size: 20px")
            radio.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
            radio.setFixedWidth(130)
            row = QHBoxLayout()
            row.setAlignment(Qt.AlignmentFlag.AlignLeft)
            row.addWidget(radio)
            layout.addLayout(row)

        # Submit Button
        self.submit_button = QPushButton("Submit")
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.submit_button.setStyleSheet("font-size: 15px; padding: 5px;")
        self.submit_button.setFixedSize(220, 60)
        layout.addWidget(self.submit_button)

        # Vote Error Message
        self.vote_error = QLabel("")
        self.vote_error.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.vote_error.setStyleSheet("color: red; font-size: 15px")
        layout.addWidget(self.vote_error)

    def _build_results_ui(self) -> None:
        '''
        Builds the results screen UI. It contains a home button to the login screen, has a
        progress bar, and a votes counter to show who is winning the election.
        '''
        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        # Results Title
        result_title = QLabel("Current Results")
        result_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        result_title.setStyleSheet("font-size: 30px; padding: 5px;")
        layout.addWidget(result_title)

        # Isabella Votes and Progress Bar
        row = QHBoxLayout()
        self.isabella_label = QLabel("Isabella")
        self.isabella_label.setStyleSheet("font-size: 15px; padding: 5px;")
        self.isabella_votes = QLabel("")
        self.isabella_votes.setStyleSheet("font-size: 15px;")
        row.addWidget(self.isabella_label)
        row.addStretch()
        row.addWidget(self.isabella_votes)
        layout.addLayout(row)

        self.bar_isabella = QProgressBar()
        self.bar_isabella.setMaximum(100)
        self.bar_isabella.setValue(10)
        self.bar_isabella.setTextVisible(False)
        self.bar_isabella.setFixedHeight(10)
        layout.addWidget(self.bar_isabella)

        # Genji Votes and Progress Bar
        row = QHBoxLayout()
        self.genji_label = QLabel("Genji")
        self.genji_label.setStyleSheet("font-size: 15px; padding: 5px;")
        self.genji_votes = QLabel("")
        self.genji_votes.setStyleSheet("font-size: 15px;")
        row.addWidget(self.genji_label)
        row.addStretch()
        row.addWidget(self.genji_votes)
        layout.addLayout(row)

        self.bar_genji = QProgressBar()
        self.bar_genji.setMaximum(100)
        self.bar_genji.setValue(40)
        self.bar_genji.setTextVisible(False)
        self.bar_genji.setFixedHeight(10)
        layout.addWidget(self.bar_genji)

        # Hannah Votes and Progress Bar
        row = QHBoxLayout()
        self.hannah_label = QLabel("Hannah")
        self.hannah_label.setStyleSheet("font-size: 15px; padding: 5px;")
        self.hannah_votes = QLabel("")
        self.hannah_votes.setStyleSheet("font-size: 15px;")
        row.addWidget(self.hannah_label)
        row.addStretch()
        row.addWidget(self.hannah_votes)
        layout.addLayout(row)

        self.bar_hannah = QProgressBar()
        self.bar_hannah.setMaximum(100)
        self.bar_hannah.setValue(50)
        self.bar_hannah.setTextVisible(False)
        self.bar_hannah.setFixedHeight(10)
        layout.addWidget(self.bar_hannah)

        # Home Button
        self.home_button = QPushButton("Home")
        self.home_button.setStyleSheet("font-size: 15px; padding: 5px;")
        self.home_button.setFixedSize(100, 60)
        layout.addWidget(self.home_button, alignment=Qt.AlignmentFlag.AlignCenter)