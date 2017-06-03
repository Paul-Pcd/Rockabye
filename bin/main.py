import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from moudles import modules

"""
堡垒机入口
"""

if __name__ == '__main__':
    modules.run()