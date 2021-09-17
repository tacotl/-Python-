# 练习8-15：打印模型 将示例printing_models.py中的函数放在一个名为printing_functions.py的文件中。在printing_models.py的开头编写一条import 语句，并修改该文件以使用导入的函数。
from printing_functions import *
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


# 练习8-16：导入 选择一个你编写的且只包含一个函数的程序，将该函数放在另一个文件中。在主程序文件中，使用下述各种方法导入这个函数，再调用它：
import printing_functions
from printing_functions import print_models
from printing_functions import print_models as pm
import printing_functions as pm
from printing_functions import *