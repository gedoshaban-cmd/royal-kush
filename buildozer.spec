
[app]
title = Royal Kush
package.name = royalkush
package.domain = org.gedoshaban
source.dir =.
source.include_exts = py,png,jpg,kv,atlas,json
version = 0.1
requirements = python3,kivy==2.3.0
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreement = True
android.arch = armeabi-v7a
p4a.bootstrap = sdl2
p4a.branch = master
