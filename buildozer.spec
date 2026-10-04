[app]

title = Royal Kush
package.name = royalkush
package.domain = org.royalkush
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,ttf,otf
source.exclude_exts = spec
source.exclude_dirs = tests, bin, venv, .git, __pycache__
version = 1.0.0

requirements = python3,kivy,cython,openssl,pyopenssl,pillow,requests

android.logcat_filters = *:S python:D
android.copy_libs = 1
android.archs = arm64-v8a, armeabi-v7a
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.category = GAME
android.permissions = INTERNET,ACCESS_NETWORK_STATE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.manifest.launch_mode = standard
android.enable_androidx = True
android.api = 33
android.debug = False
android.release = False

[buildozer]
log_level = 2
warn_on_root = 1
