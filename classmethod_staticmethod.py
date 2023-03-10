class ClassTest:
    def instace_method(self):
        print(f"Called instace_method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        print("Called static_method")


test = ClassTest()

test.instace_method()
ClassTest.instace_method(test)

ClassTest.class_method()

ClassTest.static_method()

