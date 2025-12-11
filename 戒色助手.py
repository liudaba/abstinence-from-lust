# -*- coding: utf-8 -*-
"""戒色助手 - 记录·分析·激励"""

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from datetime import datetime, timedelta
import json, os, random, webbrowser

DATA_FILE = os.path.join(os.path.expanduser('~'), '.jiesezushou_data.json')

class App:
    # 内容库 - 每天零晨随机更新
    MUSIC_ALL = [
        ("追梦赤子心 - GALA", "https://music.163.com/#/song?id=31010566"),
        ("最初的梦想 - 范玮琪", "https://music.163.com/#/song?id=255858"),
        ("阳光总在风雨后 - 许美静", "https://music.163.com/#/song?id=277322"),
        ("怒放的生命 - 汪峰", "https://music.163.com/#/song?id=167882"),
        ("平凡之路 - 朴树", "https://music.163.com/#/song?id=28815250"),
        ("海阔天空 - Beyond", "https://music.163.com/#/song?id=347230"),
        ("我相信 - 杨培安", "https://music.163.com/#/song?id=25706282"),
        ("倔强 - 五月天", "https://music.163.com/#/song?id=169159"),
        ("飞得更高 - 汪峰", "https://music.163.com/#/song?id=167876"),
        ("相信自己 - 零点乐队", "https://music.163.com/#/song?id=385905"),
        ("光辉岁月 - Beyond", "https://music.163.com/#/song?id=347235"),
        ("真的爱你 - Beyond", "https://music.163.com/#/song?id=347231"),
        ("蓝莲花 - 许巍", "https://music.163.com/#/song?id=186016"),
        ("改变自己 - 王力宏", "https://music.163.com/#/song?id=326904"),
        ("男儿当自强 - 林子祥", "https://music.163.com/#/song?id=347607"),
        ("从头再来 - 刘德华", "https://music.163.com/#/song?id=347953"),
    ]
    
    VIDEO_ALL = [
        ("当幸福来敲门 (豆瓣9.1)", "https://movie.douban.com/subject/1849031/"),
        ("肖申克的救赎 (豆瓣9.7)", "https://movie.douban.com/subject/1292052/"),
        ("阿甘正传 (豆瓣9.5)", "https://movie.douban.com/subject/1292720/"),
        ("摔跤吧爸爸 (豆瓣9.0)", "https://movie.douban.com/subject/26387939/"),
        ("心灵奇旅 (豆瓣8.7)", "https://movie.douban.com/subject/24733428/"),
        ("无问西东 (豆瓣7.6)", "https://movie.douban.com/subject/6874741/"),
        ("绿皮书 (豆瓣8.9)", "https://movie.douban.com/subject/27060077/"),
        ("美丽人生 (豆瓣9.5)", "https://movie.douban.com/subject/1292063/"),
        ("放牛班的春天 (豆瓣9.3)", "https://movie.douban.com/subject/1291Mo549/"),
        ("火战车 (豆瓣9.1)", "https://movie.douban.com/subject/1292199/"),
        ("风雨哈佛路 (豆瓣8.5)", "https://movie.douban.com/subject/1463371/"),
        ("中国合伙人 (豆瓣7.6)", "https://movie.douban.com/subject/3821Mo067/"),
    ]
    
    BOOK_ALL = [
        ("活着 - 余华", "https://book.douban.com/subject/4913064/"),
        ("人性的弱点 - 卡耐基", "https://book.douban.com/subject/25985683/"),
        ("自控力 - 凯莉", "https://book.douban.com/subject/10786473/"),
        ("原则 - 达利欧", "https://book.douban.com/subject/27608239/"),
        ("刻意练习", "https://book.douban.com/subject/26895993/"),
        ("心流", "https://book.douban.com/subject/27186106/"),
        ("高效能人士的七个习惯", "https://book.douban.com/subject/5325618/"),
        ("思考快与慢", "https://book.douban.com/subject/10785583/"),
        ("少有人走的路", "https://book.douban.com/subject/1775691/"),
        ("非暴力沟通", "https://book.douban.com/subject/3533221/"),
        ("影响力 - 西奥迪尼", "https://book.douban.com/subject/1786387/"),
        ("微习惯", "https://book.douban.com/subject/26877306/"),
    ]
    
    INTL_NEWS = [
        ("新华网国际", "http://www.news.cn/world/"),
        ("人民网国际", "http://world.people.com.cn/"),
        ("央视网国际", "https://news.cctv.com/world/"),
        ("环球时报", "https://world.huanqiu.com/"),
        ("参考消息", "http://www.cankaoxiaoxi.com/"),
        ("中国日报国际", "https://world.chinadaily.com.cn/"),
        ("凤凰国际", "https://news.ifeng.com/world/"),
    ]
    
    CN_NEWS = [
        ("新华网", "http://www.news.cn/"),
        ("人民网", "http://www.people.com.cn/"),
        ("央视网", "https://news.cctv.com/"),
        ("中国政府网", "http://www.gov.cn/"),
        ("光明网", "https://www.gmw.cn/"),
        ("中新网", "https://www.chinanews.com/"),
        ("法制网", "http://www.legaldaily.com.cn/"),
    ]
    
    TIPS_ALL = [
        "立即做20个俵卧撑或跑步，通过运动消耗多余精力",
        "用冷水洗脸，快速让自己清醒冷静下来",
        "打电话给家人或朋友聊天，转移注意力",
        "想象达成目标后的自己，自信、健康、充满活力",
        "去人多的地方，如公园、图书馆、商场",
        "深呼吸几次，让自己的心跳慢下来",
        "倒一杯冰水喝下，刺激感觉让理智回归",
        "立刻离开当前环境，换一个房间或出门走走",
        "听一首激励的歌曲，让音乐带给你正能量",
        "拿起一本书阅读，让大脑专注于知识",
        "写日记记录当前的感受，让情绪得到释放",
        "看一部励志电影，从中汲取力量",
        "整理房间或打扫卫生，让身体忙起来",
        "学习一项新技能，如乐器、编程、绘画",
        "做一道菜或烘焙美食，享受创造的乐趣",
        "冥想几分钟，让心灵安静下来",
        "回顾自己的目标，想想为什么要改变",
        "跟宠物玩耍，享受纯粹的快乐",
        "做拉伸或瑰伽，让身体放松",
        "给未来的自己写一封信，明确目标与期望",
        "回忆上次失败后的后悔，提醒自己不值得",
        "出门跑步半小时，流汗后会感觉很清爽",
        "打开窗户呼吸新鲜空气，让头脑清醒",
        "设定一个小目标，完成后奖励自己",
        "想想父母的期望，不要让他们失望",
        "洗个冷水澡，重新激发精神",
        "列出明天的计划，让心中有目标",
        "学一个新单词或算一道数学题，训练大脑",
        "写下10个你感激的人或事，培养正念",
        "大声说出''我可以做到''，给自己加油",
    ]
    
    def get_daily_content(self, items, count=6):
        """根据当天日期生成随机内容,每天零晨自动更新"""
        today = datetime.now().strftime('%Y%m%d')
        random.seed(int(today))
        return random.sample(items, min(count, len(items)))
    
    def __init__(self, root):
        self.root = root
        self.root.title("戒色助手")
        self.root.geometry("900x650")
        self.data = self.load_data()
        self.anim_running = False  # 动画状态
        self.setup_ui()
        self.show_page("checkin")
    
    def load_data(self):
        default = {'streak': 0, 'longest': 0, 'total': 0, 'relapse': 0, 'last': None, 'history': []}
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, 'r', encoding='utf-8') as f:
                    d = json.load(f)
                    for k in default:
                        if k not in d: d[k] = default[k]
                    return d
            except: pass
        return default
    
    def save_data(self):
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False)
    
    def setup_ui(self):
        # 左侧菜单
        left = tk.Frame(self.root, bg="#2c3e50", width=160)
        left.pack(side=tk.LEFT, fill=tk.Y)
        left.pack_propagate(False)
        
        tk.Label(left, text="🌟 戒色助手", font=("Microsoft YaHei", 13, "bold"),
                bg="#2c3e50", fg="white", pady=15).pack(fill=tk.X)
        
        menus = [("📋 打卡", "checkin"), ("📊 统计", "stats"), ("💡 技巧", "tips"),
                ("🎵 音乐", "music"), ("🎬 视频", "video"), ("📚 书籍", "book"),
                ("🌍 国际新闻", "intl"), ("🇨🇳 国内新闻", "cn")]
        
        for text, page in menus:
            btn = tk.Label(left, text=text, font=("Microsoft YaHei", 11),
                          bg="#2c3e50", fg="white", pady=10, padx=10, anchor="w", cursor="hand2")
            btn.pack(fill=tk.X)
            btn.bind("<Enter>", lambda e,b=btn: b.config(bg="#34495e"))
            btn.bind("<Leave>", lambda e,b=btn: b.config(bg="#2c3e50"))
            btn.bind("<Button-1>", lambda e,p=page: self.show_page(p))
        
        # 右侧内容
        self.content = tk.Frame(self.root, bg="white")
        self.content.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    def clear_content(self):
        self.anim_running = False  # 停止动画
        for w in self.content.winfo_children(): w.destroy()
    
    def create_gradient_bg(self, colors, speed=50):
        """创建动态渐变背景"""
        canvas = tk.Canvas(self.content, highlightthickness=0)
        canvas.pack(fill=tk.BOTH, expand=True)
        
        self.gradient_phase = 0
        self.gradient_colors = colors
        self.anim_running = True
        
        def draw_gradient():
            if not self.anim_running: return
            try:
                w = canvas.winfo_width()
                h = canvas.winfo_height()
                if w < 10: w = 800
                if h < 10: h = 600
                canvas.delete("gradient")
                
                # 计算当前颜色
                phase = (self.gradient_phase % 360) / 360.0
                idx = int(phase * len(colors))
                next_idx = (idx + 1) % len(colors)
                blend = (phase * len(colors)) % 1
                
                c1 = colors[idx]
                c2 = colors[next_idx]
                
                # 混合颜色
                r1, g1, b1 = int(c1[1:3], 16), int(c1[3:5], 16), int(c1[5:7], 16)
                r2, g2, b2 = int(c2[1:3], 16), int(c2[3:5], 16), int(c2[5:7], 16)
                
                for i in range(0, h, 4):
                    ratio = i / h
                    r = int(r1 + (r2 - r1) * blend + (30 * ratio))
                    g = int(g1 + (g2 - g1) * blend + (20 * ratio))
                    b = int(b1 + (b2 - b1) * blend - (10 * ratio))
                    r, g, b = max(0, min(255, r)), max(0, min(255, g)), max(0, min(255, b))
                    color = f"#{r:02x}{g:02x}{b:02x}"
                    canvas.create_line(0, i, w, i, fill=color, tags="gradient")
                
                self.gradient_phase += 1
                canvas.after(speed, draw_gradient)
            except: pass
        
        canvas.after(100, draw_gradient)
        return canvas
    
    def show_page(self, page):
        self.clear_content()
        if page == "checkin": self.page_checkin()
        elif page == "stats": self.page_stats()
        elif page == "tips": self.page_tips()
        elif page == "music": self.page_list("🎵 正能量音乐 (今日推荐)", self.get_daily_content(self.MUSIC_ALL, 8))
        elif page == "video": self.page_list("🎬 正能量电影 (今日推荐)", self.get_daily_content(self.VIDEO_ALL, 6))
        elif page == "book": self.page_list("📚 正能量书籍 (今日推荐)", self.get_daily_content(self.BOOK_ALL, 6))
        elif page == "intl": self.page_list("🌍 国际新闻", self.get_daily_content(self.INTL_NEWS, 5))
        elif page == "cn": self.page_list("🇨🇳 国内新闻", self.get_daily_content(self.CN_NEWS, 5))
    
    def page_checkin(self):
        # 绿色系动态背景
        canvas = self.create_gradient_bg(["#e8f5e9", "#c8e6c9", "#a5d6a7", "#c8e6c9"], 80)
        
        f = tk.Frame(canvas, bg="")
        f.place(relx=0.5, rely=0.45, anchor="center")
        f.config(bg=canvas.cget('bg') if canvas.cget('bg') else '#e8f5e9')
        
        # 使用透明效果的内容框
        inner = tk.Frame(f, bg="#f5f5f5", padx=30, pady=20)
        inner.pack()
        
        tk.Label(inner, text=str(self.data['total']), font=("Microsoft YaHei", 72, "bold"),
                fg="#27ae60", bg="#f5f5f5").pack()
        tk.Label(inner, text="戒断天数总计", font=("Microsoft YaHei", 16), fg="#7f8c8d", bg="#f5f5f5").pack()
        tk.Button(inner, text="清零", font=("Microsoft YaHei", 9), fg="#e74c3c", cursor="hand2",
                 command=lambda: self.reset_field('total')).pack(pady=5)
        
        bf = tk.Frame(inner, bg="#f5f5f5")
        bf.pack(pady=25)
        tk.Button(bf, text="✓ 今日打卡", font=("Microsoft YaHei", 13, "bold"),
                 bg="#27ae60", fg="white", width=12, height=2, command=self.do_checkin).pack(side=tk.LEFT, padx=8)
        tk.Button(bf, text="标记破戒", font=("Microsoft YaHei", 13, "bold"),
                 bg="#e67e22", fg="white", width=12, height=2, command=self.do_relapse).pack(side=tk.LEFT, padx=8)
        
        sf = tk.Frame(inner, bg="#f5f5f5")
        sf.pack(pady=15)
        for v, l in [(self.data['total'], "总天数"), (self.data['longest'], "最长连续"), (self.data['relapse'], "破戒次数")]:
            tk.Label(sf, text=f"{v}\n{l}", font=("Microsoft YaHei", 12), fg="#3498db", bg="#f5f5f5", padx=20).pack(side=tk.LEFT)
        
        self.msg = tk.Label(inner, text="", font=("Microsoft YaHei", 12), bg="#f5f5f5")
        self.msg.pack(pady=10)
        
        # 实时日期时间显示
        self.time_label = tk.Label(inner, text="", font=("Microsoft YaHei", 14), fg="#3498db", bg="#f5f5f5")
        self.time_label.pack(pady=15)
        self.update_time()
    
    def page_stats(self):
        # 蓝色系动态背景
        canvas = self.create_gradient_bg(["#e3f2fd", "#bbdefb", "#90caf9", "#bbdefb"], 80)
        
        f = tk.Frame(canvas, bg="#fafafa", padx=30, pady=20)
        f.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        tk.Label(f, text="📊 数据统计", font=("Microsoft YaHei", 18, "bold"), bg="#fafafa", fg="#2c3e50").pack(anchor="w")
        
        # 统计卡片
        sf = tk.Frame(f, bg="#fafafa")
        sf.pack(pady=15, anchor="w")
        for v, l, c, key in [(self.data['total'], "总戒断天数", "#27ae60", "total"), 
                        (self.data['longest'], "最长连续", "#3498db", "longest"),
                        (self.data['relapse'], "破戒次数", "#e67e22", "relapse")]:
            card = tk.Frame(sf, bg=c)
            card.pack(side=tk.LEFT, padx=5)
            tk.Label(card, text=f" {v} {l} ", font=("Microsoft YaHei", 13, "bold"), bg=c, fg="white", padx=12, pady=8).pack(side=tk.LEFT)
            tk.Button(card, text="清零", font=("Microsoft YaHei", 8), bg="white", fg=c, 
                     command=lambda k=key: self.reset_field(k)).pack(side=tk.LEFT, padx=2)
        
        # 万年历标题
        self.cal_frame = tk.Frame(f, bg="#fafafa")
        self.cal_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # 月份导航
        nav = tk.Frame(self.cal_frame, bg="#fafafa")
        nav.pack(fill=tk.X, pady=5)
        
        self.current_month = datetime.now()
        
        tk.Button(nav, text="◀ 上月", font=("Microsoft YaHei", 10), command=self.prev_month).pack(side=tk.LEFT)
        self.month_label = tk.Label(nav, text="", font=("Microsoft YaHei", 14, "bold"), bg="#fafafa", fg="#2c3e50")
        self.month_label.pack(side=tk.LEFT, expand=True)
        tk.Button(nav, text="下月 ▶", font=("Microsoft YaHei", 10), command=self.next_month).pack(side=tk.RIGHT)
        
        # 日历容器
        self.calendar_container = tk.Frame(self.cal_frame, bg="#fafafa")
        self.calendar_container.pack(fill=tk.BOTH, expand=True)
        
        self.draw_calendar()
        self.update_calendar_time()
    
    def prev_month(self):
        self.current_month = self.current_month.replace(day=1) - timedelta(days=1)
        self.draw_calendar()
    
    def next_month(self):
        next_m = self.current_month.replace(day=28) + timedelta(days=4)
        self.current_month = next_m.replace(day=1)
        self.draw_calendar()
    
    def draw_calendar(self):
        for w in self.calendar_container.winfo_children(): w.destroy()
        
        year = self.current_month.year
        month = self.current_month.month
        self.month_label.config(text=f"{year}年 {month}月")
        
        # 星期标题
        days_header = tk.Frame(self.calendar_container, bg="#3498db")
        days_header.pack(fill=tk.X)
        for day in ["日", "一", "二", "三", "四", "五", "六"]:
            c = "#e74c3c" if day in ["日", "六"] else "white"
            tk.Label(days_header, text=day, font=("Microsoft YaHei", 12, "bold"), 
                    bg="#3498db", fg=c, width=6, pady=8).pack(side=tk.LEFT, expand=True)
        
        # 获取月份信息
        import calendar
        cal = calendar.Calendar(firstweekday=6)  # 周日开始
        month_days = cal.monthdayscalendar(year, month)
        
        today = datetime.now().strftime('%Y-%m-%d')
        
        # 日期网格
        grid = tk.Frame(self.calendar_container, bg="white")
        grid.pack(fill=tk.BOTH, expand=True)
        
        today_date = datetime.now().date()
        
        for week in month_days:
            week_frame = tk.Frame(grid, bg="white")
            week_frame.pack(fill=tk.X)
            
            for i, day in enumerate(week):
                if day == 0:
                    tk.Label(week_frame, text="", width=6, height=3, bg="#f8f9fa").pack(side=tk.LEFT, expand=True, padx=1, pady=1)
                else:
                    date_str = f"{year}-{month:02d}-{day:02d}"
                    cell_date = datetime(year, month, day).date()
                    is_checked = date_str in self.data['history']
                    is_today = date_str == today
                    is_weekend = i in [0, 6]
                    is_past = cell_date < today_date
                    
                    if is_checked:
                        bg, fg = "#27ae60", "white"
                    elif is_today:
                        bg, fg = "#3498db", "white"
                    elif is_weekend:
                        bg, fg = "#fff5f5", "#e74c3c"
                    else:
                        bg, fg = "#f8f9fa", "#2c3e50"
                    
                    cell = tk.Frame(week_frame, bg=bg, relief="solid", bd=1, cursor="hand2" if (is_past and not is_checked) else "")
                    cell.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=1, pady=1)
                    
                    lbl = tk.Label(cell, text=str(day), font=("Microsoft YaHei", 14, "bold" if is_today else "normal"),
                            bg=bg, fg=fg, width=5, height=2, cursor="hand2" if (is_past and not is_checked) else "")
                    lbl.pack()
                    
                    if is_checked:
                        tk.Label(cell, text="✓", font=("Arial", 10), bg=bg, fg=fg).pack()
                    
                    # 过去未打卡的日期可以点击补打卡
                    if is_past and not is_checked:
                        cell.bind("<Button-1>", lambda e, d=date_str: self.makeup_checkin(d))
                        lbl.bind("<Button-1>", lambda e, d=date_str: self.makeup_checkin(d))
        
        # 图例
        legend = tk.Frame(self.calendar_container, bg="white")
        legend.pack(pady=10)
        for color, text in [("#27ae60", "已打卡"), ("#3498db", "今天"), ("#f8f9fa", "未打卡 (点击补卡)")]:
            tk.Label(legend, text="  ", bg=color, relief="solid", bd=1).pack(side=tk.LEFT, padx=2)
            tk.Label(legend, text=text, font=("Microsoft YaHei", 9), bg="white", fg="#7f8c8d").pack(side=tk.LEFT, padx=(0,15))
    
    def update_calendar_time(self):
        try:
            # 每分钟检查日期变化
            self.root.after(60000, self.update_calendar_time)
        except: pass
    
    def page_tips(self):
        # 紫色系动态背景
        canvas = self.create_gradient_bg(["#f3e5f5", "#e1bee7", "#ce93d8", "#e1bee7"], 80)
        
        f = tk.Frame(canvas, bg="#fafafa", padx=40, pady=30)
        f.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        tk.Label(f, text="💡 应对冲动技巧 (今日推荐)", font=("Microsoft YaHei", 18, "bold"), bg="#fafafa", fg="#2c3e50").pack(anchor="w", pady=(0,15))
        
        tips = self.get_daily_content(self.TIPS_ALL, 6)
        for i, t in enumerate(tips, 1):
            tk.Label(f, text=f"{i}. {t}", font=("Microsoft YaHei", 12), bg="#f8f9fa", fg="#2c3e50",
                    anchor="w", padx=15, pady=12).pack(fill=tk.X, pady=4)
        
        tk.Label(f, text="💪 你比想象的更强大!", font=("Microsoft YaHei", 14, "bold"),
                bg="#fafafa", fg="#27ae60").pack(pady=20)
    
    def page_list(self, title, items):
        # 根据标题选择不同颜色主题
        if "音乐" in title:
            colors = ["#fff3e0", "#ffe0b2", "#ffcc80", "#ffe0b2"]  # 橙色系
        elif "电影" in title or "视频" in title:
            colors = ["#fce4ec", "#f8bbd0", "#f48fb1", "#f8bbd0"]  # 粉色系
        elif "书籍" in title:
            colors = ["#e8f5e9", "#c8e6c9", "#a5d6a7", "#c8e6c9"]  # 绿色系
        elif "国际" in title:
            colors = ["#e0f7fa", "#b2ebf2", "#80deea", "#b2ebf2"]  # 青色系
        else:
            colors = ["#ffebee", "#ffcdd2", "#ef9a9a", "#ffcdd2"]  # 红色系
        
        canvas = self.create_gradient_bg(colors, 80)
        
        f = tk.Frame(canvas, bg="#fafafa", padx=40, pady=30)
        f.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        tk.Label(f, text=title, font=("Microsoft YaHei", 18, "bold"), bg="#fafafa", fg="#2c3e50").pack(anchor="w", pady=(0,15))
        tk.Label(f, text="点击下方链接即可打开:", font=("Microsoft YaHei", 11), bg="#fafafa", fg="#7f8c8d").pack(anchor="w", pady=(0,10))
        
        for name, url in items:
            lbl = tk.Label(f, text=f"▶ {name}", font=("Microsoft YaHei", 12), bg="#fafafa", 
                          fg="#3498db", cursor="hand2", anchor="w", pady=8)
            lbl.pack(fill=tk.X)
            lbl.bind("<Enter>", lambda e,l=lbl: l.config(fg="#2980b9", font=("Microsoft YaHei", 12, "underline")))
            lbl.bind("<Leave>", lambda e,l=lbl: l.config(fg="#3498db", font=("Microsoft YaHei", 12)))
            lbl.bind("<Button-1>", lambda e,u=url: webbrowser.open(u))
    
    def do_checkin(self):
        today = datetime.now().strftime('%Y-%m-%d')
        if self.data['last'] == today:
            self.msg.config(text="今天已打卡!", fg="#e67e22")
            return
        
        if self.data['last']:
            diff = (datetime.strptime(today, '%Y-%m-%d') - datetime.strptime(self.data['last'], '%Y-%m-%d')).days
            self.data['streak'] = self.data['streak'] + 1 if diff == 1 else 1
        else:
            self.data['streak'] = 1
        
        self.data['last'] = today
        self.data['total'] += 1
        self.data['history'].append(today)
        self.data['longest'] = max(self.data['longest'], self.data['streak'])
        self.save_data()
        
        msgs = ["太棒了!", "继续加油!", "你很强!", "坚持就是胜利!"]
        self.msg.config(text=f"✓ 打卡成功! {random.choice(msgs)}", fg="#27ae60")
        self.show_page("checkin")
    
    def do_relapse(self):
        if not messagebox.askyesno("确认", "确定标记破戒?\n\n失败是成功之母,重新开始!"): return
        reason = simpledialog.askstring("记录", "破戒诱因(可选):")
        self.data['relapse'] += 1
        self.data['streak'] = 0
        self.save_data()
        messagebox.showinfo("加油", "已记录。不要气馁,重新出发!")
        self.show_page("checkin")
    
    def makeup_checkin(self, date_str):
        """补打卡功能"""
        if date_str in self.data['history']:
            messagebox.showinfo("提示", f"{date_str} 已打卡!")
            return
        
        if not messagebox.askyesno("补打卡", f"确认为 {date_str} 补打卡?"):
            return
        
        self.data['history'].append(date_str)
        self.data['total'] += 1
        self.data['history'].sort()  # 保持日期顺序
        
        # 重新计算最长连续天数
        if len(self.data['history']) > 0:
            sorted_dates = sorted(self.data['history'])
            max_streak = 1
            current_streak = 1
            for i in range(1, len(sorted_dates)):
                d1 = datetime.strptime(sorted_dates[i-1], '%Y-%m-%d')
                d2 = datetime.strptime(sorted_dates[i], '%Y-%m-%d')
                if (d2 - d1).days == 1:
                    current_streak += 1
                    max_streak = max(max_streak, current_streak)
                else:
                    current_streak = 1
            self.data['longest'] = max(self.data['longest'], max_streak)
        
        self.save_data()
        messagebox.showinfo("成功", f"{date_str} 补打卡成功!")
        self.draw_calendar()
    
    def reset_field(self, field):
        """清零指定字段"""
        names = {'total': '戒断天数总计', 'longest': '最长连续', 'relapse': '破戒次数'}
        if not messagebox.askyesno("确认清零", f"确定要将「{names.get(field, field)}」清零吗?"):
            return
        
        self.data[field] = 0
        if field == 'total':
            self.data['history'] = []
            self.data['streak'] = 0
            self.data['last'] = None
        self.save_data()
        messagebox.showinfo("已清零", f"{names.get(field, field)} 已清零!")
        self.show_page("checkin")
    
    def update_time(self):
        try:
            now = datetime.now()
            date_str = now.strftime("%Y年%m月%d日")
            time_str = now.strftime("%H:%M:%S")
            self.time_label.config(text=f"📅 {date_str}  ⏰ {time_str}")
            self.root.after(1000, self.update_time)
        except: pass

if __name__ == '__main__':
    root = tk.Tk()
    App(root)
    root.mainloop()
