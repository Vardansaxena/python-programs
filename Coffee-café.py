print('   welcome to coffee Café\n')
print(''' before enter into menu bar u need to\n 
          sign up\n
          because our services is new''')
username = input('choose your username ')
id_no = int(input('choose id number maybe as pin '))
print('successfuly created username & id')

print('now, please login')

check = input('enter your username')
check_id = int(input('enter your id or pin'))

if username == check:
    True
    if id_no == check_id:
        True
        print(''' WELCOME 
                  Menu
                  1) expresso.............$3
                  2) double expresso......$5
                  3) cappacino............$4
                  4) latte................$4
                  5) americano............$3
                  6) mocha................$4
                  7) falt white...........$2 
                  8) short black..........$2
                  9) long black...........$2''')

        choice = int(input('what item you want to order'))

        if choice == 1:
            print('you want expresso: $3')
            price = 3
            quantity = int(input('quantity'))
            bucks = price*quantity
            print(f'you have to pay {bucks} $ ')
            print('''we only accept card
                     1) credit card
                     2) debit card ''')
            option = int(input(''' procced to payment '''))
            if option == 1:
                print('credit card details:')
                card_number = int(input('enter card number'))
                date = int(input('enter date '))
                month = int(input('enter month'))
                cvv = int(input('enter cvv'))
                print('great payment successful')
            elif option == 2:
                print('debit card details:')
                card_number = int(input('enter card number'))
                date = int(input('enter date '))
                month = int(input('enter month'))
                cvv = int(input('enter cvv'))
                print('great payment successful')
                print('wait your order ready in 15min')

            else:
                print('failed')
        elif choice == 2:
            print('you want double expresso')
            price = 5
            quantity = int(input('quantity'))
            bucks = price*quantity
            print(f'you have to pay {bucks} $')
            print('''we only accept card
                     1) credit card
                     2) debit card ''')
            option = int(input(''' procced to payment '''))
            if option == 1:
                print('credit card details:')
                card_number = int(input('enter card number'))
                date = int(input('enter date '))
                month = int(input('enter month'))
                cvv = int(input('enter cvv'))
                print('great payment successful')
            elif option == 2:
                print('debit card details:')
                card_number = int(input('enter card number'))
                date = int(input('enter date '))
                month = int(input('enter month'))
                cvv = int(input('enter cvv'))
                print('great payment successful')
                print('wait your order ready in 15min')

            else:
                print('failed')

        elif choice == 3:
            print('you want cappacino')
            price = 4
            quantity = int(input('quantity'))
            bucks = price*quantity
            print(f'you have to pay {bucks} $')
            print('''we only accept card
                     1) credit card
                     2) debit card ''')
            option = int(input(''' procced to payment '''))
            if option == 1:
                print('credit card details:')
                card_number = int(input('enter card number'))
                date = int(input('enter date '))
                month = int(input('enter month'))
                cvv = int(input('enter cvv'))
                print('great payment successful')
            elif option == 2:
                print('debit card details:')
                card_number = int(input('enter card number'))
                date = int(input('enter date '))
                month = int(input('enter month'))
                cvv = int(input('enter cvv'))
                print('great payment successful')
                print('wait your order ready in 15min')

            else:
                print('failed')

        elif choice == 4:
            print('you want double latte')
            price = 4
            quantity = int(input('quantity'))
            bucks = price*quantity
            print(f'you have to pay {bucks} $')
            print('''we only accept card
                     1) credit card
                     2) debit card ''')
            option = int(input(''' procced to payment '''))
            if option == 1:
                print('credit card details:')
                card_number = int(input('enter card number'))
                date = int(input('enter date '))
                month = int(input('enter month'))
                cvv = int(input('enter cvv'))
                print('great payment successful')
            elif option == 2:
                print('debit card details:')
                card_number = int(input('enter card number'))
                date = int(input('enter date '))
                month = int(input('enter month'))
                cvv = int(input('enter cvv'))
                print('great payment successful')
                print('wait your order ready in 15min')

            else:
                print('failed')

        elif choice == 5:
            print('you want americano')
            price = 3
            quantity = int(input('quantity'))
            bucks = price*quantity
            print(f'you have to pay {bucks} $')
            print('''we only accept card
                     1) credit card
                     2) debit card ''')
            option = int(input(''' procced to payment '''))
            if option == 1:
                print('credit card details:')
                card_number = int(input('enter card number'))
                date = int(input('enter date '))
                month = int(input('enter month'))
                cvv = int(input('enter cvv'))
                print('great payment successful')
            elif option == 2:
                print('debit card details:')
                card_number = int(input('enter card number'))
                date = int(input('enter date '))
                month = int(input('enter month'))
                cvv = int(input('enter cvv'))
                print('great payment successful')
                print('wait your order ready in 15min')

            else:
                print('failed')

        elif choice == 6:
            print('you want double mocha')
            price = 4
            quantity = int(input('quantity'))
            bucks = price*quantity
            print(f'you have to pay {bucks} $')
            print('''we only accept card
                     1) credit card
                     2) debit card ''')
            option = int(input(''' procced to payment '''))
            if option == 1:
                print('credit card details:')
                card_number = int(input('enter card number'))
                date = int(input('enter date '))
                month = int(input('enter month'))
                cvv = int(input('enter cvv'))
                print('great payment successful')
            elif option == 2:
                print('debit card details:')
                card_number = int(input('enter card number'))
                date = int(input('enter date '))
                month = int(input('enter month'))
                cvv = int(input('enter cvv'))
                print('great payment successful')
                print('wait your order ready in 15min')

            else:
                print('failed')

        elif choice == 7:
            print('you want flat white')
            price = 2
            quantity = int(input('quantity'))
            bucks = price*quantity
            print(f'you have to pay {bucks} $')
            print('''we only accept card
                     1) credit card
                     2) debit card ''')
            option = int(input(''' procced to payment '''))
            if option == 1:
                print('credit card details:')
                card_number = int(input('enter card number'))
                date = int(input('enter date '))
                month = int(input('enter month'))
                cvv = int(input('enter cvv'))
                print('great payment successful')
            elif option == 2:
                print('debit card details:')
                card_number = int(input('enter card number'))
                date = int(input('enter date '))
                month = int(input('enter month'))
                cvv = int(input('enter cvv'))
                print('great payment successful')
                print('wait your order ready in 15min')

            else:
                print('failed')

        elif choice == 8:
            print('you want short black')
            price = 2
            quantity = int(input('quantity'))
            bucks = price*quantity
            print(f'you have to pay {bucks} $')
            print('''we only accept card
                     1) credit card
                     2) debit card ''')
            option = int(input(''' procced to payment '''))
            if option == 1:
                print('credit card details:')
                card_number = int(input('enter card number'))
                date = int(input('enter date '))
                month = int(input('enter month'))
                cvv = int(input('enter cvv'))
                print('great payment successful')
            elif option == 2:
                print('debit card details:')
                card_number = int(input('enter card number'))
                date = int(input('enter date '))
                month = int(input('enter month'))
                cvv = int(input('enter cvv'))
                print('great payment successful')
                print('wait your order ready in 15min')

            else:
                print('failed')

        elif choice == 9:
            print('you want dlong black')
            price = 2
            quantity = int(input('quantity'))
            bucks = price*quantity

            print('''we only accept card
                     1) credit card
                     2) debit card ''')
            option = int(input(''' procced to payment '''))
            if option == 1:
                print('credit card details:')
                card_number = int(input('enter card number'))
                date = int(input('enter date '))
                month = int(input('enter month'))
                cvv = int(input('enter cvv'))
                print('great payment successful')
            elif option == 2:
                print('debit card details:')
                card_number = int(input('enter card number'))
                date = int(input('enter date '))
                month = int(input('enter month'))
                cvv = int(input('enter cvv'))
                print('great payment successful')
                print('wait your order ready in 15min')

            else:
                print('failed')

        else:
            print('wrong choice see the menu and enter item number carefully')



else:
    print('incorrect detail please check your information is correct or not')






