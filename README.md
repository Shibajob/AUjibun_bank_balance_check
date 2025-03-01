# AUjibun_bank_balance_check

## Overview

Get your AU Jibun Bank balance easily with this Python package.

## Install from source①
```sh
git clone https://github.com/Shibajob/AUjibun_bank_balance_check.git
cd AUjibun_bank_balance_check
pip install .
```

## Install from source②
```sh
pip install git+https://github.com/Shibajob/AUjibun_bank_balance_check.git
```

## Requirements
- Python 3.11.0
- selenium >= 4.5.0
- webdriver-manager >= 4.0.2

## How to use
```python
from AUjibun_bank_balance_check import AUjibun_bank_balance_check

account_id = "your_id"
account_pw = "your_password"

balance = AUjibun_bank_balance_check.AUjibun_bank_balance_check(account_id, account_pw)
print(f"Your balance: {balance}")
```

## LICENSE

This project is licensed under the MIT License.
