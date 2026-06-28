# APK Builder

## How to use

1. Edit `app_script.txt` — write your Python/Kivy app code here
2. Push this folder to a FREE GitHub repo
3. GitHub automatically builds your APK (~10 min)
4. Download the APK from the Actions tab

---

## Step by step

### First time setup (do once):
1. Go to github.com and create a free account
2. Click "New repository" → name it anything → set to Public → Create
3. Upload ALL files from this zip into the repo

### Every time you want a new APK:
1. Edit `app_script.txt` with your app code
2. Commit/push the change on GitHub
3. Click the **Actions** tab at the top
4. Wait ~10 minutes for the green checkmark
5. Click the run → scroll down → **Artifacts** → download your APK

### Install APK on phone:
- Copy APK to your Android phone
- Tap it to install
- Allow "Install from unknown sources" if prompted

---

## Changing the notification message

In `app_script.txt`, find this line:
```
message="Hello testing",
```
Change it to whatever you want!

## Changing the app name

In `buildozer.spec`, find:
```
title = MyApp
```
Change it to your app name.
