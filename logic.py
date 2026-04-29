from gui import *
import csv

class Logic(Window):
    '''
    This class will handle all logic for the student election app.
    '''
    def __init__(self) -> None:
        '''
        Initialization function for the Logic class. ALso connects the username input
        to handle_login
        '''
        super().__init__()
        self.input_username.returnPressed.connect(self.handle_login)

    def switch_screen(self, build_method) -> None:
        '''
        Clears the screen and changes it into a new one depending on the action.
        '''

        old_layout = self.layout()
        if old_layout is not None:
            while self.layout().count():
                item = self.layout().takeAt(0)
                if item.widget():
                     item.widget().deleteLater()
                elif item.layout():
                    while item.layout().count():
                        sub_item = item.layout().takeAt(0)
                        if sub_item.widget():
                            sub_item.widget().deleteLater()
            QWidget().setLayout(old_layout)
        build_method()

        if build_method == self._build_vote_ui:
            self.submit_button.clicked.connect(self.handle_vote)

        if build_method == self._build_results_ui:
            self.home_button.clicked.connect(self.handle_home)
            self.update_results()

        if build_method == self._build_login_ui:
            self.input_username.returnPressed.connect(self.handle_login)

    def handle_login(self) -> None:
        '''
        Handles the logic of the login screen.
        It'll validate the username by checking if it has any symbols or numbers and checking if the username is already in the system.
        If one of these errors are met, then an error message will appear.
        Once a valid username is entered, it will go onto the vote screen.
        '''
        username = self.input_username.text().lower()

        if not username.strip().isalpha():
            self.login_error.setText(f"Please enter a valid\nusername (Letters only)")
        else:
            with open("usernames.csv", "r") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row["username"].strip() == username.strip():
                        if row["voted"].strip() == "True":
                            self.login_error.setText(f"You have already voted!")
                        else:
                            self.current_user = username
                            self.switch_screen(self._build_vote_ui)
                        break
                else:
                    with open("usernames.csv", "a") as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow([username, "False"])
                    self.current_user = username
                    self.switch_screen(self._build_vote_ui)

    def handle_vote(self) -> None:
        '''
        Handles the logic of the vote screen.
        It will process the selection the user selects when a radio button is selected and the Submit button is pressed.
        This function also updates the CSV file
        Once a selection is made, it will then go onto the results screen.
        If a candidate is not selected, an error message appears.
        '''

        candidates = {
            "Isabella": self.radio_isabella,
            "Genji": self.radio_genji,
            "Hannah": self.radio_hannah,
        }

        selected = None
        for candidate, radio in candidates.items():
            if radio.isChecked():
                selected = candidate
                break

        if selected is None:
            self.vote_error.setText(f"Please select\na candidate!")
            return

        rows = []
        with open("votes.csv", "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["candidate"] == selected:
                    row["votes"] = int(row["votes"]) + 1
                rows.append(row)

        with open("votes.csv", "w") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["candidate", "votes"])
            writer.writeheader()
            writer.writerows(rows)

        rows = []
        with open("usernames.csv", "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["username"] == self.current_user:
                    row["voted"] = "True"
                rows.append(row)

        with open("usernames.csv", "w") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["username", "voted"])
            writer.writeheader()
            writer.writerows(rows)

        self.switch_screen(self._build_results_ui)

    def handle_home(self) -> None:
        '''
        Goes back to the home screen once pressed while on the results page.
        '''
        self.switch_screen(self._build_login_ui)

    def update_results(self) -> None:
        '''
        Handles the logic of the results screen.
        This function reads the votes.csv file and update the progress bar and votes count with the correct votes.
        '''
        with open("votes.csv", "r") as csvfile:
            reader = csv.DictReader(csvfile)
            rows = list(reader)

        total_votes = sum(int(row["votes"]) for row in rows)
        if total_votes == 0:
            total_votes = 1

        for row in rows:
            votes = int(row["votes"])

            if row["candidate"] == 'Isabella':
                self.isabella_votes.setText(f"{votes} Votes")
                self.bar_isabella.setMaximum(total_votes)
                self.bar_isabella.setValue(votes)
            elif row["candidate"] == 'Genji':
                self.genji_votes.setText(f"{votes} Votes")
                self.bar_genji.setMaximum(total_votes)
                self.bar_genji.setValue(votes)
            elif row["candidate"] == 'Hannah':
                self.hannah_votes.setText(f"{votes} Votes")
                self.bar_hannah.setMaximum(total_votes)
                self.bar_hannah.setValue(votes)

