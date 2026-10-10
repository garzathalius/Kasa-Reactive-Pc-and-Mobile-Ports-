import os, sys, runpy, traceback

HERE = os.path.dirname(os.path.abspath(__file__)) if "__file__" in globals() else os.getcwd()
sys.path.insert(0, HERE)

try:
    runpy.run_path(os.path.join(HERE, "app_main.py"), run_name="__main__")
except BaseException:
    err = traceback.format_exc()
    try:
        with open(os.path.join(HERE, "kasa_crash.txt"), "w") as f:
            f.write(err)
    except Exception:
        pass

    from kivy.app import App
    from kivy.uix.scrollview import ScrollView
    from kivy.uix.label import Label

    class CrashApp(App):
        def build(self):
            sv = ScrollView()
            lbl = Label(text=err, size_hint_y=None, halign="left",
                        valign="top", font_size="12sp")
            lbl.bind(width=lambda *_: setattr(lbl, "text_size", (lbl.width, None)))
            lbl.bind(texture_size=lambda *_: setattr(lbl, "height", lbl.texture_size[1]))
            sv.add_widget(lbl)
            return sv

    CrashApp().run()
