# Instagram Unfollowers Tracker using Python


## 1. Export Your Instagram Data

1. Go to Instagram → Settings → Your activity.
2. Scroll down and select **Download your information**.
3. Request to **download your data** (choose **JSON format**).
4. Instagram will email you a ZIP file – download and extract it.
5. Create a new folder
6. Inside the extracted folder, find the file:
   
   ```sh
   followers.json
   following.json
   ```
   if there is `followers_1.json` file, rename it to `followers.json`
7. Move those two files into the new folder you created.

## 2. Download & Run the Script

1. Download the Python script from GitHub and place it in the same folder as your exported `followers.json` and `following.json` file.

   - Windows
   ```sh
   curl -o main.py https://raw.githubusercontent.com/Hitchgernn/Unfollowers-Checker/main/main.py
   ```
   - Mac/Linux
   ```sh
   wget https://raw.githubusercontent.com/Hitchgernn/Unfollowers-Checker/main/main.py
   ```
1. Run the script in the terminal:

   ```sh
   python main.py
   ```
2. It will display a list of people who don’t follow you back.


