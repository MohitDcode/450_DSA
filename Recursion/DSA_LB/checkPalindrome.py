def isPalRec(st, s, e) :
	# base case
	if (s == e):
		return True

	# processing
	if (st[s] != st[e]) :
		return False

	# Recursive relation
	if (s < e + 1) :
		return isPalRec(st, s + 1, e - 1)
	return True

def isPalindrome(st) :
	n = len(st)
	if (n == 0): # considered as palindrome
		return True
	return isPalRec(st, 0, n - 1)

# Driver Code
st = "geeg"
if (isPalindrome(st)) :
	print("Yes")
else :
	print("No")