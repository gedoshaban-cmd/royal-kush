[app]

# (str) Title of your application
title = Royal Kush

# (str) Package name
package.name = royalkush

# (str) Package domain (needed for android/ios packaging)
package.domain = org.royalkush

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json,ttf,otf

# (list) Source files to exclude
source.exclude_exts = spec

# (list) List of directory to exclude
source.exclude_dirs = tests, bin, venv, .git, __pycache__

# (str) Application versioning (method 1)
version = 1.0.0

# (list) Application requirements
# ✅ تم إصلاح مشكلة kivy==2.3.0 وتحديد إصدار Python
requirements = python3==3.10.12,kivy==2.3.0,cython==0.29.36,openssl,pyopenssl,android,pillow,requests

# (str) Custom source folders for requirements
# p4a.source_dir =

# (str) The directory in which python-for-android should look for your own build recipes
# p4a.local_recipes =

# (str) Bootstrap to use for android builds
# p4a.bootstrap = sdl2

# (str) Android entry point
# android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme
# android.apptheme = "@android:style/Theme.NoTitleBar"

# (str) Android logcat filters to use
android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a libpymodules.so
android.copy_libs = 1

# (str) The Android arch to build for
android.archs = arm64-v8a, armeabi-v7a

# (int) Minimum API your APK / AAB will support
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 33

# (int) Android NDK version to use
android.ndk = 25b

# (str) Android NDK directory (if empty, it will be automatically downloaded)
android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded)
android.sdk_path =

# (bool) If True, then skip trying to update the Android sdk
android.skip_update = False

# (bool) If True, then automatically accept SDK license agreements
android.accept_sdk_license = True

# (str) Android app category
android.category = GAME

# (str) Android app permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (str) launchMode to set for the main activity
android.manifest.launch_mode = standard

# (bool) enable AndroidX support
android.enable_androidx = True

# (str) Android API to use
android.api = 33

# (bool) Indicate whether the app is not be compiled in debug mode
android.debug = False

# (bool) Indicate whether the app is released
android.release = False


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
