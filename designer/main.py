"""Main code of designer"""

import tkinter

import tkintertools as tkt
import tkintertools.core.configs as configs
import tkintertools.core.constants as constants
import tkintertools.core.virtual as virtual
import tkintertools.standard.widgets as widgets
import tkintertools.toolbox as toolbox

if toolbox.load_font("designer/assets/fonts/LXGWWenKai.ttf"):
    constants.FONT = "LXGW WenKai"


class MenuBar(tkt.Frame):
    """Menu bar"""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, name=tkt.Frame, height=50, **kwargs)

        self.main_area = tkt.Frame(self, height=50)
        self.main_area.pack(side="left", fill="x", expand=True)
        self.operation_area = tkt.Frame(self, width=200, height=50)
        self.operation_area.pack(side="right")

        self.btn_file = tkt.Button(
            self.main_area, (5, 25), text="File(F)", anchor="w")
        _x = self.btn_file.position[0] + self.btn_file.size[0] + 5
        self.btn_edit = tkt.Button(
            self.main_area, (_x, 25), text="Edit(E)", anchor="w")
        _x = self.btn_edit.position[0] + self.btn_edit.size[0] + 5
        self.btn_select = tkt.Button(
            self.main_area, (_x, 25), text="Select(S)", anchor="w")
        _x = self.btn_select.position[0] + self.btn_select.size[0] + 5
        self.btn_view = tkt.Button(
            self.main_area, (_x, 25), text="View(V)", anchor="w")
        _x = self.btn_view.position[0] + self.btn_view.size[0] + 5
        self.btn_help = tkt.Button(
            self.main_area, (_x, 25), text="Help(H)", anchor="w")

        tkt.Button(self.operation_area, (195, 25), (40, 40),
                   text="\ue768", anchor="e")


class StatusBar(tkt.Frame):
    """Status Bar"""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, name=tkt.Frame, height=30, **kwargs)


class SideBar(tkt.Frame):
    """Side Bar"""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, name=tkt.Frame, width=70, **kwargs)

        self.main_area = tkt.Frame(self, width=70)
        self.main_area.pack(side="top", fill="y", expand=True)
        self.config_area = tkt.Frame(self, width=70, height=130)
        self.config_area.pack(side="bottom")

        tkt.SegmentedButton(
            self.main_area, (5, 1), ((50, 50),)*4, layout="vertical",
            text=("\uec50", "\ue721", "\uea86", "\ue74c"), fontsize=24)

        tkt.Button(self.config_area, (10, 15),
                   (50, 50), text="\ue77b", fontsize=24)
        tkt.Button(self.config_area, (10, 75),
                   (50, 50), text="\ue713", fontsize=24)


def gen_drag_feature(widget: virtual.Widget) -> virtual.Feature:
    """Generate a special Feature class"""

    class DragFeature(widget.feature.__class__):
        """Drag the Widget to a special place"""

        def __init__(self, *args, **kwargs) -> None:
            self.x: int | None = None
            self.y: int | None = None
            super().__init__(*args, **kwargs)

        def _button_1(self, event: tkinter.Event) -> bool:
            if self.widget.detect(event.x, event.y):
                self.x, self.y = event.x, event.y
            return getattr(super(), "_button_1", configs.Env.default_callback)(event)

        def _b_1_motion(self, event: tkinter.Event) -> bool:
            if self.x is not None:
                self.widget.move(event.x - self.x, event.y - self.y)
                self.x, self.y = event.x, event.y
            return getattr(super(), "_b_1_motion", configs.Env.default_callback)(event)

        def _button_release_1(self, event: tkinter.Event) -> bool:
            self.x = self.y = None
            return getattr(super(), "_button_release_1", configs.Env.default_callback)(event)

    return DragFeature


class App(tkt.Tk):
    """"""

    def __init__(self, *args, **kwargs) -> None:
        """"""
        super().__init__(*args, **kwargs)
        self.menu_bar = MenuBar(self)
        self.menu_bar.pack(side="top", fill="x")

        self.status_bar = StatusBar(self)
        self.status_bar.pack(side="bottom", fill="x")

        self.side_bar = SideBar(self)
        self.side_bar.pack(side="left", fill="y")

        self.main_area = tkt.Frame(self, name=tkt.Canvas)
        self.main_area.pack(fill="both", expand=True)

        self.tree_area = tkt.Frame(self.main_area, width=360, name=tkt.Canvas)
        self.tree_area.pack(side="left", fill="y")

        self.work_area = tkt.Frame(
            self.main_area, name="", bg="black", highlightthickness=0)
        self.work_area.pack(side="right", fill="both", expand=True)

        self.window = tkt.Frame(
            self.work_area, width=1280, height=720, expand="")
        self.window.place(x=50, y=50)


if __name__ == "__main__":
    app = App(size=(1600, 900), title="tkintertools designer v0.0.1")

    widget_list = [
        "Text",
        # "Image",
        "Label",
        "Button",
        "Switch",
        "InputBox",
        "ToggleButton",
        "CheckButton",
        "RadioButton",
        "ProgressBar",
        # "UnderlineButton",
        # "HighlightButton",
        "IconButton",
        "Slider",
        "SegmentedButton",
        "SpinBox",
        # "Tooltip",
    ]

    for i, widget_name in enumerate(widget_list):
        try:
            widget = getattr(widgets, widget_name)(
                app.window, (20, 20 + 50*i), text=widget_name)
        except TypeError:
            widget = getattr(widgets, widget_name)(
                app.window, (20, 20 + 50*i))
        gen_drag_feature(widget)(widget)

    app.mainloop()
