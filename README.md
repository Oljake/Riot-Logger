# Riot Logger App

This application allows users to manage their Riot game account credentials through a simple UI. When you launch the app, it automatically opens League of Legends (LoL) and the application interface. In the app, you can input your account details, and the app will generate buttons for each account. By clicking a button, the app logs you into the selected Riot account. The account data is then saved into a file, allowing you to access and manage your information across sessions.

Important Risks and Considerations:
---------------------------------------

- **Sensitive Data**:  
  The `users_data.pickle` file contains sensitive account data (e.g., usernames, passwords). Be careful when sharing this file, as doing so grants others access to your accounts.

- **Rate Limiting**:  
  Riot enforces rate limits on the API. Excessive requests may result in temporary access throttling or a block on the API, but won’t affect in-game bans.

- **Non-Existing Accounts**:  
  Querying non-existing accounts will return errors but generally won't result in direct consequences. However, excessive misuse (like repeatedly querying invalid accounts) could lead to restrictions on your API access.

- **Terms of Service**:  
  Misusing the API (e.g., storing or sharing data improperly) could violate Riot’s terms and result in API access restrictions. Always use the API responsibly to avoid issues.


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
