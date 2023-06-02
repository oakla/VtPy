import win32gui
import win32con


TARGET_WINDOW_TITLE = 'CVS Main Windows HVD – AU - CFS - Desktop Viewer'

def send_page_down(handle, param):
    if win32gui.GetClassName(handle) == param:
        win32gui.SendMessage(handle, win32con.WM_KEYDOWN, win32con.VK_NEXT, 0)
        win32gui.SendMessage(handle, win32con.WM_KEYUP, win32con.VK_NEXT, 0)


window_id = win32gui.FindWindow(None, "my_multipage_doc.pdf - Foxit Reader")
win32gui.EnumChildWindows(window_id, send_page_down, 'FoxitDocWnd')


