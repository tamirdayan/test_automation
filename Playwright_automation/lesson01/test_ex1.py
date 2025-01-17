class Test_ex1:
    def setup_method(self):
        print("setup_method")

    def teardown_method(self):
        print("teardown_method")

    def setup_class(self):
        print("\nsetup_class")

    def teardown_class(self):
        print("teardown_class")

    def test_01(self):
        print("test_01")

    def test_02(self):
        print("test_02")
