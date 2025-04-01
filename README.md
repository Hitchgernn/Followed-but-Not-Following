# Followed but Not Following  

Created by : [Hitchgernn](https://www.instagram.com/hitchgernn)
## 1. Export Your Instagram Data
1. Go to Instagram → Settings → Your activity.
2. Scroll down and select **Download your information**.
3. Request to **download your data** (choose **JSON format**).
4. Instagram will email you a ZIP file – download and extract it.
5. Create a new folder.
6. Inside the extracted folder, find files:

   ```sh
   followers.json
   following.json
   ```
   if there is `followers_1.json` file, rename it to `followers.json`
7. Move those two files into new folder you created.

## 2. Download & Run the Script
1. Open your terminal and move to a folder you have created.
2. Download the Python script from GitHub:
   - Windows

   ```sh
   curl -o main.py https://raw.githubusercontent.com/Hitchgernn/Followed-but-Not-Following/main/main.py
   ```
   - Mac/Linux

   ```sh
   wget https://raw.githubusercontent.com/Hitchgernn/Followed-but-Not-Following/main/main.py
   ```
3. Run the script in terminal:

   ```sh
   python main.py
   ```
4. It will display a list of people who don’t follow you back.


