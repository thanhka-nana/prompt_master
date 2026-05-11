# notepad_clone/tien_ich/debounce.py

def debounce(widget, func, delay):
    """
    Hàm trì hoãn việc thực thi func cho đến khi người dùng ngừng thao tác trong 'delay' ms.
    Sử dụng after() của Tkinter để tránh chặn main loop.
    """
    after_id = None
    
    def wrapper(*args, **kwargs):
        nonlocal after_id
        if after_id:
            widget.after_cancel(after_id)
        # Sử dụng lambda để truyền args, kwargs vào func khi được gọi bởi after
        after_id = widget.after(delay, lambda: func(*args, **kwargs))
        
    return wrapper
