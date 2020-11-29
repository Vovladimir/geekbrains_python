'''
пишем сперва программу, потом подгоняем под классы
'''


class Depot:
    my_summary_depo = []

    def __init__(self):
        self.my_depo = []
        self.product = {}

    def analisis_depo(self):
        return f"Сейчас всего на складе:\n {self.my_summary_depo}"

    def from_depot(self):
        try:
            minus_count = int(input(f'Сколько {self.product["название"]} забираем в магазин'
                                    f'(всего: {self.product["количество"]}): '))

            if self.product["количество"] - minus_count < 0:
                raise ValueError
            else:
                self.product["количество"] = self.product["количество"] - minus_count
            print(f"Вы перенесли со склада {minus_count} товара.\n"
                  f"На складе осталось {self.product['количество']} {self.product['название']}.")
            self.my_depo.append(self.product)

        except ValueError:
            print('Ошибка ввода! Убедитесь, что ввели число и оно не больше кол-ва товара на складе.')
            Depot.from_depot(self)


class Printer(Depot):

    def __init__(self, name_brand, price, units_count, type_printer='lazer'):
        super().__init__()
        self.name_brand = name_brand
        self.price = price
        self.units_count = units_count
        self.product = {"название": name_brand, "цена": price, "количество": units_count}
        self.type_printer = type_printer
        self.printer_product = self.product.update({'тип принтера': type_printer})
        self.my_summary_depo.append(self.product)
        self.my_depo.append(self.product)
        print(f"Вы положили на склад: \n"
              f"Принтеры '{name_brand}' (тип принтера: {type_printer}) в количестве {units_count} шт. "
              f"{price} рублей за штуку.")


class Scanner(Depot):

    def __init__(self, name_brand, price, units_count, purpose='domestic'):
        super().__init__()
        self.name_brand = name_brand
        self.price = price
        self.units_count = units_count
        self.product = {"название": name_brand, "цена": price, "количество": units_count}
        self.purpose = purpose
        self.scanner_product = self.product.update({'тип сканера': purpose})
        self.my_summary_depo.append(self.product)
        print(f"Вы положили на склад: \n"
              f"Сканеры '{name_brand}' (тип сканера: {purpose}) в количестве {units_count} шт. "
              f"{price} рублей за штуку.")


class CopyMachine(Depot):

    def __init__(self, name_brand, price, units_count, classification='photocopy'):
        super().__init__()
        self.name_brand = name_brand
        self.price = price
        self.units_count = units_count
        self.product = {"название": name_brand, "цена": price, "количество": units_count}
        self.classification = classification
        self.copyer_product = self.product.update({'тип копира': classification})
        self.my_summary_depo.append(self.product)
        print(f"Вы положили на склад: \n"
              f"Копиры '{name_brand}' (тип копира: {classification}) в количестве {units_count} шт. "
              f"{price} рублей за штуку.")


depot = Depot()

printer_1 = Printer('HP', 30000, 40, 'lazer')
printer_2 = Printer('LaserJet', 25000, 50, 'injekt')
scanner_1 = Scanner('LG', 23000, 50)
copy_2 = CopyMachine('Sony', 12500, 33, 'monochromium')

printer_1.from_depot()
scanner_1.from_depot()
copy_2.from_depot()

print(depot.analisis_depo())
