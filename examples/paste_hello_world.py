import win32gui
import win32con
import win32process
import win32api
import win32clipboard

# Find the window by its title
hwnd = win32gui.FindWindow(None, "CVS Main Windows HVD – AU - CFS - Desktop Viewer")

# Get the window's thread ID and process ID
tid, pid = win32process.GetWindowThreadProcessId(hwnd)

# Attach to the window's thread
thread_handle = win32api.OpenThread(win32con.THREAD_ALL_ACCESS, False, tid)
win32process.AttachThreadInput(win32api.GetCurrentThreadId(), tid, True)

# Set the clipboard data
win32clipboard.OpenClipboard()
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText("Hello, world!")
win32clipboard.CloseClipboard()

# Send the WM_PASTE message to the window
win32gui.SendMessage(hwnd, win32con.WM_PASTE, 0, 0)

# Detach from the window's thread
win32process.AttachThreadInput(win32api.GetCurrentThreadId(), tid, False)
win32api.CloseHandle(thread_handle)