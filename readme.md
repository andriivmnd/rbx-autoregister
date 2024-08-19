# Roblox Account Registration Script

## Overview

This script was created to automate the registration of accounts in the Roblox game using Selenium. It was developed quickly to address a business need for mass account registration. The script automates the process of filling out the registration form on the Roblox website and creating new accounts.

## Requirements

- Python 3.6 or higher
- Selenium
- WebDriver for your chosen browser (e.g., ChromeDriver for Google Chrome)

## Installation

1. Install Python 3.6+ from the [official website](https://www.python.org/downloads/).
2. Install the required dependencies using pip:

    ```bash
    pip install selenium
    ```

3. Download and install the WebDriver for your browser. For example, for Google Chrome, download [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads). Ensure that the WebDriver version matches your browser version.

4. Place the WebDriver in your system's PATH or in the same directory as the script.

## Usage

1. Open the script in any text editor.
2. Set the necessary parameters, such as the number of accounts to register and unique data for each account (e.g., usernames, passwords, birth dates, etc.).
3. Run the script with the following command:

    ```bash
    python main.py
    ```

4. The script will automatically open a browser, fill out the registration form on the Roblox website, and create the specified accounts.

## Important Notes

- This script is designed for internal use and is not intended for mass use or to circumvent Roblox's terms of service.
- Roblox may block accounts registered using automated tools, so use this script at your own risk.
- Ensure that you are not violating Roblox's terms of service or any applicable laws in your country.

## Limitations

- The script was developed quickly and may contain bugs or unfinished features.
- There is no error handling or logging. If the registration process is interrupted, the script cannot resume from where it stopped.
- The script does not support CAPTCHA solving. If Roblox uses CAPTCHA, the script will not be able to bypass it automatically.

## Support

This script is not accompanied by long-term support. If you need to make modifications or improve functionality, you will need to do so on your own.

## Conclusion

This script was created solely to address a business need quickly and is not intended for long-term use or public distribution. Use it with caution and be aware of potential consequences.
