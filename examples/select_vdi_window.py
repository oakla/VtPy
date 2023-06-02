import win32gui

def select_window():
    # Find the window by its title
    hwnd = win32gui.FindWindow(None, "CVS Main Windows HVD – AU - CFS - Desktop Viewer")

    # Bring the window to the foreground
    win32gui.SetForegroundWindow(hwnd)

select_window()