# Riot Logger App




Description:
---------------------------------------
This application allows users to manage their Riot game account credentials.
It features a simple UI where users can add, view, and manage their accounts,
as well as configure the API key used to fetch account information.

Main Features:
---------------------------------------
- **Add Account**: Easily add a Riot account by providing a Riot ID, Tagline, 
  Username, Password, and Region.
  
- **Account Management**: View stored accounts and their respective winrates 
  and ranks.
  
- **Change API Key**: Update the API key used for fetching account data.
  
- **Resizable Form**: Create and manage accounts in a resizable and intuitive form.
  
- **Account Info Display**: Each account displays the account name, winrate, 
  rank, and other details.

File Storage:
---------------------------------------
- The user data is saved to a file using `pickle` in the format `users_data.pickle`.
  
- The app supports saving and loading account information between sessions.

Setup Instructions:
---------------------------------------
1. Ensure you have Python 3.x installed on your machine.
2. Install necessary dependencies:
    - PyQt6
    - Pillow
    - dotenv
3. Place your API key in a `.env` file using the variable `riot_api_key`.
4. Run the app using:
    `python main.py`

How to use:
---------------------------------------
1. Launch the app.
2. Click on "Create Account" to add a new account.
3. Enter Riot ID, Tagline, Username, Password, and Region.
4. View and manage accounts in the list.
5. Optionally, change the API key for new data.

File Locations:
---------------------------------------
- Account data is stored in the `users_data.pickle` file.
- Images are stored in the `images/` directory.

Author:
---------------------------------------
- Oljake
