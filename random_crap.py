from PyQt6.QtWidgets import QMenu, QAction

class AccountButton(QWidget):
    def __init__(self, user_data, width, height, radius, image_path='images/default.png', parent=None):
        super().__init__(parent)
        
        self.setFixedSize(width, height)
        
        # Initializing user data and labels
        self.account_name = f"{user_data['riot_id']} # {user_data['tagline']}"
        self.username = user_data['username']
        self.password = user_data['password']
        self.riot_id = user_data['riot_id']
        self.tagline = user_data['tagline']
        self.region = user_data['region']

        self.winrate = None
        self.rank = None

        api_key = os.getenv('riot_api_key')
        if not api_key:
            pass

        ranked_info = get_data(self.riot_id, self.tagline, self.region, api_key)

        if ranked_info:
            if None not in ranked_info:
                (rank, self.rank), self.winrate = ranked_info

                rank = rank.capitalize()
                if rank in RANKS:
                    image_path = RANKS[rank]

        # Load rounded image
        self.bg_pixmap = create_rounded_image(image_path, (width, height), radius)

        # Background Label (Image)
        self.bg_label = QLabel(self)
        self.bg_label.setPixmap(self.bg_pixmap)
        self.bg_label.setScaledContents(True)
        self.bg_label.setGeometry(0, 0, width, height)

        # Account Name
        self.account_label = QLabel(self.account_name, self)
        self.account_label.setFont(QFont("Arial", 14))
        self.account_label.setStyleSheet("color: gray; background: transparent;")
        self.account_label.setGeometry(10, 15, 250, 20)

        # Winrate (Centered)
        self.winrate_label = QLabel(self.winrate, self)
        self.winrate_label.setFont(QFont("Arial", 8))
        self.winrate_label.setStyleSheet("color: gray; background: transparent;")
        self.winrate_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.winrate_label.setGeometry(260, 7, 140, 20)

        # Rank (Centered)
        self.rank_label = QLabel(self.rank, self)
        self.rank_label.setFont(QFont("Arial", 8))
        self.rank_label.setStyleSheet("color: gray; background: transparent;")
        self.rank_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.rank_label.setGeometry(260, 22, 140, 20)

        # Invisible Clickable Button
        self.button = QPushButton("", self)
        self.button.setGeometry(0, 0, width, height)
        self.button.setStyleSheet("background: transparent; border: none;")

        self.button.setStyleSheet(
            f"""
            QPushButton {{
                background: transparent;
                border-radius: {radius}px;
                border: none;
            }}
            QPushButton:hover {{
                background: rgba(150, 150, 150, 20);
            }}
            QPushButton:pressed {{
                background: rgba(150, 150, 150, 30);
            }}
            """
        )

        self.button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))  # Set cursor to hand
        self.button.clicked.connect(self.on_click)
        
        # Right-click context menu
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_context_menu)

    def enterEvent(self, event):
        """ Change account label color to white on hover """
        self.account_label.setStyleSheet("color: #A5A2A3; background: transparent;")
        self.winrate_label.setStyleSheet("color: #A5A2A3; background: transparent;")
        self.rank_label.setStyleSheet("color: #A5A2A3; background: transparent;")

    def leaveEvent(self, event):
        """ Change account label color back to gray when not hovered """
        self.account_label.setStyleSheet("color: gray; background: transparent;")
        self.winrate_label.setStyleSheet("color: gray; background: transparent;")
        self.rank_label.setStyleSheet("color: gray; background: transparent;")

    def on_click(self):
        print(f"Username: {self.username}, Password: {self.password}")
    
    def show_context_menu(self, pos):
        """ Show right-click context menu to edit the account """
        context_menu = QMenu(self)
        edit_action = QAction("Edit Account", self)
        context_menu.addAction(edit_action)
        edit_action.triggered.connect(self.edit_account)

        # Execute the context menu
        context_menu.exec(self.mapToGlobal(pos))

    def edit_account(self):
        """ Show input fields with current data to edit the account """
        # Create a form to edit account data, similar to the CreateAccount form
        self.parent().edit_account(self)


class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        load_dotenv()

        self.setWindowTitle("Riot Logger")
        self.setWindowIcon(QIcon(os.path.abspath("images/icon.ico")))

        self.setGeometry(100, 100, 442, 405)  # x, y, w, h

        # Set background color
        self.setStyleSheet("background-color: #242424; color: white;")

        layout = QVBoxLayout(self)

        # Button sizes
        width = 400
        height = 50
        radius = 15

        # Create a scrollable area for the account buttons
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        # Hide the scrollbar
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        scroll_content = QWidget(scroll_area)
        scroll_layout = QVBoxLayout(scroll_content)
        scroll_area.setWidget(scroll_content)

        # Add account buttons to scrollable area
        max_accounts_visible = 6
        create_account_count = max_accounts_visible - len(users)

        for user in users:
            scroll_layout.addWidget(AccountButton(user, width, height, radius))

        # Add Create Account button
        for i in range(create_account_count):
            create_account_widget = CreateAccount(width, height, radius, scroll_area)
            scroll_layout.addWidget(create_account_widget)

        if create_account_count <= 1:
            create_account_widget = CreateAccount(width, height, radius, scroll_area)
            scroll_layout.addWidget(create_account_widget)

        # Add the scroll area to the main layout
        layout.addWidget(scroll_area)

        self.setLayout(layout)

    def edit_account(self, account_button):
        """ Display the editing form with the current account data """
        riot_id = account_button.riot_id
        tagline = account_button.tagline
        username = account_button.username
        password = account_button.password
        region = account_button.region

        # Open the CreateAccount form and pre-fill the data
        create_account_widget = CreateAccount(self.width(), self.height(), 15, self)
        create_account_widget.riot_id_entry.setText(riot_id)
        create_account_widget.tagline_entry.setText(tagline)
        create_account_widget.username_entry.setText(username)
        create_account_widget.password_entry.setText(password)
        create_account_widget.combo_box.setCurrentText(region)

        # Update the data once confirmed
        create_account_widget.confirm_button.clicked.connect(
            lambda: self.update_account(account_button, create_account_widget)
        )

    def update_account(self, account_button, create_account_widget):
        """ Update the account button with the new data """
        riot_id = create_account_widget.riot_id_entry.text()
        tagline = create_account_widget.tagline_entry.text()
        username = create_account_widget.username_entry.text()
        password = create_account_widget.password_entry.text()
        region = create_account_widget.combo_box.currentText()

        account_button.account_name = f"{riot_id} # {tagline}"
        account_button.username = username
        account_button.password = password
        account_button.riot_id = riot_id
        account_button.tagline = tagline
        account_button.region = region

        # Recalculate rank and winrate
        ranked_info = get_data(riot_id, tagline, region, os.getenv('riot_api_key'))
        if ranked_info:
            if None not in ranked_info:
                (rank, account_button.rank), account_button.winrate = ranked_info

        # Update the button display
        account_button.account_label.setText(account_button.account_name)
        account_button.winrate_label.setText(account_button.winrate)
        account_button.rank_label.setText(account_button.rank)

        # Hide the edit form
        create_account_widget.reset_form()

