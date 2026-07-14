🔹 Arithmetic Operators
Used for basic math.

Operator	           Meaning	Example	Analogy
+	Addition	       5 + 3 → 8	Adding money in wallet
-	Subtraction	       10 - 4 → 6	Spending money
*	Multiplication	6 * 2 → 12	6 chocolates × 2 packs
/	Division	10 / 2 → 5.0	Sharing 10 apples among 2
//	Floor Division	10 // 3 → 3	Quotient only (ignore remainder)
%	Modulus	10 % 3 → 1	Remainder after division
**	Exponent	2 ** 3 → 8	2³ = 8


🔹 Comparison Operators
Used to compare values → result is True/False.

Operator	Meaning	Example	Analogy
==	Equal	5 == 5 → True	Same marks in exam
!=	Not Equal	5 != 3 → True	Different roll numbers
>	Greater	7 > 4 → True	7 chocolates > 4 chocolates
<	Less	3 < 5 → True	3 pens < 5 pens
>=	Greater or Equal	5 >= 5 → True	At least 5 tickets
<=	Less or Equal	4 <= 6 → True	At most 6 players


🔹 Assignment Operators
Used to assign values and update variables.

Operator	Meaning	Example	Analogy
=	Assign	x = 10	Put 10 in box x
+=	Add & assign	x += 2 → x = x + 2	Add 2 chocolates to box
-=	Subtract & assign	x -= 3	Remove 3 chocolates
*=	Multiply & assign	x *= 4	Multiply money by 4
/=	Divide & assign	x /= 2	Share chocolates equally


🔹 Logical Operators
Used to combine conditions.

Operator	Meaning	Example	Analogy
and	Both True	age > 18 and has_id	Need ticket and popcorn
or	At least one True	is_raining or has_umbrella	Umbrella or rain
not	Negation	not is_logged_in	Not hungry → don’t order food


🔹 Membership Operators
Check if a value exists in a collection.

Operator	Meaning	Example	Analogy
in	Present	"apple" in fruits	File inside folder
not in	Absent	"grape" not in fruits	Virus not in system


🔹 Identity Operators
Check if two variables point to the same object in memory.

Operator	Meaning	Example	Analogy
is	Same object	a is b	Two shortcuts → same file
is not	Different objects	a is not c	Two separate files with same content

🔹 1. Simple if
👉 Logic:  
“If condition is True, do something.”

Example Logic (before code):

If marks ≥ 35 → Print “Pass”.

Code:

python
marks = 40
if marks >= 35:
    print("Pass")
✅ Analogy: If you have a ticket, you can enter the movie hall.

🔹 2. if...else
👉 Logic:  
“If condition is True, do something. Otherwise, do something else.”

Example Logic:

If marks ≥ 35 → Print “Pass”

Else → Print “Fail”

Code:

python
marks = 30
if marks >= 35:
    print("Pass")
else:
    print("Fail")
✅ Analogy: If you have a ticket → enter. Else → go home.

🔹 3. if...elif...else
👉 Logic:  
Multiple conditions checked one by one.

Example Logic:

If marks ≥ 90 → Print “Grade A”

Else if marks ≥ 75 → Print “Grade B”

Else if marks ≥ 35 → Print “Pass”

Else → Print “Fail”

Code:

python
marks = 80
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 35:
    print("Pass")
else:
    print("Fail")
✅ Analogy: If you score 90+, you’re topper. Else if 75+, good. Else if 35+, just passed. Else, failed.

🔹 4. Nested if
👉 Logic:  
An if inside another if.

Example Logic:

If age ≥ 18 → Check if has ID

If has ID → Print “Allowed”

Else → Print “ID required”

Else → Print “Too young”

Code:

python
age = 20
has_id = False

if age >= 18:
    if has_id:
        print("Allowed")
    else:
        print("ID required")
else:
    print("Too young")