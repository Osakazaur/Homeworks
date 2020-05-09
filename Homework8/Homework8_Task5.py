'''
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать
любую подходящую структуру, например словарь.
'''


class Storage:

    def __init__(self, model_name: str, width: int, height: int, depth: int, mass: int):
        self.model_name = model_name
        self.width = width
        self.height = height
        self.depth = depth
        self.mass = mass


class Printer(Storage):

    count = 0

    def __init__(self, model_name: str, color: bool, paper_max_format: str, width: int, height: int, depth: int, mass: int):
        self.tech_name = 'printer'
        self.count += 1
        if color:
            self.color_type = 'color'
        else:
            self.color_type = 'black&white'
        self.paper_max_format = paper_max_format
        super().__init__(model_name, width, height, depth, mass)

    def storage_place(self):
        print('This {0} {1} takes {2}x{3}x{4}. You have {5} {1}'.format(self.color_type, self.tech_name, self.width,
                                                                        self.height, self.depth, self.count))


class Scanner(Storage):

    count = 0

    def __init__(self, model_name: str, paper_max_format: str, width: int, height: int, depth: int, mass: int):
        self.tech_name = 'scanner'
        self.count += 1
        self.paper_max_format = paper_max_format
        super().__init__(model_name, width, height, depth, mass)

    def storage_place(self):
        print('This {0} {1} takes {2}x{3}x{4}. You have {5} {1}(s)'.format(self.paper_max_format, self.tech_name,
                                                                           self.width, self.height, self.depth,
                                                                           self.count))


class MFP(Printer, Scanner):

    count = 0

    def __init__(self, model_name: str, color: bool, is_fax: bool, paper_max_format: str, width: int, height: int, depth: int, mass: int):
        self.tech_name = 'MFP'
        self.count += 1
        self.is_fax = is_fax
        super().__init__(model_name, color, paper_max_format, width, height, depth, mass)

    def storage_place(self):
        print('This {0} {1} {2} takes {3}x{4}x{5}. You have {6} {2}(s)'.format(self.color_type, self.paper_max_format,
                                                                               self.tech_name, self.width, self.height,
                                                                               self.depth, self.count))

