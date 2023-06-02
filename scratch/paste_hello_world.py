import win32gui
import win32clipboard
import win32con

def send_ctrl_v():
    # Find the window by its title
    hwnd = win32gui.FindWindow(None, "Notepad")
    # hwnd = win32gui.FindWindow(None, "CVS Main Windows HVD – AU - CFS - Desktop Viewer")

    # Bring the window to the foreground
    # win32gui.SetForegroundWindow(hwnd)

    # Set the clipboard data
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText("Hello, world!")
    win32clipboard.CloseClipboard()

    # Send the WM_PASTE message to the window
    win32gui.SendMessage(hwnd, win32con.WM_PASTE, 0, 0)

send_ctrl_v()