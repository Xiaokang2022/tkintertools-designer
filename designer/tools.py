import tkinter
import types

import tkintertools as tkt
import tkintertools.core.virtual as virtual
import tkintertools.standard.features as features
import tkintertools.standard.widgets as widgets

# root = tkt.Tk()
# canvas = tkt.Canvas(root)
# canvas.place(width=1280, height=720)


def gen_drag_feature(widget: virtual.Widget) -> virtual.Feature:
    """Generate a special Feature class"""

    class DragFeature(widget.feature.__class__):
        """Drag the Widget to a special place"""

        def __init__(self, *args, **kwargs) -> None:
            self.x: int | None = None
            self.y: int | None = None
            super().__init__(*args, **kwargs)

        def _click_left(self, event: tkinter.Event) -> bool:
            if self.widget.detect(event.x, event.y):
                self.x, self.y = event.x, event.y
            return super()._click_left(event)

        def _move_left(self, event: tkinter.Event) -> bool:
            if self.x is not None:
                self.widget.move(event.x - self.x, event.y - self.y)
                self.x, self.y = event.x, event.y
            return super()._click_center(event)

        def _release_left(self, event: tkinter.Event) -> bool:
            self.x = self.y = None
            return super()._release_left(event)

    return DragFeature


# widget_list = [
#     "Text",
#     # "Image",
#     "Label",
#     "Button",
#     "Switch",
#     "InputBox",
#     "ToggleButton",
#     "CheckButton",
#     "RadioButton",
#     "ProgressBar",
#     # "UnderlineButton",
#     # "HighlightButton",
#     "IconButton",
#     "Slider",
#     "SegmentedButton",
#     "SpinBox",
#     # "Tooltip",
# ]

# for i, widget_name in enumerate(widget_list):
#     try:
#         widget = getattr(widgets, widget_name)(
#             canvas, (20, 20 + 50*i), text=widget_name)
#     except TypeError:
#         widget = getattr(widgets, widget_name)(canvas, (20, 20 + 50*i))
#     gen_drag_feature(widget)(widget)


# root.mainloop()
