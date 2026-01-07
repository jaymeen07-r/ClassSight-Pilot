import pandas as pd
import os
import random
import string
from messaging_system import *
from datetime import datetime
from auth.login import *


if __name__=="__main__":
    while True:
        login_or_signup()
        cont = input("Do you want to continue? (y/n): ").strip().lower()
        if cont!="y":
            print("Exiting system...")
            break
