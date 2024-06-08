def kiosk_program():
    menu = ["냉면", "볶음밥", "피자", "짜장면"]

    while True:
        try:

            user_input = input("메뉴를 선택하세요 (1: 냉면, 2: 볶음밥, 3: 피자, 4: 짜장면): ")


            menu_number = int(user_input)


            selected_menu = menu[menu_number - 1]


            print(f"선택하신 메뉴는 {selected_menu}입니다.")
            break

        except ValueError:

            print("잘못된 입력입니다. 숫자를 입력해주세요.")
        except IndexError:

            print("메뉴에 없는 번호입니다. 1에서 4 사이의 숫자를 입력해주세요.")



kiosk_program()