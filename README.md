# simple-ATM
implementation of simple ATM system

Insert Card => PIN number => Select Account => See Balance/Deposit/Withdraw is implemented

## clone and run
+ clone
```commandline
git clone https://github.com/sem1308/simple-ATM.git
cd ./simple-ATM
```
+ run
```commandline
python main.py
```
+ **in main.py, there are dummy datas for account and card.**
    + if you want, manipulate them
## UI 
###### if you run this system, you can see this UI
```commandline
========= ATM =========
[1] INSERT_CARD
[any button] EXIT
select wanted num :
```

###### if input 1,you can see this UI
```commandline
========= CARD UI =========
Enter card number (include '-') : 
```
+ i can't develop hardware system, so manually get card informations
+ If the entered card information is not in the dummy data, it will go back to the beginning.
+ Here is the result of entering the correct information
```commandline
Enter card number (include '-') : 4579-7300-7124-7055
Enter valid thru (ex 11/23) : 24/08
Enter cvc (ex 012) : 302
```

###### then you can see this UI
```commandline
========= PIN NUMBER UI =========
Enter pin number : 
```
+ The pin number exists in the dummy card data, so write it down as a reference
+ if write incorrect number, you can choose return to home or rewrite number
+ Here is the result of entering the correct information
```commandline
========= PIN NUMBER UI =========
Enter pin number : 1234
```

###### then you can see this UI
```
========= ACCOUNTS UI =========
[0] - 한국은행 , 111112341234
[1] - 기업은행 , 333312341234
[any else button] : exit
select wanted num : 
```
+ you can select account by number

###### if you enter 0, this UI will be seen
```commandline
=== Functions ===
[1] SEE_BALANCE
[2] DEPOSIT
[3] WITHDRAW
[4] HOME
select wanted num : 
```
+ yes, you can use these functions (see balance, deposit, withdraw, return to home)
    + case input 1 (SEE_BALANCE)
        ```
        ## SEE_BALANCE ##
        balance : 100000$
        ```
    + case input 2 (DEPOSIT)
        ```
        ## DEPOSIT ##
        Enter amount of deposit money($) : 40000 # input yourself
        ```
        ```commandline
        === before balance ===
        balance : 100000$
        
        40000$ was deposited to 111112341234
        === after balance ===
        balance : 140000$
        ```
    + case input 3 (WITHDRAW)
        ```
        ## WITHDRAW ##
        Enter amount of withdraw money($) : 100000 # input yourself
        ```
        ```commandline
        ===== before balance =====
        balance : 140000$
      
        100000$ was withdrawn from 111112341234
        ===== after balance =====
        balance : 40000$
        ```
        + if lack of balance, you can see it
        ```
        ## WITHDRAW ##
        Enter amount of withdraw money($) : 100000
        ===== before balance =====
        balance : 40000$
        withdrawl denied due to 'lack of balance'
        ===== after balance =====
        balance : 40000$
        ```
        + if ATM has lack of cash, you can see it
        ```commandline
        ## WITHDRAW ##
        Enter amount of withdraw money($) : 120000
        withdrawl denied due to 'lack of cash of ATM'
        ```
    + case input 4 (HOME)
        ```
        return to home.
        
        ========= ATM =========
        [1] INSERT_CARD
        [any button] EXIT
        select wanted num :
        ```
      
## test case
+ this system get input sequentially so test case's output may seem a little weird 
+ run by "python main.py" and copy input case and paste to terminal
<details>
<summary>case 1</summary>

+ input
```commandline
1
4579-7300-7124-7055
24/08
302
1234
0
1
2
40000
3
200000
3
100000
4
2

```
+ output
```commandline
========= CARD UI =========
Enter card number (include '-') : Enter valid thru (ex 11/23) : Enter cvc (ex 012) : 
========= PIN NUMBER UI =========
Enter pin number : 
========= ACCOUNTS UI =========
[0] - 한국은행 , 111112341234
[1] - 기업은행 , 333312341234
select wanted num : 
=== Functions ===
[1] SEE_BALANCE
[2] DEPOSIT
[3] WITHDRAW
[4] HOME
select wanted num : 
## SEE_BALANCE ##
balance : 100000$

=== Functions ===
[1] SEE_BALANCE
[2] DEPOSIT
[3] WITHDRAW
[4] HOME
select wanted num : 
## DEPOSIT ##
Enter amount of deposit money($) : === before balance ===
balance : 100000$

40000$ was deposited to 111112341234
=== after balance ===
balance : 140000$

=== Functions ===
[1] SEE_BALANCE
[2] DEPOSIT
[3] WITHDRAW
[4] HOME
select wanted num : 
## WITHDRAW ##
Enter amount of withdraw money($) : ===== before balance =====
balance : 140000$

withdrawl denied due to 'lack of balance'
===== after balance =====
balance : 140000$

=== Functions ===
[1] SEE_BALANCE
[2] DEPOSIT
[3] WITHDRAW
[4] HOME
select wanted num : 
## WITHDRAW ##
Enter amount of withdraw money($) : ===== before balance =====
balance : 140000$

100000$ was withdrawn from 111112341234
===== after balance =====
balance : 40000$

=== Functions ===
[1] SEE_BALANCE
[2] DEPOSIT
[3] WITHDRAW
[4] HOME
select wanted num : 
return to home.

=== ATM ===
[1] INSERT_CARD
[any button] EXIT
select wanted num : 
Process finished with exit code 0

```
</details>

<details>
<summary>case 2</summary>

+ input
```commandline
1
4579-7300-7124-7055
24/08
302
1234
1
1
2
40000
3
200000
3
100000
4
2

```
+ output
```commandline
========= CARD UI =========
Enter card number (include '-') : Enter valid thru (ex 11/23) : Enter cvc (ex 012) : 
========= PIN NUMBER UI =========
Enter pin number : 
========= ACCOUNTS UI =========
[0] - 한국은행 , 111112341234
[1] - 기업은행 , 333312341234
select wanted num : 
=== Functions ===
[1] SEE_BALANCE
[2] DEPOSIT
[3] WITHDRAW
[4] HOME
select wanted num : 
## SEE_BALANCE ##
balance : 553000$

=== Functions ===
[1] SEE_BALANCE
[2] DEPOSIT
[3] WITHDRAW
[4] HOME
select wanted num : 
## DEPOSIT ##
Enter amount of deposit money($) : === before balance ===
balance : 553000$

40000$ was deposited to 333312341234
=== after balance ===
balance : 593000$

=== Functions ===
[1] SEE_BALANCE
[2] DEPOSIT
[3] WITHDRAW
[4] HOME
select wanted num : 
## WITHDRAW ##
Enter amount of withdraw money($) : ===== before balance =====
balance : 593000$

200000$ was withdrawn from 333312341234
===== after balance =====
balance : 393000$

=== Functions ===
[1] SEE_BALANCE
[2] DEPOSIT
[3] WITHDRAW
[4] HOME
select wanted num : 
## WITHDRAW ##
Enter amount of withdraw money($) : ===== before balance =====
balance : 393000$

100000$ was withdrawn from 333312341234
===== after balance =====
balance : 293000$

=== Functions ===
[1] SEE_BALANCE
[2] DEPOSIT
[3] WITHDRAW
[4] HOME
select wanted num : 
return to home.

=== ATM ===
[1] INSERT_CARD
[any button] EXIT
select wanted num : 


Process finished with exit code 0

```
</details>


