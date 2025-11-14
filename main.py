import tkinter as tk
from tkinter import ttk, messagebox
import webview
import webbrowser

apis = {
    "夜幕解析": "https://www.yemu.xyz/?url={}",
    "虾米解析(有广告)": "https://jx.xmflv.cc/?url={}"
}

def main():
    root = tk.Tk()
    root.title("视频解析工具")
    
    # 样式配置
    style = ttk.Style()
    style.theme_use('clam')
    style.configure('Title.TLabel', font=('Minecraft AE', 16, 'bold'), foreground='#2C3E50')
    style.configure('Header.TLabel', font=('Minecraft AE', 10), foreground='#34495E')
    style.configure('TCombobox', font=('Minecraft AE', 10), fieldbackground='white', 
                   background='white', lightcolor='#BDC3C7', darkcolor='#95A5A6')
    style.map('TCombobox', fieldbackground=[('readonly', 'white')],
             lightcolor=[('focus', '#3498DB')], darkcolor=[('focus', '#2980B9')])
    style.configure('TEntry', font=('Minecraft AE', 10), fieldbackground='white',
                   background='white', lightcolor='#BDC3C7', darkcolor='#95A5A6')
    style.map('TEntry', lightcolor=[('focus', '#3498DB')], darkcolor=[('focus', '#2980B9')])
    style.configure('Accent.TButton', font=('Minecraft AE', 11, 'bold'), 
                   background='#3498DB', foreground='white', padding=10,
                   relief='flat', borderwidth=0, focuscolor='#2980B9')
    style.map('Accent.TButton', background=[('active', '#2980B9')], 
             relief=[('pressed', 'flat')])
    
    # 变量定义
    api_var = tk.StringVar()
    api_var.set(list(apis.keys())[0])
    url_entry = ttk.Entry(root, font=('Minecraft AE', 10))
    cur_url = None
    
    # 解析函数
    def parse():
        nonlocal cur_url
        url = url_entry.get().strip()
        
        if not url:
            messagebox.showwarning("警告", "请输入视频网址！")
            return
            
        api_name = api_var.get()
        api_template = apis[api_name]
        cur_url = api_template.format(url)
        
        root.withdraw()
        try:
            webview.create_window(
                title="视频播放",
                url=cur_url,
                width=1200,
                height=800,
                resizable=True
            )
            webview.start()
        except Exception as e:
            print(f"打开视频播放窗口失败：{str(e)}")
        finally:
            root.deiconify()
            url_entry.delete(0, tk.END)
            url_entry.focus()
    
    # 关闭处理
    root.protocol("WM_DELETE_WINDOW", lambda: (root.destroy(), exit()))
    
    # 界面布局 - 使用坐标布局
    root.geometry("400x350")  # 设置窗口大小
    
    # 标题
    title_label = ttk.Label(root, text="视频解析工具", style='Title.TLabel')
    title_label.place(x=200, y=30, anchor="center")
    
    # 选择解析接口标签
    api_label = ttk.Label(root, text="选择解析接口：", style='Header.TLabel')
    api_label.place(x=50, y=80)
    
    # 下拉菜单
    api_combo = ttk.Combobox(root, textvariable=api_var, values=list(apis.keys()), 
                            state="readonly", height=5)
    api_combo.place(x=50, y=105, width=300, height=30)
    
    # 网址输入标签
    url_label = ttk.Label(root, text="请输入视频网址：", style='Header.TLabel')
    url_label.place(x=50, y=150)
    
    # 输入框
    url_entry.place(x=50, y=175, width=300, height=35)
    
    # 解析按钮
    parse_btn = ttk.Button(root, text="🎬 解析视频", command=parse, style='Accent.TButton')
    parse_btn.place(x=50, y=230, width=300, height=40)
    
    # 官网链接
    website_label = tk.Label(root, text="官网", font=('Minecraft AE', 8), 
                            fg='#3498DB', cursor='hand2')
    website_label.place(x=350, y=300, anchor="ne")
    website_label.bind('<Button-1>', lambda e: webbrowser.open("https://blog.tbsky.xyz"))
    
    # 事件绑定
    url_entry.bind('<Return>', lambda e: parse())
    url_entry.focus()
    
    root.mainloop()

if __name__ == "__main__":
    main()