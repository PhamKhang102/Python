import os
from colorama import Fore, Style, init

init(autoreset=True)

try:
    import ms4
except ImportError:
    os.system('pip install ms4==2.10.0')
    os.system("clear")

from ms4 import InfoTik

nguoi_dung = input(Fore.CYAN + Style.BRIGHT + ' 🔹 ID TikTok: ').strip()

thong_tin = InfoTik.TikTok_Info(nguoi_dung)

if 'bad' in thong_tin['status']:
    print(Fore.RED + Style.BRIGHT + ' ❌ Tên người dùng không hợp lệ!')
elif 'ok' in thong_tin['status']:
    def get_info(key, default="⚠️ Không có dữ liệu!"):
        return str(thong_tin.get(key, default)).strip()

    ten = get_info('name')
    nguoi_theo_doi = get_info('followers')
    dang_theo_doi = get_info('following')
    luot_thich = get_info('like')
    so_video = get_info('video')
    co = get_info('flag')
    quoc_gia = get_info('country')
    ngay_tao = get_info('Date')
    ma_so = get_info('id')
    tieu_su = get_info('bio')

    print(Fore.LIGHTWHITE_EX + Style.BRIGHT + f'''
╔════════════════════════════════════════╗
║         {Fore.YELLOW}📌 THÔNG TIN TÀI KHOẢN 📌{Fore.LIGHTWHITE_EX}        ║
╠════════════════════════════════════════╣
║ {Fore.GREEN}👤 Tên người dùng:{Fore.WHITE} {nguoi_dung}             
║ {Fore.GREEN}🏷️  Tên hiển thị:{Fore.WHITE} {ten}           
╠════════════════════════════════════════╣
║ {Fore.GREEN}👥  Người theo dõi:{Fore.WHITE} {nguoi_theo_doi}         
║ {Fore.GREEN}🔄  Đang theo dõi:{Fore.WHITE} {dang_theo_doi}         
╠════════════════════════════════════════╣
║ {Fore.GREEN}❤️ Lượt thích:{Fore.WHITE} {luot_thich}       
║ {Fore.GREEN}🎞️  Số video:{Fore.WHITE} {so_video}      
╠════════════════════════════════════════╣
║ {Fore.GREEN}🚩  Cờ:{Fore.WHITE} {co}            
║ {Fore.GREEN}🌍  Quốc gia:{Fore.WHITE} {quoc_gia}        
║ {Fore.GREEN}📅  Ngày tạo:{Fore.WHITE} {ngay_tao}        
║ {Fore.GREEN}🆔  ID:{Fore.WHITE} {ma_so}           
╠════════════════════════════════════════╣
║ {Fore.GREEN}📜  Tiểu sử:{Fore.WHITE} {tieu_su}         
╚════════════════════════════════════════╝
{Fore.RED} Telegram: {Fore.YELLOW}https://t.me/sharetoolvncom
''')