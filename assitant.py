import wx
import wolframalpha
import wikipedia


class MyFrame(wx.Frame):


    def __init__(self):

        wx.Frame.__init__(self, None, pos=wx.DefaultPosition, size=wx.Size(450, 100),
                          style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN,
                          title="Assistant")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel, label="hello i am your personal assistant")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER, size=(400, 30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def OnEnter(self, event):

        q = self.txt.GetValue()
        q = q.lower()

        try:

            # wolframalpha
            app_id = "JGPKA4-TQK6EV99VR"

            client = wolframalpha.Client(app_id)
            res = client.query(q)

            ans = next(res.results).text

            print(ans)

        except:

            # wiki

            print(wikipedia.summary(q))


if __name__ == "__main__":

    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()
