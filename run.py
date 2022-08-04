import pytest
import os


if __name__ == '__main__':
    pytest.main(['-s','-v','--alluredir','./target/allure-results','--clean-alluredir'])
    os.system('allure generate -o /target/allure-results')



