import math

import tkintertools as tkt
import tkintertools.animation as animation


class LoginToplevel(tkt.Toplevel):
    """"""

    def load_ui(self) -> None:
        """"""
        canvas = tkt.Canvas(self)
        canvas.place(width=480, height=720)

        self.sub_title = tkt.Information(
            canvas, (240, 45), text="登录到你的账号", fontsize=36)

        canvas.create_oval(120, 90, 360, 330, outline="grey")
        canvas.create_text(240, 210, text="用户\n头像", fill="grey", font=30)

        self.account = tkt.Entry(canvas, (40, 360), (400, 50))
        self.password = tkt.Entry(canvas, (40, 430), (400, 50))
        self.an = tkt.Button(canvas, (40, 500), (190, 50),
                             text="注 册", command=self.animate)
        self.login = tkt.Button(canvas, (250, 500), (190, 50), text="登 录")
        self.password_verify = tkt.Entry(canvas, (40, 500+300), (400, 50))
        self.registry = tkt.Button(
            canvas, (40-300, 570), (190, 50), text="注 册")
        self.back = tkt.Button(canvas, (250+300, 570),
                               (190, 50), text="返 回", command=lambda: self.animate(True))

        self.forget = tkt.UnderlineButton(
            canvas, (140, 600), text="忘记密码", fontsize=20)
        self.sep = tkt.Information(canvas, (190, 600), text="|")
        self.find = tkt.UnderlineButton(
            canvas, (240, 600), text="找回账号", fontsize=20)
        self.sep_2 = tkt.Information(canvas, (290, 600), text="|")
        self.net = tkt.UnderlineButton(
            canvas, (340, 600), text="网络设置", fontsize=20)
        self.animation_lock = False  # 防熊

    def animate(self, back: bool = False) -> None:
        """"""
        if self.animation_lock:
            return
        self.animation_lock = True
        k = -1 if back else 1
        self.after(
            250, self.sub_title.texts[0].set, "登录到你的账号" if back else "注册新的账号")
        self.after(
            250, self.title, "登录" if back else "注册")
        animation.MoveWidget(self.sub_title, 500, (0, -80),
                             controller=animation.controller_generator(math.sin, 0, math.pi, map_y=False), fps=60,
                             end=lambda: self.__setattr__("animation_lock", False)).start()
        animation.MoveWidget(self.an, 500, (-300*k, 0),
                             controller=animation.smooth, fps=60).start()
        animation.MoveWidget(self.login, 500, (300*k, 0),
                             controller=animation.smooth, fps=60).start()
        animation.MoveWidget(self.registry, 500, (300*k, 0),
                             controller=animation.smooth, fps=60).start()
        animation.MoveWidget(self.back, 500, (-300*k, 0),
                             controller=animation.smooth, fps=60).start()
        animation.MoveWidget(self.forget, 500, (0, 100*k),
                             controller=animation.smooth, fps=60).start()
        animation.MoveWidget(self.sep, 500, (0, 100*k),
                             controller=animation.smooth, fps=60).start()
        animation.MoveWidget(self.find, 500, (0, 100*k),
                             controller=animation.smooth, fps=60).start()
        animation.MoveWidget(self.sep_2, 500, (0, 100*k),
                             controller=animation.smooth, fps=60).start()
        animation.MoveWidget(self.net, 500, (0, 100*k),
                             controller=animation.smooth, fps=60).start()
        animation.MoveWidget(self.password_verify, 500, (0, -300*k),
                             controller=animation.smooth, fps=60).start()
