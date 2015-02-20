#Private API of KryptoPay


##Target:
https://kryptopay.pl/api
####GRAPHIC (simple)
Creating transaction:


https://kryptopay.pl/api/create/


View of transaction


Default: https://kryptopay.pl/api/payments/


Polish version: https://kryptopay.pl/api/payments/pl/


English version: https://kryptopay.pl/api/payments/en/

####JSON (All account information and accessories)
https://kryptopay.pl/api/json/info/


https://kryptopay.pl/api/json/create/


https://kryptopay.pl/api/json/withdrawals/



##Code examples:
####PHP : https://github.com/Kryptopay/api/tree/master/php
####PYTHON V2/V3 : https://github.com/Kryptopay/api/tree/master/python

##Target variables:
api_public_key (sh1 string)


api_private_key (sh2 string)


amount (float)
##Additional variables:
order_nr (only a-z A-Z 1-9)


description (only a-z A-Z 1-9 and ',')


company (only a-z A-Z 1-9)


name (only a-z A-Z)


surname (only a-z A-Z)


address string(only a-z A-Z 1-9 and ',')


url 


===
##Errors list:
403 - too many attempts


402 - an incorrect amount


401 - the amount above limit


400 - invalid data of user
