[app]
title = MyApp
package.name = myapp
package.domain = com.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.3.0,plyer
android.permissions = POST_NOTIFICATIONS,VIBRATE
orientation = portrait
android.minapi = 21
android.targetapi = 33
android.ndk = 25b
android.archs = arm64-v8a
android.enable_androidx = True

[buildozer]
log_level = 2
warn_on_root = 1
