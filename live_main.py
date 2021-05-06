import wx
import live_wx

class registrasi(live_wx.MyFrame2):
    list_users = []

    def __init__(self, parent):
        live_wx.MyFrame2.__init__(self, parent)
        live_wx.MyFrame2.SetIcon(self, wx.Icon("gudang.ico"))

    def klik_button(self, event):
        datauser = []

        nama = self.input_nama.GetValue()
        asal = self.input_asal.GetValue()
        umur = self.input_umur.GetValue()

        # print("data berhasil")
        try:
            if nama == "" or asal == "" or umur == "":
                print("data ada yang kosong")
                wx.MessageBox("Data ada yang kosong", "Warning", wx.OK | wx.ICON_WARNING)
                if (wx.OK):
                    self.input_nama.SetValue("")
                    self.input_asal.SetValue("")
                    self.input_umur.SetValue("")

            elif not umur.isnumeric():
                print("Umur harus angka")
                wx.MessageBox("Umur harus angka", "Warning", wx.OK | wx.ICON_WARNING)
                if (wx.OK):
                    self.input_umur.SetValue("")

            else:
                datauser.append(nama)
                datauser.append(asal)
                datauser.append(umur)
                self.list_users.append(datauser)

                print("data berhasil disimpan")
                wx.MessageBox("Data berhasil disimpan", "Information", wx.OK | wx.ICON_INFORMATION)

                for row in range(len(self.list_users)):
                    for col in range(len(self.list_users[0])):
                        data_value = self.list_users[row][col]
                        self.m_grid1.SetCellValue(row, col, data_value)

                if (wx.OK):
                    self.input_nama.SetValue("")
                    self.input_asal.SetValue("")
                    self.input_umur.SetValue("")

                self.m_grid1.AppendRows(1)

        except Exception:
            wx.MessageBox("Data error", "Error", wx.OK | wx.ICON_ERROR)

if __name__ == "__main__":
    app = wx.App()
    regist = registrasi(parent=None)
    regist.Show()
    app.MainLoop()
