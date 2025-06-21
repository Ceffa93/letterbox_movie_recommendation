def print_vram_info():
    import psutil
    vram = psutil.virtual_memory()
    print(f"Total VRAM: {vram.total / 1024**3:.2f} GB")
    print(f"Available VRAM: {vram.available / 1024**3:.2f} GB")
    print(f"Used VRAM: {vram.used / 1024**3:.2f} GB")
    print(f"Percentage Used: {vram.percent}%")
    