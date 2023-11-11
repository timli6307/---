# q03.py
from pkg.modu import print_json, process_data, read_json, write_json

MENU_FILE = 'menu.json'       # 輸入檔案名稱
OUTPUT_FILE = 'output.json'   # 輸出檔案名稱

def main():
    # 讀取菜單並顯示
    menu = read_json(MENU_FILE)
    print_json(menu)

    # 增加新的主菜項目
    new_item = {
        "name": "海鮮燉飯",
        "price": 239,
        "description": "西班牙的代表美食，海鮮配料豐富、色彩繽紛"
    }
    menu['categories'][1]['items'].append(new_item)

    # 輸入折數
    discount = float(input("請輸入折扣率(0.0 ~ 1.0): "))

    # 將菜單進行打折處理
    process_data(menu, discount)

    # 顯示打折後的菜單
    print_json(menu)

    # 寫入檔案
    write_json(menu, OUTPUT_FILE)

if __name__ == "__main__":
    main()
